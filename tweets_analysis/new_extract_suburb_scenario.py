"""this is a function used to extract file in couchdb"""

import couchdb
import pandas as pd
import re
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import nltk
nltk.download('vader_lexicon')
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# set up some global variables:
melb_map = json.load(open('greater_melb_sub.json'))
# save all suburb names in melbourne as a list
mel_suburbs = [i['properties']["name"] for i in melb_map["features"]]
# boundary file - dictionary

"""this is a function used to extract file in couchdb"""
# set some list used to save location and doc on local
location_list = []  # store profile locaiton
place_list = []  # store suburb in place
coordinate_list = []  # store the analyzed suburb in coordinates
no_place_list = []
#!!!store the output dic for all tweet
dic_list = []
#rename nltk sentiment module
sid = SentimentIntensityAnalyzer()


# used to normalized name, to get rid of mistype
def normalize_sub_name(input_name):
    #find out if it is in the location list
    #print("new word in nomal:",input_name)
    for suburb in mel_suburbs:
        if input_name.lower() == suburb.lower():
            return suburb
    return None


# used to turn coordinate to suburb
def cor_suburb(coordinates):
    for i in melb_map["features"]:
        if Polygon(i["geometry"]["coordinates"][0]).contains(Point(coordinates)):
            return i['properties']["name"]
    return None


# use to find out suburb in user profile
def suburb_in_profile(location):
    # we send a the userprofile locaiton in,1 need to do preprocess
    location_words = re.sub(r'[^\w\s]', '', location.lower()).split()
    if "melbourne" not in location_words and "mel" not in location_words and "melb" not in location_words:
        new_word = ""
        for word in location_words:
            if word != "australia":
                if new_word == "":
                    new_word = word
                else:
                    new_word = new_word + " " + word
        normalized_suburb = normalize_sub_name(new_word)
        # it is suburb
        if normalized_suburb:
            return normalized_suburb
        # name have melbourne or vic, first consider type:(suburb,melbourne,vic) or (suburb, vic)
    if "melbourne" in location_words or "victoria" in location_words:
        if location.lower() != "melbourne":
            #("test:",location_words)
            new_word = ""
            for word in location_words:
                if word != "victoria" and word != "australia" and word != "melbourne":
                    if new_word == "":
                        new_word = word
                    else:
                        new_word = new_word + " " + word
            #print("new_word:",new_word)
            normalized_suburb = normalize_sub_name(new_word)
            #print("normalized name:", normalized_suburb)
            if normalized_suburb:
                return normalized_suburb
    # now consider suburb name contain melbourne like east melb
    if "melbourne" in location_words:
        if location.lower() != "melbourne":
            #print("测试2:",location_words)
            new_word = ""
            for word in location_words:
                if word != "victoria" and word != "australia":
                    if new_word == "":
                        new_word = new_word + word
                    else:
                        new_word = new_word + " " + word
            #print("new_word:",new_word)
            if new_word == "melbourne city" or new_word == "melbourne melbourne":
                return "MELBOURNE"
            if new_word != "melbourne":
                normalized_suburb = normalize_sub_name(new_word)
                if normalized_suburb:
                    return normalized_suburb
                else:
                    return None


# handle tweet
def find_suburb(tweet):
    # define an trigger to judge if we go into the condition
    count = 0
    # we first discuss coordinate, if we have coordinates, we translate it to suburb
    if tweet["coordinates"]:
        # print(tweet["coordinates"])
        long, lat = tweet["coordinates"]["coordinates"][0], tweet["coordinates"]["coordinates"][1]
        sub = cor_suburb([long, lat])
        if sub != None:
            print("coordinate", [long, lat, sub])
            # database.save({"suburb":sub,"doc":tweet["full_text"]})
            coordinate_list.append({"suburb": sub, "doc": tweet["full_text"]})
            count = 1
            text = tweet["full_text"]
            id = tweet["_id"]
            return id , text , sub

    # then if palce value is not null then we can extract it directly
    if count == 0:
        if tweet["place"]:
            if tweet["place"]["place_type"] == "neighborhood":
                old_name = tweet["place"]["name"]
                normalized_name = normalize_sub_name(old_name)
                if normalized_name:
                    # database.save({"suburb": normalized_name, "doc": tweet["full_text"]})
                    place_list.append({"suburb": normalized_name, "doc": tweet["full_text"]})
                    print("place:", normalized_name,"       true place:",tweet["place"]["name"])
                    count = 1
                    id = tweet["_id"]
                    text = tweet["full_text"]
                    return id, text , normalized_name

    # then location is our last chance to get locaiton,we need to preprosess the doc
    if count == 0:
        if tweet["user"]["location"]:
            location = suburb_in_profile(tweet["user"]["location"])
            if location:
                print("location:", location, "     true location:", tweet["user"]["location"])
                location_list.append({"location": location, "doc": tweet["full_text"]})
                text = tweet["full_text"]
                id = tweet["_id"]
                return id , text, location
                # database.save({"location":location, "doc": tweetJS})
            else:
                text = tweet["full_text"]
                no_place_list.append({"doc": tweet["full_text"]})
                id = tweet["_id"]
                return id , text , "None"
    return "None", "None" , "None"

#use to find text`s sentiment
def find_sentiment(text):
    if text != None:
        ss = sid.polarity_scores(text)
        if ss['neu'] == 1:
            return 0,1,0
        elif ss['pos'] > ss['neg']:
            return 1,0,0
        else:
            return 0,0,1
    else:
        return 0,0,0

#used to find text related to china
def find_china(text):
    if text != None:
        text = re.sub(r'[^\w\s]', '', text.lower())
        china_list = ['china', 'cn']
        for item in china_list:
            if item.lower() in text:
                return 1
            else:
                return 0


#used to find text related to covid_19
def find_covid_19(text):
    if text:
        text = re.sub(r'[^\w\s]', '', text.lower())
        covid_19_list = ['covid','covid_19','coronavirus','virus','covid19','covid-19','covid 19', 'corona']
        for item in covid_19_list:
            if item.lower() in text:
                return 1
            else:
                return 0


# handle all the data
def execute(old_dic):
    id , text , suburb_name = find_suburb(old_dic)
    new_dic = {}
    if suburb_name != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        # dic_list.append({"tweet_id":id,"suburb":suburb_name,"text":text,"pos":pos,"neu":neu,"neg":neg,"is_china":is_china,"is_covid_19":is_covid_19})
        new_dic = {
            'tweet_id': id,
            'suburb':suburb_name,
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic


#print("place:", len(place_list))
#print("coordinates:", len(coordinate_list))
#print("location:", len(location_list))
#print("no place:", len(no_place_list))

#{id:,suburb:"a",doc:"text",iscovid19:0,ischina:1,pos:1,neu:0,neg:0}
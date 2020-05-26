import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#rename nltk sentiment module
sid = SentimentIntensityAnalyzer()
# #use to find text`s sentiment
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
#
# #used to find text related to china
def find_china(text):
    if text != None:
        text = re.sub(r'[^\w\s]', '', text.lower())
        china_list = ['china', 'cn']
        for item in china_list:
            if item.lower() in text:
                return 1
            else:
                return 0

# #used to find text related to covid_19
def find_covid_19(text):
    if text:
        text = re.sub(r'[^\w\s]', '', text.lower())
        covid_19_list = ['covid','covid_19','coronavirus','virus','covid19','covid-19','covid 19', 'corona']
        for item in covid_19_list:
            if item.lower() in text:
                return 1
            else:
                return 0

def execute_adelaide(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Adelaide',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

def execute_brisbane(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Brisbane',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic


def execute_canberra(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Australian Capital Territory',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

def execute_darwin(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Darwin',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

def execute_hobart(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Hobart',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

def execute_melbourne(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Melbourne',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic


def execute_perth(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Perth',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

def execute_sydney(id,text):
    new_dic = {}
    if text != "None":
        pos , neu , neg = find_sentiment(text)
        is_china = find_china(text)
        is_covid_19 = find_covid_19(text)
        new_dic = {
            'tweet_id': id,
            'suburb':'Greater Sydney',
            'text': text,
            'pos': pos ,
            'neu': neu ,
            'neg':neg,
            'is_china':is_china,
            'is_covid_19':is_covid_19,
        }
    return new_dic

import config
import tweepy
import time
import datetime
import couchdb

start = time.time()

def get_api(key_index):
    consumer_key = config.app_keys_tokens[key_index]['consumer_key']
    consumer_secret = config.app_keys_tokens[key_index]['consumer_secret']
    access_token = config.app_keys_tokens[key_index]['access_token']
    access_token_secret = config.app_keys_tokens[key_index]['access_token_secret']
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


if __name__ == '__main__':
    # key_index = config.search_appid['melbourne']
    # key_index = config.search_appid['sydney']
    # key_index = config.search_appid['brisbane']
    # key_index = config.search_appid['perth']
    # key_index = config.search_appid['canberra']
    # key_index = config.search_appid['hobart']
    key_index = config.search_appid['adelaide']
    # key_index = config.search_appid['Darwin']
    api = get_api(key_index = key_index)

    server = couchdb.Server("http://%s:%s@172.26.132.58:5984/" % ('admin', 'happy'))
    db_name = 'may_3rd_adelaide'

    try:
        db = server.create(db_name)
    except:
        db = server[db_name]

    #set date
    sincedate = datetime.date.today() - datetime.timedelta(days=7)
    untildate = datetime.date.today()
    # geocode = "%f,%f,%fkm" % (-37.817457, 145.002606, 300)
    # centre of australia
    # #Australia
    # geocode = "%f,%f,%fkm" % (-25.2744, 133.7751, 3000)
    # melbourne
    # centre of melbourne with radius 40 km
    # geocode = "%f,%f,%fkm" % (-37.8142385,144.9622775,40)
    # sydney
    # geocode = "%f,%f,%fkm" % (-33.8559799094,151.20666584,50)
    # brisbane
    # geocode = "%f,%f,%fkm" % (-27.3812533,152.713015,40)
    # perth
    # geocode = "%f,%f,%fkm" % (-32.0391738,115.6813561,40)
    # # canberra
    # geocode = "%f,%f,%fkm" % (-35.2812958,149.124822,40)
    # # hobart
    # geocode = "%f,%f,%fkm" % (-42.8823389,147.3110468,40)
    # # adelaide
    geocode = "%f,%f,%fkm" % (-34.9998826,138.3309816,40)
    # # Darwin
    # geocode = "%f,%f,%fkm" % (-12.4634,130.8456,40)

    #search api method
    tweets = tweepy.Cursor(api.search, q='*',since=sincedate, until=untildate, \
                        geocode = geocode,count=100, tweet_mode='extended',lang="en").items()
    no_geo_count = 0
    no_coordinates = 0
    no_place = 0
    print('---------- collecting Tweets ----------')
    while True:
        try:
            tweet = tweets.next()._json
            if tweet['is_quote_status'] == True and 'quoted_status' in tweet:
                quoted_status = tweet['quoted_status']
            else:
                quoted_status = None
            if tweet['geo'] == None:
                no_geo_count +=1
            else:
                no_geo_count = no_geo_count

            if tweet['coordinates'] == None:
                no_coordinates += 1
            else:
                no_coordinates = no_coordinates

            if tweet['place'] == None:
                no_place += 1
            else:
                no_place = no_place
            # if (tweet['place'] is not None
            #     or (tweet['geo'] is not None
            #         or(tweet['place'] is not None))):

            new_dic = {
                '_id': tweet['id_str'],
                'created_at': tweet['created_at'],
                'full_text': tweet['full_text'],
                'entities': tweet['entities'],
                # 'source': tweet['source'],
                'user': tweet['user'],
                'geo': tweet['geo'],
                'coordinates': tweet['coordinates'],
                'place': tweet['place'],
                'lang': tweet['lang'],
                # 'favorite_count': tweet['favorite_count'],
                'is_quote_status': tweet['is_quote_status'],
                'quoted_status': quoted_status,
            }
            db.save(new_dic)
        except couchdb.http.ResourceConflict:
            pass
        except tweepy.TweepError as e1:
            print(e1.reason)
            print('tweet limit!!!')
            time.sleep(60 * 15)
            continue
        except StopIteration as e2:
            print("Finish search!")
            break
        except Exception as e3:
            print(e3)
            time.sleep(60 * 5)
            continue
    print('time used: ', time.time() - start)
    print(no_geo_count,no_coordinates,no_place)




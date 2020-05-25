import tweepy
import tweepy_tokens
import time
import datetime
import couchdb
import ssl
import scenario_cities

start = time.time()
ssl._create_default_https_context = ssl._create_unverified_context
IP_ADDRESS = '172.26.134.54'
USERNAME = 'admin'
PASSWORD = 'happy'
ORIGINAL_DATABASE_NAME = 'may_18th_canberra'
SCENARIO_DATABASE_NAME = 'scenario_city'


def tweepy_tokens(greater_citys_id):
    consumer_key = tweepy_tokens.all_keys_and_tokens[greater_citys_id]['consumer_key']
    consumer_secret = tweepy_tokens.all_keys_and_tokens[greater_citys_id]['consumer_secret']
    access_token = tweepy_tokens.all_keys_and_tokens[greater_citys_id]['access_token']
    access_token_secret = tweepy_tokens.all_keys_and_tokens[greater_citys_id]['access_token_secret']
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def create_couchdb():
    server = couchdb.Server("http://%s:%s@%s:5984/" %
                            (USERNAME, PASSWORD, IP_ADDRESS))
    try:
        original_database = server.create(ORIGINAL_DATABASE_NAME)
        scenario_database = server.create(SCENARIO_DATABASE_NAME)
    except:
        original_database = server[ORIGINAL_DATABASE_NAME]
        scenario_database = server[SCENARIO_DATABASE_NAME]
    return original_database, scenario_database


def process_tweets(raw_tweets, no_geo_count, no_coordinates, no_place):
    tweet = raw_tweets.next()._json
    if tweet['is_quote_status'] == True and 'quoted_status' in tweet:
        quoted_status = tweet['quoted_status']
    else:
        quoted_status = None

    if tweet['geo'] == None:
        no_geo_count += 1
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

    original_dic = {
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

    return original_dic, no_geo_count, no_coordinates, no_place


if __name__ == '__main__':
    greater_citys_id = tweepy_tokens.greater_citys_id['canberra']
    tweepy_api = tweepy_tokens(greater_citys_id=greater_citys_id)

    original_database, scenario_database = create_couchdb()

    # set date
    start_time = datetime.date.today() - datetime.timedelta(days=7)
    end_time = datetime.date.today()

    # canberra latitude longitude
    geocode = "%f,%f,%fkm" % (-35.2812958, 149.124822, 40)

    # search tweepy_api method
    raw_tweets = tweepy.Cursor(tweepy_api.search, q='*', since=start_time, until=end_time,
                               geocode=geocode, count=100, tweet_mode='extended', lang="en").items()
    no_geo_count = 0
    no_coordinates = 0
    no_place = 0
    print("Twitter harvest begin")
    while True:
        try:
            original_dic, no_geo_count, no_coordinates, no_place = process_tweets(
                raw_tweets, no_geo_count, no_coordinates, no_place)
            original_database.save(original_dic)
            scenario_dic = scenario_cities.execute_canberra(
                original_dic['_id'], original_dic['full_text'])

            if scenario_dic != {}:
                scenario_database.save(scenario_dic)

        except couchdb.http.ResourceConflict:
            pass
        except tweepy.TweepError as TimeLimiteError:
            print(TimeLimiteError.reason)
            print("time out of time range")
            time.sleep(1000)
            continue
        except StopIteration as FinishHarvest:
            print("all done")
            break
        except Exception as AllException:
            print(AllException)
            time.sleep(500)
            continue
    print('time used: ', time.time() - start)
    print(no_geo_count, no_coordinates, no_place)

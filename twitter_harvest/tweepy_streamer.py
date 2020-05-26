import couchdb
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


server = couchdb.Server("http://%s:%s@172.26.132.58:5984/" % ('admin', 'happy'))
db_name = 'may_4rd_australia'

try:
    db = server.create(db_name)
except:
    db = server[db_name]
'''
Twitter authenticater
'''
CONSUMER_KEY : 'CP20F8yCMC85K26XY07w4XElp'
CONSUMER_SECRET : '4t1r4cdlBPGVzkosnZ2gvBqXbet5MbuJIlkuN0JKYufWIdo4yM'
ACCESS_TOKEN : '1121041186305630208-hG4Jv9cfPOufx3vAgPpBUCODlWsHQH'
ACCESS_TOKEN_SECRET : 'OJSXpMxZDzY9XUo2gqoqZcLUyGY1C9duopI4032fywDPb'
#
# CONSUMER_KEY : '2BjmB9QN2UwT7BWGEYJc6mzyQ'
# CONSUMER_SECRET : 'dkP4itLYIM0rqhHef4BiRkEgp8n2STc5CZuddYzjpnRzN3QX0m'
# ACCESS_TOKEN : '1121041186305630208-9pyRCJS3ltExpoKeTqKVrYcdSNnqHg'
# ACCESS_TOKEN_SECRET : 'dWIS8xzpbuB1T77UZSQCHJGBOX2uT7A82UmiwpyuSfrkq'
#
# CONSUMER_KEY: 'W225IVMaLWc3Cio8Y2ZwHmwXT'
# CONSUMER_SECRET : 'D0Gebz3e1xqrSKKCNbQPCwLsjNdQVZxHguLekTU4zCavWysswy'
# ACCESS_TOKEN : '1121041186305630208-vVcpClv576aYx9OJjVaWJkYA89m7eI'
# ACCESS_TOKEN_SECRET : 'ZjUk3ppAaudL4KR3oDQo3K6lDMZRKrnGvj2wYRpzfx1uP'

# CONSUMER_KEY = 'ahKRXTnEizWqy4oHC4uBFxWuu'
# CONSUMER_SECRET = 'xF2Pc3JwGtSij9Ig0UhW5A5o4RVk1kxcbTk6jMGM7W7XfOub8w'
# ACCESS_TOKEN = '1121041186305630208-85TVCtBvNc3RjW9RjmcBdwJn5FKxQm'
# ACCESS_TOKEN_SECRET = 'l3qRsugZsCt1MApDSjtCwMFS19Jms2Y2QiGpUPfzeWVit'

# CONSUMER_KEY: 'IaRuxafuggm6eZvXdmurzA2MV'
# CONSUMER_SECRET : '9DwkZsuQHFHtnFD5JVfttZ6uNkqsm99yNxvpmPMgSlPxAtqjJ9'
# ACCESS_TOKEN : '1121041186305630208-UJOUSKINRytWJY9OiCF9ANeqNacdMY'
# ACCESS_TOKEN_SECRET : 'kQjU0Vc4x7oPnSeuOM4Jrs5waE21dtYOKHN9Wi0hcikxB'
#
# CONSUMER_KEY : 'W2pCfanNy4x8YiEEuC1pHbPU8'
# CONSUMER_SECRET : '3XfspXNraGydG3xKYfxZ6wLVaJsCZqYeSx0cOUFSv2ABNHNi8a'
# ACCESS_TOKEN : '1121041186305630208-iHTAQCyxr0QcCPjEH8gpNYTZyomfjQ'
# ACCESS_TOKEN_SECRET: 'nsNp6LLbb1SacGUbKlUPBFBEiV937Lct9LxHIgB5MYKnL'
#
# CONSUMER_KEY : 'kpC53YdFfY1Q4vXIEhLKM4lhT'
# CONSUMER_SECRET: '3qYR9E9oucDhQSwilPQxUVnmdr1tJwAOi0iMyKCYWy63coEQLZ'
# ACCESS_TOKEN : '1121041186305630208-bFfc3Y4x0ueoHCyCvVUZxeMWRmhloR'
# ACCESS_TOKEN_SECRET : 'O460teRRz2MJxQRto7ipMz3MyKA2fwZWwW4bMnMVKzKGZ'
#
# CONSUMER_KEY: 'hVmTeuwuAy44Ufr6q6SlIlSST'
# CONSUMER_SECRET : 'BsYDcvgtmbhdGDv57oI5Q3DwSsBEuPtjaIDjALelQsmnQaeQf1'
# ACCESS_TOKEN : '1121041186305630208-9xcHlMmIVGemqa6jNPDYfrXOv05V8l'
# ACCESS_TOKEN_SECRET: 'NULMzSH41CSFTzJSv8rUu0fPf2VmiqqKX80SqF06LkqT0'




auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class TwitterListener(StreamListener):
    '''
    This is a basic listener class that just prints received tweets to stdout.
    '''

    def on_status(self, status):
        tweets = status._json
        Dict = {}
        print(tweets, '\n')
        try:
            Dict = {
                'ID': tweets['id_str'],
                'Create_Time': tweets['created_at'],
                'Text': tweets['text'],
                'Entities': tweets['entities'],
                'Source': tweets['source'],
                'User': tweets['user'],
                'Geo': tweets['geo'],
                'Coordinates': tweets['coordinates'],
                'Place': tweets['place'],
                'Lang': tweets['lang']}
            db.save(Dict)
        except couchdb.http.ResourceConflict:
            pass

    def on_error(self, status):
        if status == 420:
            # return false on_data method in case rate limit occurs
            return False
        print(status)


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['virus', 'Covid-19', 'coronavirus']
    stream = Stream(auth, TwitterListener())
    #Australia
    stream.filter(locations=[112.9211, -54.6403, 159.2787, -9.2288])
    # #melbourne
    # # stream.filter(locations=[143.3525, -38.3136, 145.3657, -36.9475])
    # #sydney
    # stream.filter(locations=[150.0461, -34.9688, 152.8193, -32.6821])
    # # #brisbane
    # stream.filter(locations=[152.2445, -28.5698, 154.02517, -26.6241])
    # # #adelaide
    # stream.filter(locations=[137.58321, -35.9285, 139.7231, -33.8532])
    # #canberra
    # stream.filter(locations=[148.0834, -36.3206, 150.1324, -34.2709])
    # #darwin
    # stream.filter(locations=[129.9395, -13.0652, 131.2357, -11.9643])
    # #perth
    # stream.filter(locations=[114.9783, -30.6435, 116.937, -32.2542])
    # #hobart
    # stream.filter(locations=[146.8325, -43.3536, 148.0231, -41.9345])




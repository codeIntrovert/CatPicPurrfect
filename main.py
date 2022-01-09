import tweepy
import time
from key import *
def tweeter():
    #access verfication
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    search = '#100daysofcode'
    nrTweets = 500
    print("List loaded starting retwating")
    for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
        try: 
            tweet.retweet()
            print("retwat will check again in 60 sec ")
            time.sleep(60)
        except:
            print("ERROR:: retwat will restart in 60 secs")
            time.sleep(60)
            tweeter()
tweeter()
import tweepy
import time
from key import *

initial_twittes = 0
def tweeter():
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    search = '#codenewbie'
    nrTweets = 500
    print("List loaded starting retwating")
    for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
        try: 
            tweet.retweet()
            print("retwitter will check again in 90 sec ")
            time.sleep(90)
            final_twittes = initial_twittes+1
            if final_twittes%100 == 0:
                tweet.update_status(f"WE HAVE OFFICIALLY RETWEETED {final_twittes} TWEETS, congrats everyone!{HASTAGS}")
        except:
            print("ERROR:: retwitter will restart in 60 secs")
            time.sleep(60)
            tweeter()
tweeter()

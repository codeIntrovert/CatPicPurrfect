import tweepy
import time
from key import *

'''variable table'''
REMAP_TIME = 90
ERROR_TIME = 5
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT = int(0)
def tweeter():
    search = '#100DaysOfCode'
    nrTweets = 50

    for tweet in tweepy.Cursor(API.search_tweets, search).items(nrTweets):

        try: 
            tweet.retweet()
            print(f"retwitter will check again in {REMAP_TIME} sec {count}")
            time.sleep(REMAP_TIME)
            COUNT +=1
        except Exception as e:
            print(f"ERROR:: retwitter will restart in {ERROR_TIME} secs {e}")
            time.sleep(ERROR_TIME)
            tweeter()


        if COUNT%100==0:
            final_twittes = int(COUNT+2000)
            tweet.update_status(f"WE HAVE OFFICIALLY RETWEETED {final_twittes} TWEETS! {HASTAGS}")
            print("announced")
tweeter()
#code finalized, updated on 11/jan/2022
#@HasanBOT_PY, signed in with google public id, MYNAMEIS
#continued minor bug fixes

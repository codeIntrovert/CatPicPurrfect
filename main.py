import tweepy
import time
from key import *

'''variable table'''
REMAP_TIME = 88
ERROR_TIME = 5
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT = int(1)
POST_ERROR = int(1)
CALIBRATE = 7500

def tweeter():
    global COUNT
    global POST_ERROR
    search = '#100DaysOfCode'
    nrTweets = 30

    for tweet in tweepy.Cursor(API.search_tweets, search).items(nrTweets):
        if COUNT%200==0:
            final_twittes = int(COUNT+CALIBRATE)
            API.update_status(f"WE HAVE OFFICIALLY RETWEETED {final_twittes} TWEETS! \n {HASTAGS}")
            print("announced")

        try: 
            tweet.retweet()
            COUNT +=1
            print(f"next post in {REMAP_TIME} sec; POSTS = {COUNT} ; ERROR = {POST_ERROR}")
            time.sleep(REMAP_TIME)
            
        except Exception as e:
            POST_ERROR +=1
            print(f"ERROR: restart in {ERROR_TIME} secs; POST = {COUNT} ; ERROR = {POST_ERROR} {e}")
            time.sleep(ERROR_TIME)
            tweeter()


 
tweeter()
#code finalized, updated on 11/jan/2022
#@HasanBOT_PY, signed in with google public id, MYNAMEIS
#continued minor bug fixes

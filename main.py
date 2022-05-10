import tweepy
from time import sleep
from json import loads
from requests import get
from key import *


REMAP_TIME = int(125)
ERROR_TIME = int(5)
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT = int(0)
POST_ERROR = int(0)
FAKE = int(0)
def qoutesAPI():
    try:
        fetchapi = "https://programming-quotes-api.herokuapp.com/Quotes/random"
        response = get(fetchapi)
        thoughtJSON = loads(response.text)

        quote = thoughtJSON['en']
        author = thoughtJSON['author']

        statement = (f"{quote} - {author} #100daysOfCode #python #coding #Javascript")
        API.update_status(statement)
    except Exception as t:
        print(f"{t}\nproblem with fetching thought api")

def tweeter():
    global COUNT
    global POST_ERROR
    global FAKE
    tag = "#catsoftwitter"
    nrTweets = int(50)
    
    for status in tweepy.Cursor(API.search_tweets, tag,tweet_mode="extended",lang="en").items(nrTweets):
        if "whatsapp" in status.full_text.lower() : # dm
            print("FAKE! DM")
            FAKE+=1
        elif "buy" in status.full_text.lower(): #buy
            FAKE+=1
        else:
            try:
                status.favorite()
                status.retweet()
                COUNT +=1
                print("POSTS = %d ; ERROR = %d ; FAKE = %d "%(COUNT,POST_ERROR,FAKE))
                sleep(REMAP_TIME)
                if COUNT%200 == 0:
                    qoutesAPI()

            except Exception as e:
                POST_ERROR +=1
                print("ERROR:POSTS = %d ; ERROR = %d ; FAKE = %d %s"%(COUNT,POST_ERROR,FAKE,e))
                sleep(ERROR_TIME)
                tweeter()



tweeter()
#code finalized, updated on 12/march/2022
#@HasanIntrovert, signed in with google public id
#continued minor bug fixes

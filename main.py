import tweepy
import time
import json 
import requests
from key import *


REMAP_TIME = 10
ERROR_TIME = 5
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT = int(0)
POST_ERROR = int(0)
FAKE = int(0)
def qoutesAPI():
    try:
        fetchapi = "https://programming-quotes-api.herokuapp.com/Quotes/random"
        response = requests.get(fetchapi)
        thoughtJSON = json.loads(response.text)

        quote = thoughtJSON['en']
        author = thoughtJSON['author']

        statement = (f"{quote} - {author} #100daysOfCode #python")
        print(statement)
        API.update_status(statement)
    except Exception as t:
        print(f"{t}\n\nproblem with fetching thought api")

def tweeter():
    global fetchapi
    global COUNT
    global POST_ERROR
    global FAKE
    tag = ["#100DaysOfCode"]
    nrTweets = 10000
    
    for status in tweepy.Cursor(API.search_tweets, tag,tweet_mode="extended").items(nrTweets):
        if "dm" in status.full_text.lower() : # dm
            print("FAKE! DM \n")
            FAKE+=1
        elif "essay" in status.full_text.lower(): # /
            print("FAKE! Essay \n")
            FAKE+=1
        elif "courses" in status.full_text.lower(): #courses
            print("FAKE! COURSE\n")
            FAKE+=1
        elif "free" in status.full_text.lower(): #free
            print("FAKE! FREE\n")
            FAKE+=1
        elif "know more" in status.full_text.lower(): #free
            print("FAKE! KNOW MORE\n")
            FAKE+=1

        else:
            try: 
                status.retweet()
                #status.favorite()
                COUNT +=1
                print(f"next post in {REMAP_TIME} sec; POSTS = {COUNT}; ERROR = {POST_ERROR}; FAKE = {FAKE} ")
                time.sleep(REMAP_TIME)

            except Exception as e:
                POST_ERROR +=1
                print(f"ERROR: restart in {ERROR_TIME} secs; POST = {COUNT}; ERROR = {POST_ERROR}; FAKE = {FAKE} {e}")
                time.sleep(ERROR_TIME)
                tweeter()
            finally:
                if COUNT%150 == 0:
                    qoutesAPI()

tweeter()
#code finalized, updated on 12/march/2022
#@HasanIntrovert, signed in with google public id
#continued minor bug fixes

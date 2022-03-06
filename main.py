import tweepy
import time
from key import *


REMAP_TIME = 120
ERROR_TIME = 5
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT = int(0)
POST_ERROR = int(0)
fetchapi = "https://programming-quotes-api.herokuapp.com/Quotes/random"


def qoutesAPI():
    try:
        fetchapi = "https://programming-quotes-api.herokuapp.com/Quotes/random"
        response = requests.get(fetchapi)
        thoughtJSON = json.loads(response.text)

        quote = thoughtJSON['en']
        author = thoughtJSON['author']

        statement = (f"{quote} \n by {author} ")
        print(statement)
        API.update_status(statement)
    except:
        print("problem with fetching thought api")

def tweeter():
    global fetchapi
    global COUNT
    global POST_ERROR
    tag = ["#100DaysOfCode"]
    nrTweets = 30
    
    for tweets in tweepy.Cursor(API.search_tweets, tag).items(nrTweets):
        try: 
            tweets.retweet()
            #tweets.favorite()
            COUNT +=1
            print(f"next post in {REMAP_TIME} sec; POSTS = {COUNT} ; ERROR = {POST_ERROR}")
            time.sleep(REMAP_TIME)

        except Exception as e:
            POST_ERROR +=1
            print(f"ERROR: restart in {ERROR_TIME} secs; POST = {COUNT} ; ERROR = {POST_ERROR} {e}")
            time.sleep(ERROR_TIME)
            tweeter()
        finally:
            if COUNT%1 == 0:
                qoutesAPI()

tweeter()
#code finalized, updated on 12/march/2022
#@HasanIntrovert, signed in with google public id
#continued minor bug fixes

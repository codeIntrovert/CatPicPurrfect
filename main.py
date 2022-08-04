import tweepy
from time import sleep
from json import loads
from requests import get
from key import *


REMAP_TIME , ERROR_TIME = int(125), int(5)

auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
API = tweepy.API(auth, wait_on_rate_limit = True)
COUNT,POST_ERROR,FAKE = int(0),int(0),int(0)


def qoutesAPI():
    try:
        fetchapi = "https://api.quotable.io/random?tags=famous-quotes"
        response = get(fetchapi)
        thoughtJSON = loads(response.text)

        quote = thoughtJSON['content']
        author = thoughtJSON['author']

        statement = (f"Quote of the day \U0001F496 {quote} - {author} #quotes #quoteoftheday")
        print(statement)
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

        if "whatsapp" in status.full_text.lower() : # blocks whatsapp
            FAKE+=1
        elif "buy" in status.full_text.lower(): #blocks buy
            FAKE+=1
        elif "know more" in status.full_text.lower(): #blocks knowmore
            FAKE+=1
        elif "#crypto" in status.full_text.lower(): #blocks $
            FAKE+=1
        elif "#nft" in status.full_text.lower(): #blocks nft
            FAKE+=1
            
        else:
            try:
                status.retweet()
                status.favorite()
                COUNT +=1
                print("Latest TIME = %d ; POSTS = %d ; ERROR = %d ; FAKE = %d "%(REMAP_TIME,COUNT,POST_ERROR,FAKE))
                sleep(REMAP_TIME)
                if COUNT%200 == 0:
                    qoutesAPI() #call quotesapi here if wanted

            except Exception as e:
                POST_ERROR +=1
                print("ERROR:POSTS = %d ; ERROR = %d ; FAKE = %d %s"%(COUNT,POST_ERROR,FAKE,e))
                sleep(ERROR_TIME)
                tweeter()



tweeter()
#code finalized, updated on 12/march/2022
#@HasanIntrovert, signed in with google public id
#continued minor bug fixes

tweet = ["a","c","b","d"]

for tweet in tweet:
    if tweet == "c":
        print("sus")
    else:
        print("fine")

for tweets in tweepy.Cursor(API.search_tweets, tag).items(nrTweets):
    if tweets
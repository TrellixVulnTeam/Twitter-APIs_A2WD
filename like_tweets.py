import tweepy
import time
from tweepy import OAuthHandler

import twitter_credentials


auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.me()
search = 'Javascript'
numberOfTweets = 500


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print('Tweet liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

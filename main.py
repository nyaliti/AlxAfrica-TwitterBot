import tweepy
import os
from dotenv import load_dotenv
import time

load_dotenv()

auth = tweepy.OAuthHandler(
    os.getenv('CONSUMER_KEY'),
    os.getenv('CONSUMER_SECRET')
)
auth.set_access_token(
    os.getenv('ACCESS_TOKEN'),
    os.getenv('ACCESS_TOKEN_SECRET')
)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def retweet_alx_africa(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        api.retweet(tweet_id)
        print(f"Retweeted tweet: {tweet_id}")
    except tweepy.TweepError as e:
        print(f"Error retweeting tweet: {e}")

latest_tweet_id = None

while True:
    tweets = api.search(q="@alx_africa", count=1)
    if tweets:
        latest_tweet_id = tweets[0].id
        retweet_alx_africa(latest_tweet_id)
    time.sleep(3600)  # Retweet every hour

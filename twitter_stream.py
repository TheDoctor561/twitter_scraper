from tkinter.tix import TCL_WINDOW_EVENTS
import tweepy
import configparser
import pandas as pd
from tw_sentiment import sentimenter


# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class Linstener(tweepy.Stream):

    tweets = []
    limit = 100
 
    def on_status(self, status):
        self.tweets.append(status)
        print(status.user.screen_name + ": " + status.text)
        print(sentimenter(status.text))
        if len(self.tweets) == self.limit: 
            self.disconnect() 

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

# stream by keywords
keywords = ['bitcoin']

stream_tweet.filter(track=keywords)


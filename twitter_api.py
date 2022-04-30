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

#authentification
auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)



# print(public_tweets[0].user.screen_name)

"""
public_tweets = api.home_timeline()

columns = ['Time', 'User', 'Tweet']
data = [] 

for tweet in public_tweets: 
   data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns = columns) 

s = df['Tweet']

 for i in s: 
   print(i)
   sentimenter(i)
 """

columns = ['Time', 'User', 'Tweet']
data = []

userID = "elonmusk"

limit = 200
tweets = tweepy.Cursor(api.user_timeline, screen_name = userID, count = 200, tweet_mode = 'extended').items(limit)

# tweets = api.user_timeline(screen_name = userID, count = 200, tweet_mode = 'extended')

i = 1
neg = 0 
neu = 0 
pos = 0

for tweet in tweets: 
   print(i)
   print(tweet.full_text)
   s = sentimenter(tweet.full_text)
   neg += s[0] # negative
   neu += s[1] # neutral 
   pos += s[2] # positive
   i += 1 

print(neg/i)
print(neu/i)
print(pos/i)
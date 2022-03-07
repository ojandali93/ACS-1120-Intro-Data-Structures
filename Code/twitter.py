import os
import dotenv
dotenv.load_dotenv("../.env")
from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

session = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

url = 'https://api.twitter.com/2/tweets'
status = 'If you are reading this on Twitter, the API request worked!'

def tweet(status):
  response = session.post(url, json={ 'text': status })
  return response.text
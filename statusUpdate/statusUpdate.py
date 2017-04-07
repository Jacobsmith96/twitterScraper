import tweepy
from tweepy import OAuthHandler
import pandas
import sys
import json
import argparse



#Function that runs when a Twitter username is provided
def main(text, access_token, access_token_secret, consumer_key, consumer_secret):
    #Finish setting up authentication and creating the Tweepy API object
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #Post a tweet with the user inputted text
    api.update_status(status = text)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("conf_filename", help="the file containing your Twitter API info")
    parser.add_argument("text", help="the text you wish to post")
    args = parser.parse_args()
     
    conf = json.load(open(args.conf_filename))
    access_token = conf["token"]
    access_token_secret = conf["token_secret"]
    consumer_key = conf["consumer_key"]
    consumer_secret = conf["consumer_secret"]

    main(args.text, access_token, access_token_secret, consumer_key, consumer_secret)

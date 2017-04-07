import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas
import sys
import json
import argparse

#Define a function that clears a file
def deleteContent(fName):
    with open(fName, "w"):
        pass

#Define the tweepy StreamListener class
class StdOutListener(StreamListener):
    def on_data(self, data):
        #Write to the output file whenever a tweet is received
        out.write(data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("conf_filename", help="the file containing your Twitter API info")
    parser.add_argument("filter_words", nargs="*", help="the words you wish to filter on")
    args = parser.parse_args()
    
    conf = json.load(open(args.conf_filename))
    access_token = conf["token"]
    access_token_secret = conf["token_secret"]
    consumer_key = conf["consumer_key"]
    consumer_secret = conf["consumer_secret"]
     
    screen_name = args.screen_name
    #Create the StreamListener
    l = StdOutListener()
    #Setup authentication
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #Create a stream using the StreamListener object
    stream = Stream(auth, l)
    
    deleteContent("twitter_data.txt")
    #Open the output file for writing to
    out = open("twitter_data.txt", "w")
    
    stream.filter(track=args.filter_words)


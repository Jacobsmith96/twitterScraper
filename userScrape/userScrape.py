import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas
import sys
import json
consumer_key = "VzEgtLw9mhYA1gecaOLTS7US6"
consumer_secret = "AwMCrGIpjNfC1DBPjgIuONH57v2ueJLK1ovIOIwLjyVwsEFhJK"
access_token = "844933048911237121-oJZ9iTf9J4Sse4S7XmfPudc5WSdgRQr"
access_token_secret = "TqEt9xmbPnPXZxYvorEJOT2GStBL4Hzw0msVCyeMuBx9G"

def main(screen_name):
     auth = OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)
     api = tweepy.API(auth)
     
     out = open("twitter_data.txt", "w") 
     
     new_tweets = api.user_timeline(screen_name = screen_name, count=200)

     #while len(new_tweets) > 0:       
     new_tweets = api.user_timeline(screen_name = screen_name, count=200)
     for x in new_tweets:
        print(x._json['id'])
        out.write(json.dumps(x._json))
        out.write("\n")

if __name__ == '__main__':
    if len(sys.argv) <2 or len(sys.argv)>2:
        print("Invalid number of arguments (should be of the format python userScrape.py <screen_name>)")
    else:
        main(sys.argv[1]) 
        

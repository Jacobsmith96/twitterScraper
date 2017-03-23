import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas
import sys

consumer_key = "VzEgtLw9mhYA1gecaOLTS7US6"
consumer_secret = "AwMCrGIpjNfC1DBPjgIuONH57v2ueJLK1ovIOIwLjyVwsEFhJK"
access_token = "844933048911237121-oJZ9iTf9J4Sse4S7XmfPudc5WSdgRQr"
access_token_secret = "TqEt9xmbPnPXZxYvorEJOT2GStBL4Hzw0msVCyeMuBx9G"

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        if len(sys.argv)<=1:
            print("Input a series of words to be filtered")
        else:
            stream.filter(track=sys.argv[1:])


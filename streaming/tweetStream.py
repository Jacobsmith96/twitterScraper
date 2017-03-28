import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas
import sys

#Setup authentication
consumer_key = "VzEgtLw9mhYA1gecaOLTS7US6"
consumer_secret = "AwMCrGIpjNfC1DBPjgIuONH57v2ueJLK1ovIOIwLjyVwsEFhJK"
access_token = "844933048911237121-oJZ9iTf9J4Sse4S7XmfPudc5WSdgRQr"
access_token_secret = "TqEt9xmbPnPXZxYvorEJOT2GStBL4Hzw0msVCyeMuBx9G"

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
    
    #Make sure the user inputs a series of words for filtering
    if len(sys.argv)<=1:
        print("Input a series of words to be filtered")
    #Start the stream
    else:
        stream.filter(track=sys.argv[1:])


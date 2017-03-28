import tweepy
from tweepy import OAuthHandler
import pandas
import sys
import json

#Setup twitter authentication 
consumer_key = "VzEgtLw9mhYA1gecaOLTS7US6"
consumer_secret = "AwMCrGIpjNfC1DBPjgIuONH57v2ueJLK1ovIOIwLjyVwsEFhJK"
access_token = "844933048911237121-oJZ9iTf9J4Sse4S7XmfPudc5WSdgRQr"
access_token_secret = "TqEt9xmbPnPXZxYvorEJOT2GStBL4Hzw0msVCyeMuBx9G"

#Function that runs when a Twitter username is provided
def main(text):
    #Finish setting up authentication and creating the Tweepy API object
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #Post a tweet with the user inputted text
    api.update_status(status = text)

if __name__ == '__main__':
    #Make sure the user inputs only one input after the file name 
    if len(sys.argv) <2 or len(sys.argv)>2:
        print("Invalid number of arguments (should be of the format python userScrape.py <text>)")
    else:
        #Run the main function
        main(sys.argv[1]) 
        

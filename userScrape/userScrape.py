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
def main(screen_name):
     #Finish setting up authentication and creating the Tweepy API object
     auth = OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)
     api = tweepy.API(auth)
     
     #Open the file to write the json blobs of Twitter Statuses to
     out = open("twitter_data.txt", "w") 

     #Create variables for tracking total tweets processed
     totalLen = 0

     #Get the first batch of tweets from the user
     new_tweets = api.user_timeline(screen_name = screen_name, count=200)
     
     #Iterate over the first batch of tweets, writing non-retweets to the output file
     for x in new_tweets:
         if 'retweeted_status' not in x._json:
                out.write(json.dumps(x._json))
                out.write("\n")
       
     #Get the id of the oldest tweet, used to ensure no duplicates in future API calls
     oldest = new_tweets[-1].id
   
     #Increase the total length counter
     totalLen = totalLen + len(new_tweets)

     #Continue to loop over tweets while there a still new ones being retrieved
     #Currently can only loop 15 times, need to add a timer to get around the API restrictions
     while len(new_tweets) > 0: 
         print "getting tweets before %s" %(oldest)

         #Get a new batch of tweets using the previous oldest id ad max_id
         new_tweets = api.user_timeline(screen_name = screen_name, count = 200,  max_id=oldest-1)
         #Increment the total length variable
         totalLen = totalLen + len(new_tweets)
         
         #Set the new oldest id
         oldest = new_tweets[-1].id
         
         #Handle output of Tweets to the output file
         for x in new_tweets:
             if 'retweeted_status' not in x._json:
                out.write(json.dumps(x._json))
                out.write("\n")
        
         print "...%s tweets downloaded so far" % (totalLen)
if __name__ == '__main__':
    #Make sure the user inputs only one input after the file name 
    if len(sys.argv) <2 or len(sys.argv)>2:
        print("Invalid number of arguments (should be of the format python userScrape.py <screen_name>)")
    else:
        #Run the main function
        main(sys.argv[1]) 
        

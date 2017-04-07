import tweepy
from tweepy import OAuthHandler
import pandas
import sys
import json
import json
import argparse

#Function that runs when a Twitter username is provided
def main(screen_name, access_token, access_token_secret, consumer_key, consumer_secret):
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
     
     parser = argparse.ArgumentParser()
     parser.add_argument("conf_filename", help="the file containing your Twitter API info")
     parser.add_argument("screen_name", help="the screen name of the user you wish to scrape")
     args = parser.parse_args()
     
     conf = json.load(open(args.conf_filename))
     access_token = conf["token"]
     access_token_secret = conf["token_secret"]
     consumer_key = conf["consumer_key"]
     consumer_secret = conf["consumer_secret"]
     
     screen_name = args.screen_name
     
     main(screen_name, access_token, access_token_secret, consumer_key, consumer_secret)   

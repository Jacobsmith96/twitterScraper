import json
import pandas as pd
import matplotlib.pyplot as plt

#Open the files for sentiment analysis
positives = open('positive.txt', 'r').read().split('\n')
negatives = open('negative.txt', 'r').read().split('\n')

#Define a function to count the number of words in each tweet
def countWords(x):
    if x is not None:
        split = x.split(' ')
        words = []
        for a in split:
            if a.isalpha():
                words.append(a)
        return len(words)
    else:
        return 0

#Define a function that cleans the tweet text
def cleanString(x):
    if x is not None:
        x = x.lower()
        x = x.replace('\n', ' ')
        for ch in ['.', ',', '!', '?', ':', ';', '"', '\'', '-', '~', '|']:
            if ch in x:
                x = x.replace(ch, '')
        return x
    else:
        return

#Define a function that counts the number of positive words in each tweet
def countPositive(x):
    count = 0
    if x is not None:
        x = x.split(' ')
        for w in x:
            if w in positives:
                count = count + 1
    return count

#Define a function that counts the number of negative words in each tweet
def countNegative(x):
    count = 0
    if x is not None:
        x = x.split(' ')
        for w in x:
            if w in negatives:
                count = count + 1
    return count    

#Defne the main function for analytics
def main():
    print "Reading Tweets\n"

    #Define the path to the data file
    tweets_data_path = 'twitter_data.txt'

    #Create an empty list for adding tweets to
    tweets_data = []
    #Open the data file for reading
    tweets_file = open(tweets_data_path, "r")
    
    #Iterate over the lines in the data file, adding each line to the list
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    #Print the number of tweets loaded
    print("Number of Tweets: " + str(len(tweets_data)))
    print "Structuring Tweets\n"

    #Create an empty pandas DataFrame for tweet formatting
    tweets = pd.DataFrame()

    #Create a series of new columns using mappings of the tweets
    tweets['text'] = map(lambda tweet: tweet.get('text',None), tweets_data)
    tweets['cleanText'] = tweets['text'].map(cleanString)
    tweets['numWords'] = tweets['cleanText'].map(countWords)
    tweets['numPos'] = tweets['cleanText'].map(countPositive)
    tweets['numNeg'] = tweets['cleanText'].map(countNegative)
    tweets['sent'] = tweets['numPos']-tweets['numNeg']
    
    #Output the sentiment results from analysis
    print("Mean positive sentiment words: " + str((tweets['numPos']).mean()))
    print("Mean negtave sentiment words: " + str((tweets['numNeg']).mean()))
    print("Mean combined sentiment: " + str((tweets['sent']).mean()))

if __name__ == '__main__':
    main()

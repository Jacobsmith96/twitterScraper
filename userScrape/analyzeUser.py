import json
import pandas as pd
import matplotlib.pyplot as plt

#Open the files of positive and negative words
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

#Define a function that removes unnecessary characters from tweets
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

#The main function
def main():
    print "Reading Tweets\n"

    #Define the path of the output file
    tweets_data_path = 'twitter_data.txt'
    
    #Create a list for converting the json strings into a datatable format
    tweets_data = []
    #Open the data file for reading
    tweets_file = open(tweets_data_path, "r")
    #Iterate over the lines in the tweet file
    for line in tweets_file:
        try:
            #Append these json blobs into the tweets_data list
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    #Output the number of tweets in the list
    print("Number of Tweets: " + str(len(tweets_data)))
    print "Structuring Tweets\n"

    #Create an empty pandas DataFrame for splitting up the tweets
    tweets = pd.DataFrame()
    

    #Perform a series of mappings that create new columns in the pandas DataFrame
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['cleanText'] = tweets['text'].map(cleanString)
    tweets['numWords'] = tweets['cleanText'].map(countWords)
    tweets['numPos'] = tweets['cleanText'].map(countPositive)
    tweets['numNeg'] = tweets['cleanText'].map(countNegative)
    tweets['sent'] = tweets['numPos']-tweets['numNeg']

    #Output findings
    print("Mean positive sentiment words: " + str((tweets['numPos']).mean()))
    print("Mean negtave sentiment words: " + str((tweets['numNeg']).mean()))
    print("Mean combined sentiment: " + str((tweets['sent']).mean()))
    

if __name__ == '__main__':
    main()

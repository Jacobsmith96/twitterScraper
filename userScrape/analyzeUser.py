import json
import pandas as pd
import matplotlib.pyplot as plt
#Define a function to count the number of words in each tweet
positives = open('positive.txt', 'r').read().split('\n')
negatives = open('negative.txt', 'r').read().split('\n')
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

def main():
    print "Reading Tweets\n"

    tweets_data_path = 'twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    print("Number of Tweets: " + str(len(tweets_data)))
    print "Structuring Tweets\n"
    tweets = pd.DataFrame()
    

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['cleanText'] = tweets['text'].map(cleanString)
    tweets['numWords'] = tweets['cleanText'].map(countWords)
    tweets['numPos'] = tweets['cleanText'].map(countPositive)
    tweets['numNeg'] = tweets['cleanText'].map(countNegative)
    tweets['sent'] = tweets['numPos']-tweets['numNeg']
    print("Mean positive sentiment words: " + str((tweets['numPos']).mean()))
    print("Mean negtave sentiment words: " + str((tweets['numNeg']).mean()))
    print("Mean combined sentiment: " + str((tweets['sent']).mean()))
    for tweet in tweets['cleanText']:
        print tweet

if __name__ == '__main__':
    main()

# twitterScraper
Includes functionality for:

  -Ingesting streamed tweets using user inputted filter words

  -Ingesting a specific users tweets

  -Sentiment analysis for both

  -Posting a tweet
## Streaming
1. First, run the tweetStream.py python file with a list of user inputted filter words as arguments. This will monitor all the tweets being tweeted for the given filter words, outputting them to twitter_data.txt as json blobs.
2. To perform the sentiment analysis, next run the analyzeStream.py python file. This will output the number of tweets ingested, as well as mean positive, negative, and combined sentiment.

## User Scraping
1. To scrape a users tweets, first run the userScrape.py python file with a Twitter username as the first and only argument. This will repeatedly call the API, getting more and more old tweets. Currently breaks after 15 calls, per twitter API specs. This can be avoided by adding a delay between calls using the time library. Outputs json blobs to twitter_data.txt.
2. Run the python file analyzeUser to perform sentiment analysis on the ingested tweets.

## Status Update
1. To post a tweet, simply run statusUpdate.py with a command line argument string of the tweet text you want to post.

import tweepy
from tweepy import OAuthHandler

consumer_key = "VzEgtLw9mhYA1gecaOLTS7US6"
consumer_secret = "AwMCrGIpjNfC1DBPjgIuONH57v2ueJLK1ovIOIwLjyVwsEFhJK"
access_token = "844933048911237121-oJZ9iTf9J4Sse4S7XmfPudc5WSdgRQr"
access_secret = "TqEt9xmbPnPXZxYvorEJOT2GStBL4Hzw0msVCyeMuBx9G"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
        print(status.text)

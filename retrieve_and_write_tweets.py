import sys

import tweepy

api_key = "api_key"
api_secret = "api_secret"
access_key = "access_key"
access_secret = "access_secret"

def get_tweets(username, count):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	#Tweepy is a little easier then twitter api docs :)
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	tweet_count = count

	#get tweets & write to file as you go (memory consideration)
	outfile = username + "_tweets.txt"
	file = open(outfile, "w+")

	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(tweet_count):
		file.write(tweet.text.encode("utf-8") + "\n")

	file.close()


user = input("What user do you want tweets for?: ")
count = input("How many tweets do you want?: ")

get_tweets(user,count)
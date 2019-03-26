import tweepy

consumer_key = "api_key"
consumer_secret = "api_secret"
access_key = "access_key"
access_secret = "access_secret"

def get_tweets(username, count):

	#http://tweepy.readthedocs.org/en/v3.7.0/getting_started.html#api
	#Tweepy is a little easier then twitter api docs :)
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#get tweets & write to file as you go (memory consideration)
	#outfile = username + "_tweets.txt"
	#file = open(outfile, "w+")

	for tweet in tweepy.Cursor(api.home_timeline, id=username).items(count):
		print(tweet.text)

	#file.close()


user = input("What user do you want tweets for?: ")
count = input("How many tweets do you want?: ")

get_tweets(user,count)
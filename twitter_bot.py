import tweepy
import time

auth = tweepy.OAuth1UserHandler(
   '7POHEsJv6mrw668KcNTcyKmPs', '17a9opR34yX4YeJ2wnVSXkpyxev1liT8jmbPG4weMLCxDIamXn', '1597932774253809665-vX7OmjMr07p1OrMnpJgCDv3M7bP33G', 'cEnXNZjnZ1KErGsTOCYgWqjv7qo0lAzzFrrKftpkCY1zJ'
)

api = tweepy.API(auth, wait_on_rate_limit=True)


for follower in tweepy.Cursor(api.get_followers).items():
   api.create_friendship(screen_name=follower.screen_name)


search_string = "Day #100DaysOfCode"
tweets_limit = 100

for tweet in tweepy.Cursor(api.search_tweets , search_string).items(tweets_limit):
   try:
      tweet.favorite()
      tweet.retweet()
      print("tweet liked")
      time.sleep(10)
   except tweepy.TweepyException as e:
      print(e.reason)
   except StopIteration:
      break 
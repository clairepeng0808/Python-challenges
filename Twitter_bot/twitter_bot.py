import tweepy
import time
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# me = api.me()
# user = api.get_user('twitter')

# commonly used:
# for tweet in public_tweets:
#     print(tweet.text)

# print(user)
# print(me.screen_name)
# print(user.screen_name)
# print(user.followers_count)


def limit_handler(cursor):

    try:
        while True:
            yield cursor.next()

    except StopIteration:
        return

    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()
    print('I follow this account!')

# Love Python bot
search_string = 'Python'
numbers_of_tweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numbers_of_tweets):

    try:
        tweet.favorite()
        print('I like the tweet!')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

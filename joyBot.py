import tweepy
#import config
import logging
CONSUMER_KEY = "rR1a8MuCyAsPhnxVLANrvbXlP"
CONSUMER_SECRET = "gTAZ7bvfFaMvQGf9z1WeJbU8VaJAziCDIgCGJwA5GGqvtVJPXs"
ACCESS_TOKEN = "576724631-vThh3Cbb9S4qGSWcBDRE0sd1hWycdsqE2u2hk7In"
ACCESS_TOKEN_SECRET = "XJL8oCuvX1nS4YnVWqyLUU7nFRDu8oB1k1NhW1JeYBtk0"

#Setup authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def follow_followers(api):
	#Create logger object
	loggin.basicConfig(level=logging.INFO)
	logger = logging.getLogger()
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)



# Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True,
#     wait_on_rate_limit_notify=True)


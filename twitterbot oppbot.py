import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("key", "key secret")
auth.set_access_token("token", "token secret")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")

queries = ["#healthyconversations"]
tweets_per_query  = 50

new_tweets = 0
for query in queries:
    print ("Starting new query: " + query)
    for tweet in tweepy.Cursor(api.search, q=query, tweet_mode="extended").items(tweets_per_query ):

        user = tweet.user.screen_name
        id = tweet.id
        url = 'https://twitter.com/' + user +  '/status/' + str(id)
        print (url)

        try:
            text = tweet.retweeted_status.full_text.lower()
        except:
            text = tweet.full_text.lower()
        if "mental health" in text or "happiness" in text:
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    print("\tRetweeted")
                    new_tweets += 1
                except tweepy.TweepError as e:
                    print('\tAlready Retweeted')

        if "like" in text or "fav" in text:
            try:
                tweet.favorite()
                print('\t' + "Liked")
            except:
                print('\tAlready Liked')
      

print ("New Tweets: " + str(new_tweets))
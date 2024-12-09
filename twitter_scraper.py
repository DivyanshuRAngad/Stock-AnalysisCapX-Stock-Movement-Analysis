
import tweepy
import pandas as pd

# Twitter API credentials
api_key = "your_api_key"
api_secret = "your_api_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Scrape tweets
query = "#stocks OR #investing -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(100)

# Extract relevant information
data = [{"Date": tweet.created_at, "Text": tweet.full_text} for tweet in tweets]
df = pd.DataFrame(data)
df.to_csv("data/twitter_data.csv", index=False)
print("Data saved to twitter_data.csv")

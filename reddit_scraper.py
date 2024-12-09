
import praw
import pandas as pd

# Reddit API credentials
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="your_user_agent"
)

# Scrape subreddit posts
subreddit = reddit.subreddit("stocks")
posts = []
for post in subreddit.hot(limit=100):
    posts.append({"Title": post.title, "Score": post.score, "Comments": post.num_comments, "Text": post.selftext})
    
df = pd.DataFrame(posts)
df.to_csv("data/reddit_data.csv", index=False)
print("Data saved to reddit_data.csv")

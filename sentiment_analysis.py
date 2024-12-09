
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Load data
df = pd.read_csv("data/twitter_data.csv")  # Replace with the appropriate dataset

# Sentiment analysis
analyzer = SentimentIntensityAnalyzer()
df["Sentiment"] = df["Text"].apply(lambda x: analyzer.polarity_scores(x)["compound"])

# Save the data
df.to_csv("data/sentiment_data.csv", index=False)
print("Sentiment analysis completed and saved.")

import pandas as pd
import os

print("Loading required columns...")

df = pd.read_csv("data/twcs.csv")

print("Finding Spotify support tweets...")

# Extract all tweets directly written by Spotify support
spotify_tweets = df[df["author_id"] == "SpotifyCares"]

print(f"\nSpotify support tweets found: {len(spotify_tweets)}")

# Save Spotify tweets
os.makedirs("data/processed", exist_ok=True)

spotify_tweets.to_csv(
    "data/processed/spotify_support_tweets.csv",
    index=False
)

print("\n✅ Spotify data saved successfully!")
print("📁 Location: data/processed/spotify_support_tweets.csv")

print("\nFirst 10 Spotify tweets:")
print(spotify_tweets[["tweet_id", "text", "in_response_to_tweet_id"]].head(10).to_string())
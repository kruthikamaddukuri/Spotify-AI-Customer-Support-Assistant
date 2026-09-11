import pandas as pd
import os

print("Loading dataset...")

# Load the required columns
df = pd.read_csv(
    "data/twcs.csv",
    usecols=[
        "tweet_id",
        "author_id",
        "inbound",
        "text",
        "in_response_to_tweet_id"
    ]
)

print("Dataset loaded!")

# Get Spotify support replies
spotify = df[
    (df["author_id"] == "SpotifyCares") &
    (df["inbound"] == False)
].copy()

print(f"Spotify replies found: {len(spotify)}")

# Customer tweets only
customers = df[df["inbound"] == True].copy()

# Rename columns before merging
customers = customers.rename(columns={
    "tweet_id": "customer_tweet_id",
    "text": "customer_message"
})

spotify = spotify.rename(columns={
    "tweet_id": "spotify_tweet_id",
    "text": "spotify_response"
})

# Match Spotify reply with the customer tweet it replied to
pairs = spotify.merge(
    customers[
        ["customer_tweet_id", "customer_message"]
    ],
    left_on="in_response_to_tweet_id",
    right_on="customer_tweet_id",
    how="inner"
)

# Keep useful columns
pairs = pairs[
    [
        "customer_tweet_id",
        "customer_message",
        "spotify_tweet_id",
        "spotify_response"
    ]
]

# Remove missing values and duplicates
pairs = pairs.dropna()
pairs = pairs.drop_duplicates()

print(f"\n✅ Customer → Spotify pairs created: {len(pairs)}")

# Create processed folder if needed
os.makedirs("data/processed", exist_ok=True)

# Save pairs
pairs.to_csv(
    "data/processed/spotify_conversation_pairs.csv",
    index=False
)

print("\n💾 File saved successfully!")
print("📁 data/processed/spotify_conversation_pairs.csv")

print("\n🔍 First 10 conversation pairs:\n")

for i, row in pairs.head(10).iterrows():
    print("CUSTOMER:", row["customer_message"])
    print("SPOTIFY:", row["spotify_response"])
    print("-" * 100)
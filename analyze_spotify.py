import pandas as pd
from collections import Counter
import re

print("Loading cleaned Spotify data...")

df = pd.read_csv("data/processed/spotify_cleaned_pairs.csv")

print(f"\nTotal cleaned pairs: {len(df)}")

# Show shortest customer messages
print("\n" + "=" * 80)
print("🔍 SOME SHORT CUSTOMER MESSAGES")
print("=" * 80)

df["message_length"] = df["customer_message_clean"].str.len()

short_messages = df.sort_values("message_length").head(30)

for _, row in short_messages.iterrows():
    print(f"- {row['customer_message_clean']}")

# Basic keyword analysis
keywords = [
    "premium",
    "payment",
    "pay",
    "account",
    "login",
    "password",
    "playlist",
    "song",
    "music",
    "shuffle",
    "repeat",
    "app",
    "crash",
    "download",
    "offline",
    "subscription",
    "student",
    "family",
    "ads",
    "advertisement"
]

print("\n" + "=" * 80)
print("📊 KEYWORD COUNTS")
print("=" * 80)

text = " ".join(df["customer_message_clean"].astype(str)).lower()

for keyword in keywords:
    count = len(re.findall(r"\b" + re.escape(keyword) + r"\b", text))
    print(f"{keyword:15}: {count}")

# Show random examples
print("\n" + "=" * 80)
print("🎲 RANDOM CUSTOMER EXAMPLES")
print("=" * 80)

sample = df.sample(30, random_state=42)

for _, row in sample.iterrows():
    print("\nCUSTOMER:", row["customer_message_clean"])
    print("SPOTIFY:", row["spotify_response_clean"])
    print("-" * 80)
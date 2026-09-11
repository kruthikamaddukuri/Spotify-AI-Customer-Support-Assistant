import pandas as pd
import os

print("Loading useful Spotify dataset...")

df = pd.read_csv("data/processed/spotify_useful_pairs.csv")

print(f"Total useful pairs: {len(df)}")

# Take a random sample of 1000 conversations
sample = df.sample(n=1000, random_state=42)

# Save sample
os.makedirs("data/processed", exist_ok=True)

sample.to_csv(
    "data/processed/spotify_sample_1000.csv",
    index=False
)

print("\n✅ Sample created successfully!")
print("📁 Saved as: data/processed/spotify_sample_1000.csv")

print("\n🔍 First 10 customer messages:\n")

for i, message in enumerate(sample["customer_message_clean"].head(10), 1):
    print(f"{i}. {message}")
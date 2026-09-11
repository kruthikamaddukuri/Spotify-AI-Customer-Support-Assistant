import pandas as pd
import os

print("Loading cleaned dataset...")

df = pd.read_csv("data/processed/spotify_cleaned_pairs.csv")

print(f"Original dataset: {len(df)} rows")


# Convert messages to string
df["customer_message_clean"] = df["customer_message_clean"].astype(str)

# Calculate number of words
df["word_count"] = df["customer_message_clean"].str.split().str.len()


# Remove very short messages
df_filtered = df[df["word_count"] >= 4].copy()

print(f"After removing short messages: {len(df_filtered)} rows")


# Common non-problem messages
remove_messages = [
    "thanks",
    "thank you",
    "ok thx",
    "cheers",
    "merci",
    "will get back to you",
    "yes",
    "no",
    "please"
]

# Convert to lowercase for comparison
df_filtered["message_lower"] = (
    df_filtered["customer_message_clean"]
    .str.lower()
    .str.strip()
)

# Remove exact useless messages
df_filtered = df_filtered[
    ~df_filtered["message_lower"].isin(remove_messages)
].copy()


# Remove helper columns
df_filtered = df_filtered.drop(
    columns=["word_count", "message_lower", "message_length"],
    errors="ignore"
)

print(f"Final useful dataset: {len(df_filtered)} rows")


# Save
os.makedirs("data/processed", exist_ok=True)

df_filtered.to_csv(
    "data/processed/spotify_useful_pairs.csv",
    index=False
)

print("\n✅ Useful dataset saved successfully!")

print("📁 data/processed/spotify_useful_pairs.csv")

print("\n🔍 Sample messages:")

for message in df_filtered["customer_message_clean"].head(15):
    print("-", message)
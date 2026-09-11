import pandas as pd
import re
import html
import os

print("Loading Spotify conversation pairs...")

df = pd.read_csv("data/processed/spotify_conversation_pairs.csv")

print(f"Original pairs: {len(df)}")


# Function to clean Twitter text
def clean_text(text):

    if pd.isna(text):
        return ""

    text = str(text)

    # Convert HTML entities like &amp; → &
    text = html.unescape(text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove Twitter mentions
    text = re.sub(r"@\w+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Clean customer messages
df["customer_message_clean"] = df["customer_message"].apply(clean_text)

# Clean Spotify responses
df["spotify_response_clean"] = df["spotify_response"].apply(clean_text)


# Remove empty messages
df = df[
    (df["customer_message_clean"].str.len() > 5) &
    (df["spotify_response_clean"].str.len() > 5)
]

# Remove duplicates
df = df.drop_duplicates(
    subset=["customer_message_clean", "spotify_response_clean"]
)

print(f"Pairs after cleaning: {len(df)}")

# Save cleaned data
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/spotify_cleaned_pairs.csv",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")

print("\n📁 Location:")
print("data/processed/spotify_cleaned_pairs.csv")


# Show examples
print("\n🔍 First 10 cleaned examples:\n")

for _, row in df.head(10).iterrows():

    print("CUSTOMER:", row["customer_message_clean"])
    print("SPOTIFY:", row["spotify_response_clean"])
    print("-" * 80)
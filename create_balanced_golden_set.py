import pandas as pd
import os

print("Loading labeled dataset...")

df = pd.read_csv("data/processed/spotify_labeled_improved.csv")

# Remove Other intent
df = df[df["intent"] != "Other"].copy()

# Remove Playlist_Library because it has very few examples
df = df[df["intent"] != "Playlist_Library"].copy()

print(f"Available labeled examples: {len(df)}")

# Your final 10 intents
intents = [
    "Account_Security",
    "App_Technical",
    "Downloads_Offline",
    "Family_Student_Plan",
    "Feature_Request",
    "Login_Issue",
    "Music_Content",
    "Payment_Refund",
    "Playback_Issue",
    "Premium_Subscription"
]

golden_samples = []

print("\nCreating balanced sample...\n")

for intent in intents:

    intent_data = df[df["intent"] == intent]

    # Select 20 examples from each intent
    sample = intent_data.sample(n=20, random_state=42)

    golden_samples.append(sample)

    print(f"✅ {intent}: {len(sample)} examples selected")

# Combine all samples
golden_set = pd.concat(golden_samples)

# Add expected escalation action
escalate_intents = [
    "Account_Security",
    "Payment_Refund"
]

golden_set["expected_action"] = golden_set["intent"].apply(
    lambda intent: "ESCALATE_TO_HUMAN"
    if intent in escalate_intents
    else "AUTO_HANDLE"
)

# Keep the correct columns
golden_set = golden_set[
    [
        "customer_message_clean",
        "intent",
        "expected_action"
    ]
]

# Rename column to text for easier evaluation later
golden_set = golden_set.rename(
    columns={
        "customer_message_clean": "text"
    }
)

# Shuffle all examples
golden_set = golden_set.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Create golden folder
os.makedirs("data/golden", exist_ok=True)

# Save candidate golden set
output_path = "data/golden/golden_evaluation_candidates.csv"

golden_set.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("✅ BALANCED GOLDEN SET CREATED SUCCESSFULLY!")
print("=" * 60)

print(f"\n📁 Saved at: {output_path}")
print(f"📊 Total examples: {len(golden_set)}")

print("\nIntent Distribution:")
print(golden_set["intent"].value_counts())

print("\n🔍 First 10 examples:")
print(golden_set.head(10))
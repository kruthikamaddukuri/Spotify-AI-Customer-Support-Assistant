import pandas as pd
import os

print("Loading final training dataset...")

df = pd.read_csv("data/processed/final_training_dataset.csv")

print(f"Total available examples: {len(df)}")

# Randomly sample 200 examples
golden_set = df.sample(n=200, random_state=42).copy()

# Add expected escalation action
escalate_intents = [
    "Account_Security",
    "Payment_Refund"
]

golden_set["expected_action"] = golden_set["intent"].apply(
    lambda x: "ESCALATE_TO_HUMAN"
    if x in escalate_intents
    else "AUTO_HANDLE"
)

# Keep required columns
golden_set = golden_set[
    ["text", "intent", "expected_action"]
]

# Create folder if it doesn't exist
os.makedirs("data/golden", exist_ok=True)

# Save dataset
output_path = "data/golden/golden_evaluation_set.csv"

golden_set.to_csv(
    output_path,
    index=False
)

print("\n✅ Golden evaluation set created!")
print(f"📁 Saved at: {output_path}")

print("\n📊 Intent Distribution:")
print(golden_set["intent"].value_counts())

print("\n🔍 First 10 examples:")
print(golden_set.head(10))
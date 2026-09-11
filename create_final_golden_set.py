import pandas as pd
import os

input_file = "data/golden/golden_set_reviewed.csv"
output_file = "data/golden/final_golden_evaluation_set.csv"

print("Loading reviewed Golden Set...")

df = pd.read_csv(input_file)

# Create final golden set using human-reviewed labels
final_df = df[[
    "text",
    "human_intent",
    "human_expected_action"
]].copy()

# Rename columns for evaluation
final_df.columns = [
    "text",
    "intent",
    "expected_action"
]

# Save final dataset
os.makedirs("data/golden", exist_ok=True)
final_df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("FINAL GOLDEN EVALUATION SET CREATED!")
print("=" * 60)

print(f"\n📊 Total examples: {len(final_df)}")

print("\n📁 Saved at:")
print(output_file)

print("\n🎯 Final Intent Distribution:")
print(final_df["intent"].value_counts())

print("\n🤖 Expected Action Distribution:")
print(final_df["expected_action"].value_counts())

print("\n🔍 First 5 examples:")
print(final_df.head())

print("\n✅ Final Golden Set is ready for evaluation!")
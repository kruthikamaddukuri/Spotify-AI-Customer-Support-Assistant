import pandas as pd

print("Loading Golden Set candidates...")

df = pd.read_csv(
    "data/golden/golden_evaluation_candidates.csv"
)

# Add columns for manual review
df["human_intent"] = ""
df["human_expected_action"] = ""
df["review_status"] = "PENDING"
df["review_notes"] = ""

# Save review version
output_path = "data/golden/golden_set_for_manual_review.csv"

df.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("✅ MANUAL REVIEW FILE CREATED!")
print("=" * 60)

print(f"\n📁 File saved at:\n{output_path}")

print("\nYou can now open this CSV in Excel and manually review it.")
print(f"\nTotal examples to review: {len(df)}")
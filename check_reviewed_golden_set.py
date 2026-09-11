import pandas as pd

file_path = "data/golden/golden_set_reviewed.csv"

print("Loading reviewed Golden Set...\n")

df = pd.read_csv(file_path)

print("=" * 60)
print("GOLDEN SET VALIDATION")
print("=" * 60)

print(f"\nTotal rows: {len(df)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nEmpty human_intent values:")
print(df["human_intent"].isna().sum())

print("\nEmpty human_expected_action values:")
print(df["human_expected_action"].isna().sum())

print("\nReview Status Distribution:")
print(df["review_status"].value_counts(dropna=False))

print("\nHuman Intent Distribution:")
print(df["human_intent"].value_counts(dropna=False))

print("\nHuman Expected Action Distribution:")
print(df["human_expected_action"].value_counts(dropna=False))

print("\n" + "=" * 60)

if len(df) == 200:
    print("✅ Correct number of examples: 200")
else:
    print(f"⚠️ Expected 200 examples, found {len(df)}")

print("=" * 60)
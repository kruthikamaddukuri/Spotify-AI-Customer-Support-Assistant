import pandas as pd

print("Loading human review file...")

file_path = "data/golden/human_review_sample.csv"

df = pd.read_csv(file_path)

human_labels = [
    "PARTIAL",
    "PARTIAL",
    "GOOD",
    "PARTIAL",
    "GOOD",
    "POOR",
    "GOOD",
    "PARTIAL",
    "PARTIAL",
    "GOOD",
    "POOR",
    "GOOD",
    "POOR",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "POOR",
    "PARTIAL",
    "POOR",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD",
    "GOOD"
]

if len(df) != len(human_labels):
    raise ValueError(
        f"Expected {len(human_labels)} rows, but found {len(df)} rows."
    )

df["human_quality"] = human_labels

df.to_csv(file_path, index=False)

print("\n" + "=" * 60)
print("HUMAN LABELS SAVED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal examples labeled: {len(df)}")

print("\nHuman quality distribution:")
print(df["human_quality"].value_counts())

print(f"\nSaved at: {file_path}")
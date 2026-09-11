import pandas as pd

print("Loading improved labeled dataset...")

df = pd.read_csv("data/processed/spotify_labeled_improved.csv")

print("\n" + "=" * 60)
print("FINAL DATASET DISTRIBUTION")
print("=" * 60)

counts = df["intent"].value_counts()

for intent, count in counts.items():
    print(f"{intent:25} : {count}")

print("\nTotal examples:", len(df))

print("\n" + "=" * 60)
print("CHECKING FOR SMALL CATEGORIES")
print("=" * 60)

for intent, count in counts.items():

    if count < 100:
        print(f"⚠️ {intent} has only {count} examples")
    else:
        print(f"✅ {intent} has {count} examples")

print("\nDone!")
import pandas as pd

print("Loading labeled dataset...")

df = pd.read_csv("data/processed/spotify_labeled_improved.csv")

print(f"Original dataset: {len(df)} rows")


# Remove the category with too few examples
df = df[df["intent"] != "Playlist_Library"].copy()


# Keep only the columns needed for ML
final_df = df[
    ["customer_message_clean", "intent"]
].copy()


# Remove any missing values
final_df.dropna(inplace=True)


# Rename the text column to something simpler
final_df.rename(
    columns={
        "customer_message_clean": "text"
    },
    inplace=True
)


# Remove duplicate messages
final_df.drop_duplicates(
    subset=["text"],
    inplace=True
)


print(f"\nFinal training examples: {len(final_df)}")


print("\n📊 FINAL INTENT DISTRIBUTION:\n")

print(final_df["intent"].value_counts())


# Save final dataset
final_df.to_csv(
    "data/processed/final_training_dataset.csv",
    index=False
)


print("\n✅ Final training dataset created successfully!")

print("📁 Location:")
print("data/processed/final_training_dataset.csv")


print("\n🔍 SAMPLE DATA:\n")

print(final_df.head(10))
import pandas as pd
import os
import re

print("Loading useful Spotify dataset...")

df = pd.read_csv("data/processed/spotify_useful_pairs.csv")

print(f"Total messages: {len(df)}")


def assign_intent(text):

    text = str(text).lower()

    # Account & Security
    if any(word in text for word in [
        "hacked", "hack", "account compromised",
        "account stolen"
    ]):
        return "Account_Security"

    # Login
    elif any(word in text for word in [
        "login", "log in", "sign in", "sign-in",
        "can't access"
    ]):
        return "Login_Issue"

    # Payment & Refund
    elif any(word in text for word in [
        "charged twice", "refund", "overcharged",
        "charged", "payment failed"
    ]):
        return "Payment_Refund"

    # Family & Student
    elif any(word in text for word in [
        "family plan", "family member",
        "student discount", "student premium",
        "unidays"
    ]):
        return "Family_Student_Plan"

    # Premium & Subscription
    elif any(word in text for word in [
        "premium", "subscription",
        "free account", "premium account"
    ]):
        return "Premium_Subscription"

    # Downloads & Offline
    elif any(word in text for word in [
        "offline", "downloaded",
        "downloads", "download music"
    ]):
        return "Downloads_Offline"

    # Playlist & Library
    elif any(word in text for word in [
        "playlist disappeared", "lost playlist",
        "my playlist", "library"
    ]):
        return "Playlist_Library"

    # Playback
    elif any(word in text for word in [
        "won't play", "wont play",
        "stops playing", "shuffle",
        "repeat button", "music stops"
    ]):
        return "Playback_Issue"

    # App & Technical
    elif any(word in text for word in [
        "app crashes", "app crash",
        "app doesn't work", "app wont work",
        "app not working", "bug"
    ]):
        return "App_Technical"

    # Music content
    elif any(word in text for word in [
        "missing songs", "missing album",
        "add music", "add song",
        "album missing", "not available"
    ]):
        return "Music_Content"

    # Feature Request
    elif any(word in text for word in [
        "feature", "please add",
        "should add", "make it happen",
        "would be great if"
    ]):
        return "Feature_Request"

    else:
        return "Other"


print("\nAssigning preliminary intents...")

df["intent"] = df["customer_message_clean"].apply(assign_intent)


print("\n📊 INTENT DISTRIBUTION:\n")

print(df["intent"].value_counts())


# Keep only messages with identified intents
labeled_df = df[df["intent"] != "Other"].copy()

print(f"\nTotal labeled messages: {len(labeled_df)}")


# Save dataset
os.makedirs("data/processed", exist_ok=True)

labeled_df.to_csv(
    "data/processed/spotify_labeled_preliminary.csv",
    index=False
)

print("\n✅ Preliminary labeled dataset saved!")

print("📁 data/processed/spotify_labeled_preliminary.csv")


print("\n🔍 EXAMPLES FROM EACH INTENT:\n")

for intent in labeled_df["intent"].unique():

    print("\n" + "=" * 70)
    print("INTENT:", intent)
    print("=" * 70)

    examples = labeled_df[
        labeled_df["intent"] == intent
    ].head(3)

    for _, row in examples.iterrows():
        print("-", row["customer_message_clean"])
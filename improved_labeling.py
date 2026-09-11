import pandas as pd
import re
import os

print("Loading useful Spotify dataset...")

df = pd.read_csv("data/processed/spotify_useful_pairs.csv")

print(f"Total messages: {len(df)}")


def has_any(text, patterns):
    """Check whether any pattern exists in the text."""
    return any(re.search(pattern, text) for pattern in patterns)


def assign_intent(text):

    text = str(text).lower().strip()

    # =========================================================
    # 1. ACCOUNT SECURITY - highest confidence
    # =========================================================
    if has_any(text, [
        r"\bhacked\b",
        r"\bhack(ed)? my account\b",
        r"\baccount compromised\b",
        r"\bsomeone (got|has) into my account\b",
        r"\bsomeone else.*my account\b",
        r"\bchanged my email\b.*account"
    ]):
        return "Account_Security"

    # =========================================================
    # 2. PAYMENT / REFUND
    # =========================================================
    if has_any(text, [
        r"\bcharged twice\b",
        r"\bcharged.*twice\b",
        r"\bovercharged\b",
        r"\brefund\b",
        r"\bdouble charged\b",
        r"\bcharged.*but.*premium\b"
    ]):
        return "Payment_Refund"

    # =========================================================
    # 3. FAMILY / STUDENT PLAN
    # =========================================================
    if has_any(text, [
        r"\bfamily plan\b",
        r"\bpremium family\b",
        r"\bfamily member\b",
        r"\bfamily invite\b",
        r"\bstudent discount\b",
        r"\bstudent premium\b",
        r"\bunidays\b"
    ]):
        return "Family_Student_Plan"

    # =========================================================
    # 4. DOWNLOAD / OFFLINE
    # =========================================================
    if has_any(text, [
        r"\boffline\b",
        r"\bdownloads? (disappeared|deleted|removed)\b",
        r"\bdownloaded music.*deleted\b",
        r"\bdownloaded playlist.*deleted\b",
        r"\bdownloads? unexpectedly removed\b"
    ]):
        return "Downloads_Offline"

    # =========================================================
    # 5. PLAYBACK / SHUFFLE
    # Check BEFORE Premium because Premium may appear in the message
    # =========================================================
    if has_any(text, [
        r"\bshuffle\b",
        r"\brepeat button\b",
        r"\bwon'?t play\b",
        r"\bcannot play\b",
        r"\bcan'?t play\b",
        r"\bstops playing\b",
        r"\bmusic stops\b",
        r"\bplay one song.*stop\b",
        r"\bwon'?t let me play\b"
    ]):
        return "Playback_Issue"

    # =========================================================
    # 6. LOGIN
    # =========================================================
    if has_any(text, [
        r"\bcan'?t log ?in\b",
        r"\bcannot log ?in\b",
        r"\bwon'?t log ?in\b",
        r"\bunable to log ?in\b",
        r"\blogin screen.*not\b",
        r"\bsign in.*not working\b"
    ]):
        return "Login_Issue"

    # =========================================================
    # 7. APP TECHNICAL
    # =========================================================
    if has_any(text, [
        r"\bapp.*crash",
        r"\bapp.*not working\b",
        r"\bapp.*doesn'?t work\b",
        r"\bapp.*won'?t work\b",
        r"\bspotify.*crashes\b",
        r"\bbugfest\b",
        r"\bapp.*bug\b"
    ]):
        return "App_Technical"

    # =========================================================
    # 8. PLAYLIST / LIBRARY
    # =========================================================
    if has_any(text, [
        r"\bplaylist(s)? (disappeared|gone|deleted|missing)\b",
        r"\blost my playlist\b",
        r"\bmy playlist.*gone\b",
        r"\bsongs? disappeared from.*playlist\b",
        r"\blost.*library\b"
    ]):
        return "Playlist_Library"

    # =========================================================
    # 9. MUSIC / CONTENT AVAILABILITY
    # =========================================================
    if has_any(text, [
        r"\bsong.*missing\b",
        r"\bsongs.*missing\b",
        r"\balbum.*missing\b",
        r"\badd.*song\b",
        r"\badd.*music\b",
        r"\bput.*on spotify\b",
        r"\bnot available on spotify\b",
        r"\bmissing from spotify\b"
    ]):
        return "Music_Content"

    # =========================================================
    # 10. FEATURE REQUEST
    # =========================================================
    if has_any(text, [
        r"\bplease add\b",
        r"\bshould add\b",
        r"\badd a feature\b",
        r"\bmake it a feature\b",
        r"\bfeature request\b",
        r"\bi wish spotify had\b",
        r"\bwould be great if\b"
    ]):
        return "Feature_Request"

    # =========================================================
    # 11. PREMIUM / SUBSCRIPTION
    # Keep near the end
    # =========================================================
    if has_any(text, [
        r"\bpremium.*not working\b",
        r"\bpremium.*not activated\b",
        r"\bpremium.*expired\b",
        r"\bsubscription.*not working\b",
        r"\bsubscription.*expire\b",
        r"\bpaid.*premium.*free\b",
        r"\bpremium.*free account\b",
        r"\bno premium\b"
    ]):
        return "Premium_Subscription"

    return "Other"


print("\nAssigning improved intents...")

df["intent"] = df["customer_message_clean"].apply(assign_intent)


print("\n📊 IMPROVED INTENT DISTRIBUTION:\n")
print(df["intent"].value_counts())


# Keep only confidently labeled rows
labeled_df = df[df["intent"] != "Other"].copy()

print(f"\n✅ High-confidence labeled messages: {len(labeled_df)}")


# Save the improved dataset
os.makedirs("data/processed", exist_ok=True)

labeled_df.to_csv(
    "data/processed/spotify_labeled_improved.csv",
    index=False
)

print("\n💾 Improved dataset saved successfully!")
print("📁 data/processed/spotify_labeled_improved.csv")


# Show 3 examples from every intent
print("\n🔍 EXAMPLES FROM EACH INTENT:")

for intent in sorted(labeled_df["intent"].unique()):

    print("\n" + "=" * 70)
    print("INTENT:", intent)
    print("=" * 70)

    examples = labeled_df[
        labeled_df["intent"] == intent
    ].sample(
        n=min(3, len(labeled_df[labeled_df["intent"] == intent])),
        random_state=42
    )

    for _, row in examples.iterrows():
        print("-", row["customer_message_clean"])
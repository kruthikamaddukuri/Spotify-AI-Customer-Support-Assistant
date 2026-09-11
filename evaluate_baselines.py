import pandas as pd
import joblib
from collections import Counter

print("Loading Golden Evaluation Set...")

# Load golden evaluation set
df = pd.read_csv("data/golden/final_golden_evaluation_set.csv")

# Load trained ML model
model = joblib.load("models/spotify_intent_model.pkl")

total = len(df)

print(f"Total examples: {total}")

# ============================================================
# BASELINE 1: TRIVIAL BASELINE
# Always predict the most common intent from the golden set
# ============================================================

most_common_intent = df["intent"].mode()[0]

trivial_predictions = [most_common_intent] * total

trivial_correct = sum(
    predicted == actual
    for predicted, actual in zip(trivial_predictions, df["intent"])
)

trivial_accuracy = trivial_correct / total


# ============================================================
# BASELINE 2: SIMPLE KEYWORD-BASED CLASSIFIER
# ============================================================

def keyword_classifier(text):

    text = str(text).lower()

    if any(word in text for word in [
        "hacked", "hack", "someone else using my account",
        "security", "changed my email"
    ]):
        return "Account_Security"

    elif any(word in text for word in [
        "refund", "charged twice", "double charged",
        "charged me twice", "money back"
    ]):
        return "Payment_Refund"

    elif any(word in text for word in [
        "login", "log in", "password", "can't access"
    ]):
        return "Login_Issue"

    elif any(word in text for word in [
        "offline", "downloaded", "downloads",
        "download music"
    ]):
        return "Downloads_Offline"

    elif any(word in text for word in [
        "family plan", "student discount",
        "student premium", "hulu"
    ]):
        return "Family_Student_Plan"

    elif any(word in text for word in [
        "premium", "subscription"
    ]):
        return "Premium_Subscription"

    elif any(word in text for word in [
        "shuffle", "won't play", "wont play",
        "songs won't play", "song won't play",
        "playback"
    ]):
        return "Playback_Issue"

    elif any(word in text for word in [
        "crash", "crashing", "app not working",
        "bug", "desktop app"
    ]):
        return "App_Technical"

    elif any(word in text for word in [
        "feature request", "please add",
        "add a feature", "would be great"
    ]):
        return "Feature_Request"

    else:
        return "Music_Content"


keyword_predictions = [
    keyword_classifier(text)
    for text in df["text"]
]

keyword_correct = sum(
    predicted == actual
    for predicted, actual in zip(keyword_predictions, df["intent"])
)

keyword_accuracy = keyword_correct / total


# ============================================================
# OUR ML MODEL
# ============================================================

ml_predictions = model.predict(df["text"])

ml_correct = sum(
    predicted == actual
    for predicted, actual in zip(ml_predictions, df["intent"])
)

ml_accuracy = ml_correct / total


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 65)
print("BASELINE COMPARISON RESULTS")
print("=" * 65)

print("\n1. TRIVIAL BASELINE")
print(f"Strategy: Always predict '{most_common_intent}'")
print(f"Accuracy: {trivial_accuracy:.2%}")
print(f"Correct: {trivial_correct}/{total}")

print("\n2. KEYWORD-BASED BASELINE")
print("Strategy: Rule-based keyword matching")
print(f"Accuracy: {keyword_accuracy:.2%}")
print(f"Correct: {keyword_correct}/{total}")

print("\n3. OUR ML MODEL")
print("Strategy: Trained Spotify intent classification model")
print(f"Accuracy: {ml_accuracy:.2%}")
print(f"Correct: {ml_correct}/{total}")


# ============================================================
# SAVE RESULTS
# ============================================================

results = pd.DataFrame({
    "Model": [
        "Trivial Baseline",
        "Keyword Baseline",
        "ML Model"
    ],
    "Accuracy": [
        trivial_accuracy,
        keyword_accuracy,
        ml_accuracy
    ],
    "Correct_Predictions": [
        trivial_correct,
        keyword_correct,
        ml_correct
    ],
    "Total_Examples": [
        total,
        total,
        total
    ]
})

results.to_csv(
    "data/golden/baseline_comparison.csv",
    index=False
)

print("\n" + "=" * 65)
print("RESULTS SAVED")
print("=" * 65)

print("\n📁 data/golden/baseline_comparison.csv")
print("\n✅ Baseline evaluation completed successfully!")
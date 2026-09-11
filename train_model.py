import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

import joblib
import os


print("Loading final training dataset...")

df = pd.read_csv(
    "data/processed/final_training_dataset.csv"
)

print(f"Total examples: {len(df)}")

print("\nIntent categories:")

print(df["intent"].value_counts())


# Input text
X = df["text"].fillna("").astype(str)

# Output labels
y = df["intent"]


# Split dataset into training and testing data
print("\nSplitting dataset into training and testing data...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training examples: {len(X_train)}")
print(f"Testing examples: {len(X_test)}")


# Create the AI pipeline
print("\nCreating TF-IDF + Logistic Regression model...")

model = Pipeline([

    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=5000,
            ngram_range=(1, 2)
        )
    ),

    (
        "classifier",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced"
        )
    )

])


# Train model
print("\n🤖 Training the AI model... Please wait...")

model.fit(X_train, y_train)


# Make predictions
print("\nMaking predictions on unseen test data...")

predictions = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 60)
print("MODEL RESULTS")
print("=" * 60)

print(f"\n🎯 Accuracy: {accuracy * 100:.2f}%\n")


# Detailed metrics
print("📊 Classification Report:\n")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# Create models folder
os.makedirs("models", exist_ok=True)


# Save trained model
joblib.dump(
    model,
    "models/spotify_intent_model.pkl"
)


print("\n✅ MODEL TRAINED SUCCESSFULLY!")

print("💾 Model saved at:")

print("models/spotify_intent_model.pkl")
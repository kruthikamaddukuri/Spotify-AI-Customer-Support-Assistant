import pandas as pd
import joblib

from escalation_policy import decide_action


print("Loading Golden Evaluation Set...")

# Load Golden Evaluation Set
df = pd.read_csv("data/golden/final_golden_evaluation_set.csv")

# Load trained model
model = joblib.load("models/spotify_intent_model.pkl")

print(f"Total examples: {len(df)}")
print("\nEvaluating model...\n")


correct_intents = 0
correct_actions = 0

results = []


# Evaluate every example
for _, row in df.iterrows():

    text = row["text"]
    expected_intent = row["intent"]
    expected_action = row["expected_action"]

    # Predict intent
    predicted_intent = model.predict([text])[0]

    # Get prediction confidence
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    # Decide whether to auto-handle or escalate
    decision = decide_action(predicted_intent, confidence)

    # Extract values from dictionary
    predicted_action = decision["action"]
    reason = decision["reason"]

    # Check intent prediction
    intent_correct = predicted_intent == expected_intent

    # Check escalation decision
    action_correct = predicted_action == expected_action

    # Count correct predictions
    if intent_correct:
        correct_intents += 1

    if action_correct:
        correct_actions += 1

    # Save result
    results.append({
        "text": text,

        "expected_intent": expected_intent,
        "predicted_intent": predicted_intent,
        "intent_correct": intent_correct,

        "confidence": round(confidence, 4),

        "expected_action": expected_action,
        "predicted_action": predicted_action,
        "action_correct": action_correct,

        "reason": reason
    })


# Calculate accuracy
total_examples = len(df)

intent_accuracy = correct_intents / total_examples
action_accuracy = correct_actions / total_examples


# Display results
print("=" * 60)
print("GOLDEN SET EVALUATION RESULTS")
print("=" * 60)

print(f"\nTotal Examples: {total_examples}")

print(f"\nIntent Accuracy: {intent_accuracy:.2%}")
print(f"Correct Intent Predictions: {correct_intents}/{total_examples}")

print(f"\nAction Accuracy: {action_accuracy:.2%}")
print(f"Correct Action Predictions: {correct_actions}/{total_examples}")


# Save detailed results
results_df = pd.DataFrame(results)

output_path = "data/golden/evaluation_results.csv"

results_df.to_csv(output_path, index=False)


print("\n" + "=" * 60)
print("DETAILED RESULTS SAVED")
print("=" * 60)

print(f"\n📁 {output_path}")

print("\n✅ Evaluation completed successfully!")
import pandas as pd

print("Loading failure analysis results...")

df = pd.read_csv(
    "data/golden/failure_analysis_predictions.csv"
)

# Top 5 failure patterns identified from the evaluation
failure_patterns = [
    ("Music_Content", "Feature_Request"),
    ("Family_Student_Plan", "Premium_Subscription"),
    ("Feature_Request", "Music_Content"),
    ("App_Technical", "Music_Content"),
    ("Feature_Request", "Downloads_Offline")
]

print("\n" + "=" * 70)
print("TOP FAILURE MODES WITH REAL EXAMPLES")
print("=" * 70)

results = []

for i, (expected, predicted) in enumerate(failure_patterns, start=1):

    matching = df[
        (df["expected_intent"] == expected) &
        (df["predicted_intent"] == predicted)
    ]

    print(f"\nFAILURE MODE {i}")
    print(f"Expected Intent: {expected}")
    print(f"Predicted Intent: {predicted}")
    print(f"Total Cases: {len(matching)}")

    # Show up to 3 real examples
    examples = matching.head(3)

    for _, row in examples.iterrows():

        print("\nCustomer Message:")
        print(row["text"])

        print(f"Confidence: {row['confidence']}")

        results.append({
            "failure_mode": i,
            "expected_intent": expected,
            "predicted_intent": predicted,
            "customer_message": row["text"],
            "confidence": row["confidence"]
        })

results_df = pd.DataFrame(results)

output_path = "data/golden/top_failure_examples.csv"

results_df.to_csv(output_path, index=False)

print("\n" + "=" * 70)
print("FAILURE EXAMPLES SAVED")
print("=" * 70)

print(f"\nSaved to: {output_path}")
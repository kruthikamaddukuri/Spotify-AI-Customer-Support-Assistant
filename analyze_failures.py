import pandas as pd

print("Loading golden set evaluation results...")

df = pd.read_csv(
    "data/golden/evaluation_results.csv"
)

print(f"Total examples: {len(df)}")

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nFinding incorrect predictions...")

# Automatically detect rows where prediction differs from expected intent
incorrect = df[
    df["expected_intent"] != df["predicted_intent"]
].copy()

print(f"\nIncorrect predictions: {len(incorrect)}")

print("\nTop confusion patterns:")

confusions = (
    incorrect
    .groupby(["expected_intent", "predicted_intent"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)

print(confusions.head(10).to_string(index=False))

output_path = "data/golden/failure_analysis_predictions.csv"

incorrect.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("FAILURE ANALYSIS COMPLETED")
print("=" * 60)

print(f"\nIncorrect examples saved to: {output_path}")
print("\nThese examples will help us identify the top 5 failure modes.")
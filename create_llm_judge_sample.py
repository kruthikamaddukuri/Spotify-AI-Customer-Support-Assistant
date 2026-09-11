import pandas as pd

print("Loading no-data-leakage reply evaluation results...")

df = pd.read_csv(
    "data/golden/reply_quality_results_no_leakage.csv"
)

print(f"Total available examples: {len(df)}")

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nCreating a random evaluation sample...")

sample_size = min(30, len(df))

sample_df = df.sample(
    n=sample_size,
    random_state=42
).copy()

output_path = "data/golden/llm_judge_sample.csv"

sample_df.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("LLM JUDGE SAMPLE CREATED SUCCESSFULLY!")
print("=" * 60)

print(f"\nTotal examples selected: {len(sample_df)}")
print(f"Saved at: {output_path}")

print("\nIMPORTANT:")
print("This sample is created from the NO-DATA-LEAKAGE evaluation results.")
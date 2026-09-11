import pandas as pd

print("Loading the 30-example LLM judge sample...")

df = pd.read_csv("data/golden/llm_judge_sample.csv")

print(f"Total examples: {len(df)}")

# Create a human review file for the EXACT same 30 examples
human_review_df = pd.DataFrame({
    "example_id": range(1, len(df) + 1),
    "customer_message": df["text"],
    "support_reply": df["historical_reply"],
    "human_quality": ""
})

output_path = "data/golden/human_review_sample.csv"

human_review_df.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("HUMAN REVIEW FILE CREATED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal examples: {len(human_review_df)}")
print(f"Saved at: {output_path}")

print("\nReview each example using:")
print("GOOD = relevant, helpful, and appropriate")
print("PARTIAL = somewhat relevant but incomplete")
print("POOR = irrelevant or unhelpful")
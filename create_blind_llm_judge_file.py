import pandas as pd

print("Loading LLM judge sample...")

df = pd.read_csv(
    "data/golden/llm_judge_sample.csv"
)

print(f"Total examples: {len(df)}")

# Create a blind evaluation dataset.
# Claude will only see the customer message and retrieved reply.

blind_df = pd.DataFrame({
    "example_id": range(1, len(df) + 1),
    "customer_message": df["text"],
    "support_reply": df["historical_reply"]
})

output_path = "data/golden/blind_llm_judge_sample.csv"

blind_df.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("BLIND LLM JUDGE FILE CREATED SUCCESSFULLY!")
print("=" * 60)

print(f"\nTotal examples: {len(blind_df)}")
print(f"Saved at: {output_path}")

print("\nClaude will only see:")
print("- Example ID")
print("- Customer Message")
print("- Support Reply")
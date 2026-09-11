import pandas as pd

results = [
    [1, "PARTIAL"],
    [2, "PARTIAL"],
    [3, "GOOD"],
    [4, "PARTIAL"],
    [5, "GOOD"],
    [6, "POOR"],
    [7, "GOOD"],
    [8, "PARTIAL"],
    [9, "PARTIAL"],
    [10, "GOOD"],
    [11, "POOR"],
    [12, "GOOD"],
    [13, "POOR"],
    [14, "GOOD"],
    [15, "GOOD"],
    [16, "GOOD"],
    [17, "GOOD"],
    [18, "POOR"],
    [19, "PARTIAL"],
    [20, "POOR"],
    [21, "GOOD"],
    [22, "GOOD"],
    [23, "GOOD"],
    [24, "GOOD"],
    [25, "GOOD"],
    [26, "GOOD"],
    [27, "GOOD"],
    [28, "GOOD"],
    [29, "GOOD"],
    [30, "GOOD"]
]

df = pd.DataFrame(
    results,
    columns=["example_id", "llm_overall_quality"]
)

output_path = "data/golden/llm_judge_results.csv"

df.to_csv(output_path, index=False)

print("=" * 60)
print("LLM JUDGE RESULTS SAVED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal results: {len(df)}")

print("\nQuality distribution:")
print(df["llm_overall_quality"].value_counts())

print(f"\nSaved at: {output_path}")
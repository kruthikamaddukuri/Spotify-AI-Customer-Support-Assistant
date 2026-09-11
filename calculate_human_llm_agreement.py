import pandas as pd
from sklearn.metrics import cohen_kappa_score, confusion_matrix

print("Loading human evaluation results...")

human_df = pd.read_csv(
    "data/golden/human_review_sample.csv"
)

print("Loading Claude LLM judge results...")

llm_df = pd.read_csv(
    "data/golden/llm_judge_results.csv"
)

# Merge using example_id
df = human_df.merge(
    llm_df,
    on="example_id"
)

human_labels = df["human_quality"]
llm_labels = df["llm_overall_quality"]

# Exact agreement
agreement = (
    human_labels == llm_labels
).mean() * 100

# Cohen's Kappa
kappa = cohen_kappa_score(
    human_labels,
    llm_labels
)

# Confusion matrix
labels = ["GOOD", "PARTIAL", "POOR"]

matrix = confusion_matrix(
    human_labels,
    llm_labels,
    labels=labels
)

print("\n" + "=" * 60)
print("HUMAN vs LLM JUDGE AGREEMENT")
print("=" * 60)

print(f"\nTotal examples: {len(df)}")
print(f"Exact Agreement: {agreement:.2f}%")
print(f"Cohen's Kappa: {kappa:.3f}")

print("\nConfusion Matrix")
print("Rows = Human | Columns = LLM")

matrix_df = pd.DataFrame(
    matrix,
    index=labels,
    columns=labels
)

print(matrix_df)

# Save merged comparison
output_path = "data/golden/human_llm_agreement_results.csv"

df.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("RESULTS SAVED")
print("=" * 60)

print(f"\nSaved at: {output_path}")
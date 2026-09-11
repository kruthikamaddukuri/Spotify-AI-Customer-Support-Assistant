import pandas as pd
from sklearn.metrics import cohen_kappa_score, confusion_matrix

print("Loading independent human labels...")
human_df = pd.read_csv(
    "data/golden/blind_llm_judge_sample.csv",
    encoding="latin1"
)

print("Loading Claude LLM judge results...")
llm_df = pd.read_csv(
    "data/golden/llm_judge_results.csv",
    encoding="latin1"
)

# Keep only the columns needed for comparison
human_df = human_df[["example_id", "human_quality"]]
llm_df = llm_df[["example_id", "llm_overall_quality"]]

# Merge by example ID
df = human_df.merge(llm_df, on="example_id")

# Normalize labels
df["human_quality"] = df["human_quality"].astype(str).str.strip().str.upper()
df["llm_overall_quality"] = (
    df["llm_overall_quality"].astype(str).str.strip().str.upper()
)

# Calculate agreement
exact_agreement = (
    df["human_quality"] == df["llm_overall_quality"]
).mean() * 100

kappa = cohen_kappa_score(
    df["human_quality"],
    df["llm_overall_quality"]
)

labels = ["GOOD", "PARTIAL", "POOR"]

cm = confusion_matrix(
    df["human_quality"],
    df["llm_overall_quality"],
    labels=labels
)

print("\n" + "=" * 60)
print("INDEPENDENT HUMAN vs CLAUDE LLM AGREEMENT")
print("=" * 60)

print(f"\nTotal examples: {len(df)}")
print(f"Exact Agreement: {exact_agreement:.2f}%")
print(f"Cohen's Kappa: {kappa:.3f}")

print("\nConfusion Matrix")
print("Rows = Human | Columns = Claude\n")

cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels
)

print(cm_df)

# Save results
df.to_csv(
    "data/golden/independent_human_llm_comparison.csv",
    index=False
)

print("\n" + "=" * 60)
print("RESULTS SAVED")
print("=" * 60)

print(
    "\nSaved at: data/golden/independent_human_llm_comparison.csv"
)
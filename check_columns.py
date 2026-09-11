import pandas as pd

df = pd.read_csv("data/processed/spotify_labeled_improved.csv")

print("COLUMN NAMES:")
print(df.columns.tolist())

print("\nFIRST 5 ROWS:")
print(df.head())
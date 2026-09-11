import pandas as pd

print("Loading dataset... please wait")

df = pd.read_csv(
    "data/twcs.csv",
    usecols=["author_id", "inbound"]
)

print("Dataset loaded!")

# First check what values exist in inbound
print("\nInbound values:")
print(df["inbound"].value_counts(dropna=False))

# Find company/support accounts
companies = df[df["inbound"] == False]

print("\nNumber of company tweets:", len(companies))

# Count company accounts
brand_counts = companies["author_id"].value_counts()

print("\n🏢 TOP 30 BRANDS/COMPANIES:\n")
print(brand_counts.head(30).to_string())
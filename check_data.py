import pandas as pd

# Load dataset
df = pd.read_csv("data/twcs.csv")

print("✅ Dataset loaded successfully!")

print("\n📊 Dataset Shape:")
print(df.shape)

print("\n📋 Column Names:")
print(df.columns.tolist())

print("\n🔍 First 10 Rows:")
print(df.head(10).to_string())

print("\n📌 Data Types:")
print(df.dtypes)
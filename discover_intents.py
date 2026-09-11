import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

print("Loading Spotify sample...")

df = pd.read_csv("data/processed/spotify_sample_1000.csv")

texts = df["customer_message_clean"].fillna("").astype(str)

print("Creating TF-IDF features...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=2000,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(texts)

print("Finding customer issue groups...")

# Create 10 clusters
kmeans = KMeans(
    n_clusters=10,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X)

# Get important words for each cluster
terms = vectorizer.get_feature_names_out()

print("\n" + "=" * 70)
print("🔍 DISCOVERED CUSTOMER ISSUE GROUPS")
print("=" * 70)

for cluster_num in range(10):

    print(f"\n📌 CLUSTER {cluster_num}")

    center = kmeans.cluster_centers_[cluster_num]

    top_indices = center.argsort()[-10:][::-1]

    top_words = [terms[i] for i in top_indices]

    print("Top keywords:", ", ".join(top_words))

    print("\nExample customer messages:")

    examples = df[df["cluster"] == cluster_num].head(5)

    for _, row in examples.iterrows():
        print("-", row["customer_message_clean"])

# Save clustered sample
df.to_csv(
    "data/processed/spotify_sample_clustered.csv",
    index=False
)

print("\n✅ Clustered dataset saved successfully!")
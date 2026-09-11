import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = "data/processed/spotify_labeled_improved.csv"


print("Loading historical Spotify support conversations...")

df = pd.read_csv(DATA_PATH)

# Keep only rows that have both customer message and Spotify response
df = df.dropna(
    subset=["customer_message_clean", "spotify_response_clean", "intent"]
)

print(f"Historical conversations loaded: {len(df)}")


# ============================================================
# BUILD TF-IDF RETRIEVAL INDEX
# ============================================================

print("Building reply retrieval system...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

message_vectors = vectorizer.fit_transform(
    df["customer_message_clean"].astype(str)
)


# ============================================================
# RETRIEVE SIMILAR HISTORICAL RESPONSE
# ============================================================

def get_similar_response(customer_message, predicted_intent, top_k=3):

    # Only search conversations with the same predicted intent
    intent_df = df[df["intent"] == predicted_intent].copy()

    if len(intent_df) == 0:
        return {
            "response": None,
            "similarity": 0,
            "matched_message": None
        }

    # Get original indices
    indices = intent_df.index.tolist()

    # Transform customer message
    query_vector = vectorizer.transform([customer_message])

    # Get vectors for matching intent examples
    intent_vectors = message_vectors[indices]

    # Calculate similarity
    similarities = cosine_similarity(
        query_vector,
        intent_vectors
    )[0]

    # Best match
    best_position = similarities.argmax()

    best_similarity = similarities[best_position]

    best_index = indices[best_position]

    matched_message = df.loc[
        best_index,
        "customer_message_clean"
    ]

    matched_response = df.loc[
        best_index,
        "spotify_response_clean"
    ]

    return {
        "response": matched_response,
        "similarity": float(best_similarity),
        "matched_message": matched_message
    }


# ============================================================
# SAVE RETRIEVAL SYSTEM
# ============================================================

print("Saving retrieval components...")

joblib.dump(
    {
        "vectorizer": vectorizer,
        "message_vectors": message_vectors,
        "data": df
    },
    "models/spotify_reply_retrieval.pkl"
)


print("\n" + "=" * 60)
print("✅ REPLY RETRIEVAL SYSTEM CREATED SUCCESSFULLY!")
print("=" * 60)

print("\nSaved at:")
print("models/spotify_reply_retrieval.pkl")
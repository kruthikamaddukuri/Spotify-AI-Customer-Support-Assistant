import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity


print("Loading Golden Evaluation Set...")

golden = pd.read_csv(
    "data/golden/final_golden_evaluation_set.csv"
)

print(f"Total examples: {len(golden)}")


print("\nLoading reply retrieval system...")

retrieval_data = joblib.load(
    "models/spotify_reply_retrieval.pkl"
)

vectorizer = retrieval_data["vectorizer"]
message_vectors = retrieval_data["message_vectors"]
historical_data = retrieval_data["data"]

print("✅ Reply retrieval system loaded successfully!")


def evaluate_reply(text, expected_intent):

    # Convert query into TF-IDF vector
    query_vector = vectorizer.transform([text])

    # Calculate similarity with historical messages
    similarities = cosine_similarity(
        query_vector,
        message_vectors
    )[0]

    # Prevent retrieving the exact same message
    normalized_text = str(text).strip().lower()

    for i, historical_text in enumerate(
        historical_data["customer_message"]
    ):

        historical_normalized = (
            str(historical_text).strip().lower()
        )

        if normalized_text == historical_normalized:
            similarities[i] = -1


    # Find best remaining historical example
    best_index = similarities.argmax()

    similarity_score = similarities[best_index]

    historical_row = historical_data.iloc[best_index]

    retrieved_intent = historical_row["intent"]

    intent_match = (
        retrieved_intent == expected_intent
    )

    historical_reply = historical_row[
        "spotify_response"
    ]


    return {
        "retrieved_intent": retrieved_intent,
        "intent_match": intent_match,
        "similarity_score": similarity_score,
        "historical_reply": historical_reply
    }


print("\nEvaluating reply retrieval quality...")

results = []


for index, row in golden.iterrows():

    evaluation = evaluate_reply(
        row["text"],
        row["intent"]
    )

    results.append({

        "text": row["text"],

        "expected_intent": row["intent"],

        "retrieved_intent":
            evaluation["retrieved_intent"],

        "intent_match":
            evaluation["intent_match"],

        "similarity_score":
            evaluation["similarity_score"],

        "historical_reply":
            evaluation["historical_reply"]
    })


results_df = pd.DataFrame(results)


# Intent relevance
intent_relevance = (
    results_df["intent_match"].mean() * 100
)


# Average similarity
average_similarity = (
    results_df["similarity_score"].mean() * 100
)


# Save results
results_df.to_csv(
    "data/golden/reply_quality_results_no_leakage.csv",
    index=False
)


print("\n" + "=" * 65)
print("REPLY RETRIEVAL QUALITY EVALUATION")
print("NO DATA LEAKAGE VERSION")
print("=" * 65)

print(f"\nTotal Examples: {len(results_df)}")

print(
    f"\nReply Intent Relevance: "
    f"{intent_relevance:.2f}%"
)

print(
    f"Average Historical Similarity: "
    f"{average_similarity:.2f}%"
)


print("\n" + "=" * 65)
print("RESULTS SAVED")
print("=" * 65)

print(
    "\n📁 data/golden/"
    "reply_quality_results_no_leakage.csv"
)

print("\n✅ Leakage-free evaluation completed successfully!")
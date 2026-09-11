import joblib
from escalation_policy import decide_action


print("Loading Spotify AI Customer Support Model...")

# Load Intent Classification Model
model = joblib.load("models/spotify_intent_model.pkl")

# Load Reply Retrieval System
retrieval_system = joblib.load(
    "models/spotify_reply_retrieval.pkl"
)

vectorizer = retrieval_system["vectorizer"]
message_vectors = retrieval_system["message_vectors"]
df = retrieval_system["data"]

print("✅ Intent model loaded successfully!")
print("✅ Historical reply retrieval system loaded successfully!")


# ============================================================
# RETRIEVE SIMILAR HISTORICAL SPOTIFY RESPONSE
# ============================================================

from sklearn.metrics.pairwise import cosine_similarity


def get_similar_response(customer_message, predicted_intent):

    # Search only conversations with the predicted intent
    intent_df = df[df["intent"] == predicted_intent]

    if len(intent_df) == 0:
        return None, 0

    indices = intent_df.index.tolist()

    # Convert customer message into TF-IDF vector
    query_vector = vectorizer.transform([customer_message])

    # Get vectors for matching intent
    intent_vectors = message_vectors[indices]

    # Calculate similarity
    similarities = cosine_similarity(
        query_vector,
        intent_vectors
    )[0]

    # Find best matching historical conversation
    best_position = similarities.argmax()

    best_similarity = similarities[best_position]

    best_index = indices[best_position]

    historical_response = df.loc[
        best_index,
        "spotify_response_clean"
    ]

    return historical_response, float(best_similarity)


# ============================================================
# SPOTIFY AI SUPPORT ASSISTANT
# ============================================================

print("\n" + "=" * 65)
print("🎵🤖 SPOTIFY AI CUSTOMER SUPPORT ASSISTANT")
print("=" * 65)

print("\nType 'exit' anytime to close the assistant.\n")


while True:

    message = input("👤 Customer: ")

    if message.lower() == "exit":

        print("\n🤖 Assistant: Thank you for using Spotify AI Support!")
        break


    # ========================================================
    # STEP 1: INTENT CLASSIFICATION
    # ========================================================

    predicted_intent = model.predict([message])[0]

    probabilities = model.predict_proba([message])[0]

    confidence = max(probabilities)


    # ========================================================
    # STEP 2: ESCALATION DECISION
    # ========================================================

    decision = decide_action(
        predicted_intent,
        confidence
    )

    action = decision["action"]

    reason = decision["reason"]


    # ========================================================
    # STEP 3: RETRIEVE HISTORICAL RESPONSE
    # ========================================================

    historical_response, similarity = get_similar_response(
        message,
        predicted_intent
    )


    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    print("\n" + "-" * 65)

    print(f"🔍 Detected Intent: {predicted_intent}")

    print(f"📊 AI Confidence: {confidence * 100:.2f}%")

    print(f"\n🚦 Decision: {action}")

    print(f"\n💡 Reason: {reason}")


    print("\n🤖 Suggested Spotify Support Reply:")

    if historical_response is not None:

        print(historical_response)

        print(
            f"\n📚 Historical similarity: "
            f"{similarity * 100:.2f}%"
        )

    else:

        print(
            "Sorry, we couldn't find a sufficiently "
            "relevant historical support response."
        )


    print("-" * 65 + "\n")
import joblib

print("Loading Spotify Intent Classification Model...")

model = joblib.load("models/spotify_intent_model.pkl")

print("✅ Model loaded successfully!")
print("\n🤖 Spotify Customer Support Intent Classifier")
print("Type 'exit' to stop.\n")

while True:

    message = input("Customer message: ")

    if message.lower() == "exit":
        print("\nThank you! Program closed.")
        break

    prediction = model.predict([message])[0]

    probabilities = model.predict_proba([message])[0]

    confidence = max(probabilities) * 100

    print("\n🎯 Predicted Intent:", prediction)
    print(f"📊 Confidence: {confidence:.2f}%\n")
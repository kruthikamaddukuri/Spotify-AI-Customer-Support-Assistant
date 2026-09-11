import joblib

print("Loading Spotify AI Customer Support Model...")

model = joblib.load("models/spotify_intent_model.pkl")

print("✅ Model loaded successfully!")


# Responses for each customer issue
responses = {

    "Account_Security": """
We understand that account security is very important.

Please reset your password immediately and check whether your email address or account details have been changed. If you still notice unauthorized activity, contact Spotify Support for further assistance.
""",

    "App_Technical": """
Sorry you're experiencing a technical issue.

Please try restarting the Spotify app, updating it to the latest version, or reinstalling it. If the problem continues, please contact Spotify Support.
""",

    "Downloads_Offline": """
We understand you're having trouble with downloads or offline listening.

Please check your internet connection and make sure your Spotify app is updated. You can also try removing and downloading the content again.
""",

    "Family_Student_Plan": """
We can help with your Family or Student Premium plan.

Please check that your account details and eligibility requirements are correct. For Family plans, make sure all members meet the required plan conditions.
""",

    "Feature_Request": """
Thank you for sharing your suggestion!

Your feedback is valuable and can help improve the Spotify experience. We recommend sharing the feature request with the appropriate Spotify feedback channel.
""",

    "Login_Issue": """
Sorry you're having trouble logging in.

Please verify your username and password. You can also try resetting your password or checking whether you're logging in using the correct method, such as email, Facebook, or another connected account.
""",

    "Music_Content": """
We understand you're having an issue related to music or content availability.

Some songs, albums, or artists may be unavailable because of licensing restrictions or regional availability.
""",

    "Payment_Refund": """
Sorry to hear about the payment issue.

Please check your subscription and payment history. If you were charged incorrectly or multiple times, contact Spotify Support with your payment details so they can investigate the issue.
""",

    "Playback_Issue": """
Sorry your music isn't playing properly.

Please try restarting the app and checking your internet connection. You can also try logging out and back in or reinstalling the Spotify application.
""",

    "Premium_Subscription": """
We understand you're experiencing an issue with your Premium subscription.

Please check your subscription status and payment information. If your payment was successful but Premium isn't active, contact Spotify Support for assistance.
"""
}


print("\n" + "=" * 65)
print("🎵🤖 SPOTIFY AI CUSTOMER SUPPORT ASSISTANT")
print("=" * 65)

print("\nType 'exit' anytime to close the assistant.\n")


while True:

    message = input("👤 Customer: ")

    if message.lower() == "exit":
        print("\n🤖 Assistant: Thank you for using Spotify AI Support!")
        break


    # Predict intent
    prediction = model.predict([message])[0]


    # Get confidence score
    probabilities = model.predict_proba([message])[0]

    confidence = max(probabilities) * 100


    print("\n" + "-" * 65)

    print("🔍 Detected Issue:", prediction)

    print(f"📊 AI Confidence: {confidence:.2f}%")

    print("\n🤖 Spotify AI Assistant:")


    # Low confidence handling
    if confidence < 40:

        print("""
I'm not completely sure what issue you're experiencing.

Could you please provide more details about your problem so I can assist you better?
""")

    else:

        print(responses.get(
            prediction,
            "Sorry, I couldn't identify the issue clearly."
        ))


    print("-" * 65 + "\n")
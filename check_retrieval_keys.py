import joblib

print("Loading retrieval system...\n")

data = joblib.load("models/spotify_reply_retrieval.pkl")

print("AVAILABLE KEYS:")

for key in data.keys():
    print("-", key)

print("\nData type:", type(data))
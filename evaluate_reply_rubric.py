import os
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
 
GOLDEN_SET_PATH = "data/golden/final_golden_evaluation_set.csv"
MODEL_PATH = "models/spotify_reply_retrieval.pkl"
OUTPUT_PATH = "data/golden/reply_rubric_evaluation_results.csv"
 
GOOD_THRESHOLD = 0.40
HIGH_THRESHOLD = 0.70
 
MESSAGE_COLUMN_CANDIDATES = ["text", "message", "customer_message", "Message", "Text"]
INTENT_COLUMN_CANDIDATES = ["human_intent", "expected_intent", "intent", "Intent", "human_expected_intent"]
 
if not os.path.exists(GOLDEN_SET_PATH):
    raise FileNotFoundError("Golden evaluation set not found at: " + GOLDEN_SET_PATH)
 
golden_df = pd.read_csv(GOLDEN_SET_PATH)
 
if golden_df.empty:
    raise ValueError("Golden evaluation set at " + GOLDEN_SET_PATH + " is empty.")
 
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Retrieval model pickle not found at: " + MODEL_PATH)
 
retrieval_data = joblib.load(MODEL_PATH)
 
if "vectorizer" not in retrieval_data:
    raise KeyError("Key 'vectorizer' not found in retrieval pickle.")
if "message_vectors" not in retrieval_data:
    raise KeyError("Key 'message_vectors' not found in retrieval pickle.")
if "data" not in retrieval_data:
    raise KeyError("Key 'data' not found in retrieval pickle.")
 
vectorizer = retrieval_data["vectorizer"]
message_vectors = retrieval_data["message_vectors"]
data = retrieval_data["data"]
 
if not isinstance(data, pd.DataFrame):
    data = pd.DataFrame(data)
 
golden_message_col = None
for candidate in MESSAGE_COLUMN_CANDIDATES:
    if candidate in golden_df.columns:
        golden_message_col = candidate
        break
if golden_message_col is None:
    raise ValueError(
        "Could not find a message column in the golden set. Looked for one of: "
        + str(MESSAGE_COLUMN_CANDIDATES)
        + ". Available columns are: "
        + str(list(golden_df.columns))
    )
 
golden_intent_col = None
for candidate in INTENT_COLUMN_CANDIDATES:
    if candidate in golden_df.columns:
        golden_intent_col = candidate
        break
if golden_intent_col is None:
    raise ValueError(
        "Could not find an expected intent column in the golden set. Looked for one of: "
        + str(INTENT_COLUMN_CANDIDATES)
        + ". Available columns are: "
        + str(list(golden_df.columns))
    )
 
historical_message_col = None
for candidate in MESSAGE_COLUMN_CANDIDATES:
    if candidate in data.columns:
        historical_message_col = candidate
        break
if historical_message_col is None:
    raise ValueError(
        "Could not find a message column in the historical data. Looked for one of: "
        + str(MESSAGE_COLUMN_CANDIDATES)
        + ". Available columns are: "
        + str(list(data.columns))
    )
 
historical_intent_col = None
for candidate in INTENT_COLUMN_CANDIDATES:
    if candidate in data.columns:
        historical_intent_col = candidate
        break
if historical_intent_col is None:
    raise ValueError(
        "Could not find an intent column in the historical data. Looked for one of: "
        + str(INTENT_COLUMN_CANDIDATES)
        + ". Available columns are: "
        + str(list(data.columns))
    )
 
print("Golden set message column: '" + golden_message_col + "'")
print("Golden set expected intent column: '" + golden_intent_col + "'")
print("Historical data message column: '" + historical_message_col + "'")
print("Historical data intent column: '" + historical_intent_col + "'")
 
historical_messages_normalized = data[historical_message_col].astype(str).str.strip().str.lower()
 
results = []
 
for idx in range(len(golden_df)):
    row = golden_df.iloc[idx]
    query_text = row[golden_message_col]
    expected_intent = row[golden_intent_col]
 
    query_vector = vectorizer.transform([str(query_text)])
 
    similarities = cosine_similarity(query_vector, message_vectors).flatten()
 
    normalized_query = str(query_text).strip().lower()
    leakage_mask = (historical_messages_normalized == normalized_query).to_numpy()
 
    masked_similarities = similarities.copy()
    masked_similarities[leakage_mask] = -1.0
 
    if np.all(masked_similarities < 0):
        retrieved_message = None
        retrieved_intent = None
        best_similarity = 0.0
    else:
        best_index = int(np.argmax(masked_similarities))
        best_similarity = float(masked_similarities[best_index])
        best_row = data.iloc[best_index]
        retrieved_message = best_row[historical_message_col]
        retrieved_intent = best_row[historical_intent_col]
 
    if retrieved_intent is not None:
        intent_match = str(retrieved_intent).strip().lower() == str(expected_intent).strip().lower()
    else:
        intent_match = False
 
    if intent_match and best_similarity >= GOOD_THRESHOLD:
        rubric = "GOOD"
    elif intent_match and best_similarity < GOOD_THRESHOLD:
        rubric = "PARTIAL"
    else:
        rubric = "POOR"
 
    if best_similarity >= HIGH_THRESHOLD:
        similarity_rubric_score = 3
    elif best_similarity >= GOOD_THRESHOLD:
        similarity_rubric_score = 2
    else:
        similarity_rubric_score = 1
 
    result_row = row.to_dict()
    result_row["retrieved_message"] = retrieved_message
    result_row["retrieved_intent"] = retrieved_intent
    result_row["similarity_score_raw"] = round(best_similarity, 4)
    result_row["intent_match"] = intent_match
    result_row["rubric"] = rubric
    result_row["similarity_rubric_score"] = similarity_rubric_score
 
    results.append(result_row)
 
results_df = pd.DataFrame(results)
 
total_examples = len(results_df)
good_count = int((results_df["rubric"] == "GOOD").sum())
partial_count = int((results_df["rubric"] == "PARTIAL").sum())
poor_count = int((results_df["rubric"] == "POOR").sum())
 
if total_examples > 0:
    intent_relevance_pct = (results_df["intent_match"].sum() / total_examples) * 100
    avg_similarity_rubric_score = results_df["similarity_rubric_score"].mean()
else:
    intent_relevance_pct = 0.0
    avg_similarity_rubric_score = 0.0
 
print("")
print("=" * 50)
print("REPLY RETRIEVAL RUBRIC EVALUATION SUMMARY")
print("=" * 50)
print("Total Examples: " + str(total_examples))
print("Intent Relevance: {:.2f}%".format(intent_relevance_pct))
print("Average Similarity Rubric Score: {:.2f} / 3".format(avg_similarity_rubric_score))
print("GOOD results: " + str(good_count))
print("PARTIAL results: " + str(partial_count))
print("POOR results: " + str(poor_count))
print("=" * 50)
 
output_dir = os.path.dirname(OUTPUT_PATH)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)
 
results_df.to_csv(OUTPUT_PATH, index=False)
 
print("")
print("Detailed results saved to: " + OUTPUT_PATH)
 


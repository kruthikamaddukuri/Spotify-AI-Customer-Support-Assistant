# 🎵 Spotify AI Customer Support Assistant

An AI-powered customer support system that uses Natural Language Processing (NLP), Machine Learning, confidence-based decision-making, escalation policies, and historical reply retrieval to assist with Spotify customer support queries.

The system analyzes a customer's message, identifies the underlying support intent, measures prediction confidence, decides whether the issue can be automatically handled or should be escalated to a human agent, and retrieves a relevant historical support response.

---

## 📌 Project Overview

Customer support teams receive a large number of messages covering technical issues, login problems, payment concerns, subscription questions, and account security issues.

This project demonstrates an AI-powered customer support workflow that can:

* Automatically classify customer support messages
* Predict customer intent using Machine Learning
* Calculate prediction confidence
* Apply an escalation policy for sensitive or high-risk issues
* Automatically handle common support requests
* Escalate sensitive issues to a human agent
* Retrieve relevant historical support responses
* Evaluate the system using a manually reviewed Golden Evaluation Set

---

## 🚀 Key Features

* 🤖 Automatic customer intent classification
* 🧠 NLP-based text processing
* 📊 TF-IDF feature extraction
* 🤖 Logistic Regression Machine Learning model
* 🎯 Intent prediction with confidence scores
* 🚦 Confidence-based escalation decisions
* ⚠️ High-risk issue detection
* 💬 Historical reply retrieval using similarity search
* 🧑‍💻 Interactive terminal-based customer support assistant
* 📊 Golden Set evaluation
* 📈 Baseline model comparison
* 🔍 No-data-leakage reply retrieval evaluation
* ⭐ Reply quality rubric evaluation

---

# 🏷️ Intent Categories

The model can identify the following customer support issues:

1. Account Security
2. App Technical
3. Downloads and Offline
4. Family and Student Plan
5. Feature Request
6. Login Issue
7. Music Content
8. Payment and Refund
9. Playback Issue
10. Premium Subscription

---

# 📊 Dataset

The project uses Spotify-related customer support conversations extracted from a public Twitter customer support dataset.

### Dataset Processing

The dataset was processed to create useful Machine Learning examples.

The processing workflow includes:

* Extracting Spotify-related customer support conversations
* Creating customer and support response pairs
* Cleaning and preprocessing text
* Filtering useful customer messages
* Assigning support intent categories
* Preparing data for Machine Learning training

### Available Labeled Examples

**4,131 labeled examples** were available for Golden Set sampling and evaluation.

---

# 🧠 Machine Learning Approach

The intent classification system uses:

### TF-IDF Vectorization

Customer messages are converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

### Logistic Regression

A **Logistic Regression classifier** is used to predict the customer support intent.

### Confidence Scores

The model calculates prediction probabilities to determine how confident the AI system is about its prediction.

---

# 🏗️ System Architecture

```text
Customer Message
       ↓
Text Preprocessing
       ↓
TF-IDF Feature Extraction
       ↓
Logistic Regression Model
       ↓
Intent Prediction + Confidence Score
       ↓
Escalation Policy
       ↓
 ┌─────────────────────────────┐
 │                             │
 ↓                             ↓
AUTO_HANDLE              ESCALATE_TO_HUMAN
 │                             │
 ↓                             ↓
Retrieve Relevant         Human Support
Historical Reply          Review
 │
 ↓
Suggested Support Response
```

---

# 🚦 Escalation Policy

The project includes a rule-based escalation policy that determines whether a customer issue should be automatically handled or escalated to a human agent.

### Low Confidence

If the AI model has low confidence in its prediction, the issue is escalated to a human agent.

### High-Risk Intents

The following categories are treated as high-risk:

* Account Security
* Payment and Refund

These issues may involve sensitive information, account verification, unauthorized access, or financial concerns.

### Common Support Issues

Common and lower-risk issues can be automatically handled using standard support responses.

Examples include:

* App technical problems
* Login issues
* Playback problems
* Downloads and offline issues
* Feature requests
* Music content questions

---

# 💬 Reply Retrieval System

Instead of generating completely new responses, the system can retrieve relevant historical Spotify support responses.

The retrieval system uses:

* TF-IDF vectorization
* Customer message vectors
* Cosine similarity

### Retrieval Workflow

```text
Customer Message
       ↓
Convert Message to TF-IDF Vector
       ↓
Compare with Historical Messages
       ↓
Cosine Similarity
       ↓
Find Most Similar Conversation
       ↓
Retrieve Historical Support Reply
```

This approach helps provide responses based on historically relevant customer support conversations.

---

# 📊 Golden Evaluation Set

A separate **Golden Evaluation Set** was created to evaluate the system more reliably.

### Golden Set Creation Process

1. A balanced sample was created from the labeled dataset.
2. Initially, 20 examples were selected from each of the 10 intent categories.
3. This created a dataset containing **200 evaluation examples**.
4. The examples were manually reviewed.
5. Human reviewers could approve or correct:

   * Intent labels
   * Expected actions
6. The reviewed data was used to create the final Golden Evaluation Set.

### Final Golden Set

🎯 **Total Examples: 200**

The final Golden Set contains manually reviewed customer support examples and expected outcomes.

---

# 📈 Intent Classification Evaluation

The trained Machine Learning model was evaluated using the Golden Evaluation Set.

### Results

| Metric                     |     Result |
| -------------------------- | ---------: |
| Total Examples             |        200 |
| Correct Intent Predictions |        170 |
| Intent Accuracy            | **85.00%** |

This evaluation provides an independent assessment of the model using the manually reviewed Golden Set.

---

# 📊 Baseline Comparison

The Machine Learning model was compared against simpler baseline approaches.

| Model                  |   Accuracy |
| ---------------------- | ---------: |
| Trivial Baseline       |     12.50% |
| Keyword-Based Baseline |     80.00% |
| Our ML Model           | **85.00%** |

### Interpretation

The Logistic Regression Machine Learning model outperformed both:

* A trivial baseline that always predicts the same intent
* A keyword-based rule system

This demonstrates that the Machine Learning approach provides improved intent classification performance.

---

# 🚦 Action / Escalation Evaluation

The escalation policy was evaluated using the Golden Evaluation Set.

### Results

| Metric                     |     Result |
| -------------------------- | ---------: |
| Total Examples             |        200 |
| Correct Action Predictions |        144 |
| Action Accuracy            | **72.00%** |

The action evaluation measures whether the system correctly decides between:

* `AUTO_HANDLE`
* `ESCALATE_TO_HUMAN`

---

# 🔍 Reply Retrieval Evaluation

The reply retrieval system was evaluated using the Golden Evaluation Set.

### No-Data-Leakage Evaluation

To avoid unfair evaluation, exact matching customer messages were excluded from the historical retrieval candidates.

### Results

| Metric                        |     Result |
| ----------------------------- | ---------: |
| Total Examples                |        200 |
| Reply Intent Relevance        | **85.50%** |
| Average Historical Similarity | **98.80%** |

---

# ⭐ Reply Quality Rubric Evaluation

A rubric-based evaluation was also performed to assess the quality of retrieved historical conversations.

### Quality Categories

#### GOOD

The retrieved intent matches the expected intent and the similarity score is at least 0.40.

#### PARTIAL

The retrieved intent matches the expected intent, but similarity is below 0.40.

#### POOR

The retrieved intent does not match the expected intent.

### Similarity Rubric

| Similarity        | Score |
| ----------------- | ----: |
| ≥ 0.70            |     3 |
| ≥ 0.40 and < 0.70 |     2 |
| < 0.40            |     1 |

### Results

| Metric                          |       Result |
| ------------------------------- | -----------: |
| Total Examples                  |          200 |
| Intent Relevance                |   **85.50%** |
| Average Similarity Rubric Score | **2.97 / 3** |
| GOOD Results                    |      **168** |
| PARTIAL Results                 |        **3** |
| POOR Results                    |       **29** |

---

# 🖥️ Running the Customer Support Assistant

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the customer support assistant:

```bash
python customer_support_bot.py
```

Example:

```text
👤 Customer: My Spotify account was hacked and someone changed my email.

🔍 Detected Intent: Account_Security
📊 AI Confidence: 98.71%

🚦 Decision: ESCALATE_TO_HUMAN

💡 Reason: This issue belongs to Account_Security and may require account-specific verification or sensitive information.

🤖 Suggested Spotify Support Reply:
[Retrieved historical support response]
```

Type:

```text
exit
```

to close the assistant.

---

# 📁 Project Structure

```text
Spotify-AI-Customer-Support-Assistant/
│
├── data/
│   └── golden/
│       ├── final_golden_evaluation_set.csv
│       ├── evaluation_results.csv
│       ├── baseline_comparison.csv
│       ├── reply_quality_results.csv
│       ├── reply_quality_results_no_leakage.csv
│       └── reply_rubric_evaluation_results.csv
│
├── models/
│   ├── spotify_intent_model.pkl
│   └── spotify_reply_retrieval.pkl
│
├── customer_support_bot.py
├── escalation_policy.py
├── reply_retrieval.py
├── evaluate_golden_set.py
├── evaluate_baselines.py
├── evaluate_reply_quality.py
├── evaluate_reply_rubric.py
│
├── create_balanced_golden_set.py
├── prepare_manual_review.py
├── check_reviewed_golden_set.py
├── create_final_golden_set.py
│
└── README.md
```

---

# 🔬 Evaluation Methodology

The project uses multiple evaluation approaches:

### 1. Intent Classification Evaluation

Measures whether the Machine Learning model predicts the correct customer support intent.

### 2. Baseline Comparison

Compares the ML model against simpler baseline approaches.

### 3. Action Evaluation

Measures whether the escalation policy correctly selects:

* AUTO_HANDLE
* ESCALATE_TO_HUMAN

### 4. Reply Retrieval Evaluation

Measures whether the retrieval system finds historically relevant conversations.

### 5. No-Data-Leakage Evaluation

Exact matching messages are excluded to prevent the retrieval system from simply returning the same example.

### 6. Reply Quality Rubric

Retrieved results are categorized as:

* GOOD
* PARTIAL
* POOR

based on intent relevance and similarity.

---

# 🎯 Key Results

🏆 **Intent Classification Accuracy:** 85.00%

📈 **Keyword Baseline Accuracy:** 80.00%

🤖 **ML Model Accuracy:** 85.00%

🚦 **Action Accuracy:** 72.00%

💬 **Reply Intent Relevance:** 85.50%

⭐ **Average Reply Rubric Score:** 2.97 / 3

---

# 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Natural Language Processing
* TF-IDF Vectorization
* Logistic Regression
* Cosine Similarity
* Git and GitHub

---

# 🔮 Future Improvements

Possible future improvements include:

* Using transformer-based language models for intent classification
* Improving the escalation policy using more contextual signals
* Adding sentiment and urgency detection
* Building a web-based user interface
* Adding a database for conversation history
* Supporting real-time human agent handoff
* Using semantic embeddings for improved reply retrieval
* Adding more manually reviewed evaluation examples

---

# 📌 Conclusion

This project demonstrates a complete AI-powered customer support workflow using Machine Learning and NLP.

The system performs customer intent classification, confidence estimation, escalation decision-making, and historical reply retrieval. The system was evaluated using a manually reviewed Golden Evaluation Set and compared against baseline approaches.

The results demonstrate that the Machine Learning model performs better than the tested baseline approaches and that the reply retrieval system can retrieve historically relevant support conversations.

---

## 👩‍💻 Author

**Kruthikaa Maddukuri**

B.Tech – Computer Science Engineering
Specialization: Artificial Intelligence and Machine Learning

---

⭐ If you found this project interesting, feel free to explore the repository!

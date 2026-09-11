# 🎵 Spotify AI Customer Support Assistant

An AI-powered customer support system that uses Natural Language Processing (NLP), Machine Learning, confidence-based decision-making, escalation policies, and historical reply retrieval to assist with Spotify customer support queries.

The system analyzes a customer's message, identifies the underlying support intent, measures prediction confidence, decides whether the issue can be automatically handled or should be escalated to a human agent, and retrieves a relevant historical support response.

---

# ⚡ Quick Start — Reproduce the Project

## 1. Clone the Repository

```bash
git clone https://github.com/kruthikamaddukuri/Spotify-AI-Customer-Support-Assistant.git
cd Spotify-AI-Customer-Support-Assistant
```

## 2. Create and Activate a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

## 4. Run the AI Customer Support Assistant

```powershell
python customer_support_bot.py
```

Example message:

```text
I paid for Spotify Premium but my account still shows Free.
```

The system will:

1. Classify the customer's intent.
2. Calculate the model confidence.
3. Decide whether to auto-handle or escalate.
4. Retrieve a historically grounded Spotify support reply.
5. Display the retrieval similarity score.

## 5. Reproduce the Evaluation Results

Run the following commands:

```powershell
python evaluate_golden_set.py
python evaluate_baselines.py
python evaluate_reply_quality.py
python evaluate_reply_rubric.py
python test_escalation.py
```

Additional evaluation and analysis commands:

```powershell
python analyze_failures.py
python show_failure_examples.py
python calculate_human_llm_agreement.py
python calculate_independent_agreement.py
```

## Expected Headline Results

| Metric                         |       Result |
| ------------------------------ | -----------: |
| Intent Classification Accuracy |   **85.00%** |
| Keyword Baseline Accuracy      |   **80.00%** |
| Action Accuracy                |   **72.00%** |
| Reply Intent Relevance         |   **85.50%** |
| Average Reply Rubric Score     | **2.97 / 3** |

---

# 📌 Project Overview

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

# 🚀 Key Features

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
* 🔎 Failure analysis
* 🧑 Human and LLM judge agreement analysis

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

## Dataset Processing

The dataset was processed to create useful Machine Learning examples.

The processing workflow includes:

* Extracting Spotify-related customer support conversations
* Creating customer and support response pairs
* Cleaning and preprocessing text
* Filtering useful customer messages
* Assigning support intent categories
* Preparing data for Machine Learning training

## Available Labeled Examples

**4,131 labeled examples** were available for Golden Set sampling and evaluation.

---

# 🧠 Machine Learning Approach

The intent classification system uses:

## TF-IDF Vectorization

Customer messages are converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

## Logistic Regression

A **Logistic Regression classifier** is used to predict the customer support intent.

## Confidence Scores

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

## Low Confidence

If the AI model has low confidence in its prediction, the issue is escalated to a human agent.

## High-Risk Intents

The following categories are treated as high-risk:

* Account Security
* Payment and Refund

These issues may involve sensitive information, account verification, unauthorized access, or financial concerns.

## Common Support Issues

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

Instead of generating completely new responses, the system retrieves relevant historical Spotify support responses.

The retrieval system uses:

* TF-IDF vectorization
* Customer message vectors
* Cosine similarity

## Retrieval Workflow

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

## Golden Set Creation Process

1. A balanced sample was created from the labeled dataset.
2. Initially, 20 examples were selected from each of the 10 intent categories.
3. This created a dataset containing **200 evaluation examples**.
4. The examples were manually reviewed.
5. Human reviewers could approve or correct:

   * Intent labels
   * Expected actions
6. The reviewed data was used to create the final Golden Evaluation Set.

## Final Golden Set

🎯 **Total Examples: 200**

The final Golden Set contains manually reviewed customer support examples and expected outcomes.

---

# 📈 Intent Classification Evaluation

The trained Machine Learning model was evaluated using the Golden Evaluation Set.

## Results

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

## Interpretation

The Logistic Regression Machine Learning model outperformed both:

* A trivial baseline that always predicts the same intent
* A keyword-based rule system

This demonstrates that the Machine Learning approach provides improved intent classification performance.

---

# 🚦 Action / Escalation Evaluation

The escalation policy was evaluated using the Golden Evaluation Set.

## Results

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

## No-Data-Leakage Evaluation

To avoid unfair evaluation, exact matching customer messages were excluded from the historical retrieval candidates.

## Results

| Metric                        |     Result |
| ----------------------------- | ---------: |
| Total Examples                |        200 |
| Reply Intent Relevance        | **85.50%** |
| Average Historical Similarity | **98.80%** |

---

# ⭐ Reply Quality Rubric Evaluation

A rubric-based evaluation was also performed to assess the quality of retrieved historical conversations.

## Quality Categories

### GOOD

The retrieved intent matches the expected intent and the similarity score is at least 0.40.

### PARTIAL

The retrieved intent matches the expected intent, but similarity is below 0.40.

### POOR

The retrieved intent does not match the expected intent.

## Similarity Rubric

| Similarity        | Score |
| ----------------- | ----: |
| ≥ 0.70            |     3 |
| ≥ 0.40 and < 0.70 |     2 |
| < 0.40            |     1 |

## Results

| Metric                          |       Result |
| ------------------------------- | -----------: |
| Total Examples                  |          200 |
| Intent Relevance                |   **85.50%** |
| Average Similarity Rubric Score | **2.97 / 3** |
| GOOD Results                    |      **168** |
| PARTIAL Results                 |        **3** |
| POOR Results                    |       **29** |

---

# 🧑‍⚖️ Independent Human vs LLM Judge Agreement

To avoid relying only on labels that may have been influenced by the same evaluation logic, an additional independent human evaluation was conducted on a sample of **30 support replies**.

The human reviewer independently labelled each reply as:

* `GOOD`
* `PARTIAL`
* `POOR`

These labels were then compared with the Claude LLM judge results.

## Results

| Metric          |     Result |
| --------------- | ---------: |
| Total Examples  |         30 |
| Exact Agreement | **40.00%** |
| Cohen's Kappa   |  **0.056** |

### Confusion Matrix

Rows represent the independent human labels, while columns represent the Claude LLM judge labels.

| Human \ Claude | GOOD | PARTIAL | POOR |
| -------------- | ---: | ------: | ---: |
| GOOD           |    9 |       3 |    0 |
| PARTIAL        |    6 |       1 |    3 |
| POOR           |    4 |       2 |    2 |

## Interpretation

The relatively low agreement shows that reply quality is subjective and that an LLM judge should not be treated as a perfect replacement for human evaluation.

This is an important limitation of the evaluation. While automated evaluation can provide useful signals, stronger conclusions would require more independent human reviewers and a larger evaluation sample.

---

# 🔎 Failure Analysis

The Golden Set evaluation produced **30 incorrect intent predictions out of 200 examples**.

The most common confusion patterns were:

| Expected Intent       | Predicted Intent     | Cases |
| --------------------- | -------------------- | ----: |
| Music Content         | Feature Request      |     8 |
| Family / Student Plan | Premium Subscription |     4 |
| Feature Request       | Music Content        |     4 |
| App Technical         | Music Content        |     3 |
| Feature Request       | Downloads / Offline  |     3 |

## Key Failure Patterns

### 1. Music Content vs Feature Request

The model sometimes struggles to distinguish between:

* Requests to add specific songs, artists, or albums
* Requests for completely new Spotify features

For example, asking Spotify to add a particular song may be incorrectly interpreted as a feature request.

### 2. Subscription-Related Intent Overlap

Messages involving Premium, Family plans, Student plans, payments, or account activation can contain overlapping vocabulary.

This can lead to confusion between:

* Family / Student Plan
* Premium Subscription
* Payment and Refund

### 3. Feature Requests Containing Music Vocabulary

Feature requests may contain words such as:

* Song
* Music
* Offline
* Download

Because TF-IDF relies heavily on vocabulary patterns, these messages can sometimes be classified as Music Content or Downloads / Offline.

### 4. Technical Issues Mentioning Music

Some technical problems include words related to songs, queues, advertisements, or downloads.

This can cause confusion between:

* App Technical
* Music Content

### 5. High-Confidence Errors

Confidence does not always mean correctness.

One example, **“Please add Again-Bruno Mars”**, was incorrectly classified with approximately **99.7% confidence**.

This demonstrates that prediction confidence should be treated as one signal rather than proof that a prediction is correct.

---

# 🖥️ Running the Customer Support Assistant

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate
```

Run the customer support assistant:

```powershell
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
│       ├── reply_rubric_evaluation_results.csv
│       ├── blind_llm_judge_sample.csv
│       ├── human_review_sample.csv
│       ├── llm_judge_results.csv
│       ├── human_llm_agreement_results.csv
│       ├── failure_analysis_predictions.csv
│       └── top_failure_examples.csv
│
├── models/
│   ├── spotify_intent_model.pkl
│   └── spotify_reply_retrieval.pkl
│
├── customer_support_bot.py
├── escalation_policy.py
├── reply_retrieval.py
│
├── evaluate_golden_set.py
├── evaluate_baselines.py
├── evaluate_reply_quality.py
├── evaluate_reply_rubric.py
├── test_escalation.py
│
├── analyze_failures.py
├── show_failure_examples.py
├── create_human_review_file.py
├── create_human_labels.py
├── create_llm_judge_sample.py
├── create_llm_judge_results.py
├── create_blind_llm_judge_file.py
├── calculate_human_llm_agreement.py
├── calculate_independent_agreement.py
│
├── requirements.txt
└── README.md
```

---

# 🔬 Evaluation Methodology

The project uses multiple evaluation approaches.

## 1. Intent Classification Evaluation

Measures whether the Machine Learning model predicts the correct customer support intent.

## 2. Baseline Comparison

Compares the ML model against simpler baseline approaches.

## 3. Action Evaluation

Measures whether the escalation policy correctly selects:

* `AUTO_HANDLE`
* `ESCALATE_TO_HUMAN`

## 4. Reply Retrieval Evaluation

Measures whether the retrieval system finds historically relevant conversations.

## 5. No-Data-Leakage Evaluation

Exact matching messages are excluded to prevent the retrieval system from simply returning the same example.

## 6. Reply Quality Rubric

Retrieved results are categorized as:

* GOOD
* PARTIAL
* POOR

based on intent relevance and similarity.

## 7. Independent Human vs LLM Agreement

Independent human labels are compared against LLM judge labels using:

* Exact agreement
* Cohen's Kappa
* Confusion matrix analysis

This helps measure how closely automated evaluation aligns with independent human judgement.

## 8. Failure Analysis

Incorrect predictions are analyzed to identify common confusion patterns between intent categories.

---

# 🎯 Key Results

🏆 **Intent Classification Accuracy:** 85.00%

📈 **Keyword Baseline Accuracy:** 80.00%

🚦 **Action Accuracy:** 72.00%

💬 **Reply Intent Relevance:** 85.50%

⭐ **Average Reply Rubric Score:** 2.97 / 3

🔎 **Incorrect Intent Predictions:** 30 / 200

🧑‍⚖️ **Independent Human vs Claude Agreement:** 40.00%

📊 **Independent Human vs Claude Cohen's Kappa:** 0.056

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
* Git
* GitHub

---

# 📌 What Is Misleading About My Headline Number?

A headline accuracy number can make the system appear more reliable than it actually is.

The Golden Evaluation Set shows that the model achieved **85.00% intent accuracy**, which means it still made **30 incorrect intent predictions out of 200 examples (15%)**.

First, accuracy does not show which mistakes the model makes. Some mistakes occurred between closely related intents where vocabulary overlaps.

For example, the model frequently confused **Music Content requests with Feature Requests**. A message asking Spotify to add a specific song could be incorrectly interpreted as a request for a new product feature. Similarly, Feature Requests mentioning words such as *offline*, *downloaded*, *song*, or *music* could be classified into Downloads / Offline or Music Content instead.

Second, the model's confidence can sometimes be misleading. Some incorrect predictions received relatively high confidence scores. For example, the request **“Please add Again-Bruno Mars”** was classified incorrectly with approximately **99.7% confidence**.

This means confidence should not automatically be interpreted as correctness.

Third, intent classification accuracy does not fully measure the quality of the complete support agent. A correct intent prediction does not guarantee that the retrieved historical reply is relevant or helpful.

Fourth, the independent human vs LLM judge evaluation showed only **40.00% exact agreement** and a **Cohen's Kappa of 0.056** on the 30-example sample. This demonstrates that reply quality evaluation is subjective and that automated LLM evaluation should not be treated as a perfect substitute for independent human judgement.

Finally, the evaluation dataset contains **200 hand-reviewed examples**, while the independent human evaluation contains **30 examples**. These evaluations provide useful evidence but may not represent every possible type of Spotify customer message.

Therefore, the reported metrics should be treated as useful indicators of specific parts of the system rather than proof that the complete support agent is equally reliable in every situation.

A complete evaluation should consider:

* Intent accuracy
* Escalation decisions
* Reply relevance
* Failure analysis
* Human evaluation
* Agreement between human and automated judges

---

# 🔮 What I'd Do Next With One More Week

With one additional week, I would focus on improving the reliability of the complete support agent rather than simply trying to increase the intent-classification accuracy.

## 1. Improve Intent Classification

The failure analysis shows that the TF-IDF + Logistic Regression model struggles when different intents share similar vocabulary.

I would experiment with sentence embeddings or transformer-based models to better capture the meaning and context of customer messages.

## 2. Improve Retrieval Quality

The current system retrieves historical replies based primarily on message similarity.

I would introduce intent-aware retrieval, where replies are retrieved only from examples with the same predicted intent. This could reduce irrelevant responses caused by retrieving messages from different issue categories.

## 3. Improve Escalation Decisions

I would evaluate the escalation policy separately using more difficult and ambiguous examples.

The policy could combine:

* Model confidence
* Intent ambiguity
* Message risk
* Retrieval similarity

instead of relying on a single signal.

## 4. Collect More Human Evaluations

I would expand the human evaluation sample and have multiple independent reviewers label the same examples.

This would provide a more reliable measurement of reply quality and allow stronger evaluation of agreement between human reviewers and the LLM judge.

## 5. Add Better End-to-End Evaluation

I would evaluate the complete pipeline using realistic customer messages and measure whether the final action was correct:

* Correct intent
* Appropriate escalation decision
* Useful response

This would provide a more meaningful measure of agent reliability than intent accuracy alone.

## 6. Improve Reproducibility and Usability

Finally, I would package the pipeline into a cleaner command-line workflow, reduce intermediate files, and add automated tests so the complete system could be reproduced and evaluated more easily.

---

# 📝 Decision Log

The following decisions were made during the development of this project.

## 1. Chosen Brand: Spotify

Spotify was selected because the dataset contained enough customer-support conversations to build a meaningful intent classification and reply retrieval system across multiple types of customer issues.

## 2. Defined 10 Intent Categories

Instead of creating too many highly specific classes, similar customer problems were grouped into 10 practical support intents.

This created a balance between:

* Coverage of common support issues
* Having enough examples per category

## 3. Used the Twitter Customer Support Dataset as the Primary Source

The goal was to work with noisy, real-world customer conversations rather than a perfectly clean benchmark dataset.

This made the classification problem closer to realistic customer support scenarios.

## 4. Used TF-IDF for Text Representation

TF-IDF was selected because it is:

* Lightweight
* Fast to train
* Interpretable
* Effective for sparse text features
* A strong baseline for a relatively small text-classification problem

## 5. Used Logistic Regression for Intent Classification

Logistic Regression was chosen because it works well with sparse TF-IDF features and provides probability estimates.

These probability estimates were useful for the confidence-based escalation policy.

## 6. Used Historical Reply Retrieval Instead of Fully Generative Responses

The system retrieves historically relevant support replies instead of generating unrestricted responses.

This approach provides a more grounded prototype and reduces the risk of unsupported or fabricated support information.

## 7. Added a Confidence-Based Escalation Policy

Not every customer issue should be automatically handled.

Low-confidence predictions and high-risk categories can be escalated to a human agent.

This decision reflects the importance of human oversight in sensitive customer support situations.

## 8. Treated Account Security and Payment Issues as High Risk

Account Security and Payment / Refund issues may involve:

* Sensitive information
* Account verification
* Unauthorized access
* Financial concerns

For this reason, these categories receive more cautious handling.

## 9. Created a Separate Golden Evaluation Set

A separate manually reviewed Golden Set was used to evaluate the system beyond the standard train-test split.

This provides a more realistic estimate of performance on independently reviewed examples.

## 10. Added Failure Analysis

Accuracy alone does not explain where the model fails.

Failure analysis was added to identify recurring confusion patterns and guide future improvements.

## 11. Added Independent Human vs LLM Agreement Analysis

Automated LLM evaluation can be useful, but it should not automatically be assumed to represent human judgement.

An independent human evaluation was therefore compared with the Claude LLM judge to measure agreement and highlight the limitations of automated quality evaluation.

---

# 📌 Conclusion

This project demonstrates a complete AI-powered customer support workflow using Machine Learning and NLP.

The system performs:

* Customer intent classification
* Confidence estimation
* Escalation decision-making
* Historical reply retrieval
* Golden Set evaluation
* Baseline comparison
* Reply quality evaluation
* Failure analysis
* Human vs LLM agreement analysis

The Golden Set evaluation achieved **85.00% intent classification accuracy**, outperforming the tested **80.00% keyword-based baseline**.

However, the evaluation also identified important limitations. The system made **30 incorrect predictions out of 200 examples**, confidence could sometimes be misleading, and independent human evaluation showed limited agreement with the automated LLM judge.

These findings demonstrate that building a reliable AI support system requires evaluating more than a single accuracy metric.

The project therefore focuses not only on model performance, but also on:

* Failure patterns
* Escalation reliability
* Reply relevance
* Human evaluation
* Limitations of automated evaluation

---

# 👩‍💻 Author

**Kruthikaa Maddukuri**

B.Tech – Computer Science Engineering
Specialization: Artificial Intelligence and Machine Learning

---

⭐ If you found this project interesting, feel free to explore the repository!

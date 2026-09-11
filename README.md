# 🎵 Spotify AI Customer Support Assistant

An AI-powered customer support system that automatically identifies customer issues from Spotify support messages and provides appropriate responses.

## 📌 Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to classify customer support messages into different issue categories.

The system analyzes a customer's message, predicts the customer's intent, calculates the confidence score, and provides an appropriate support response.

## 🚀 Features

- 🤖 Automatic customer intent classification
- 🧠 NLP-based text processing
- 📊 TF-IDF feature extraction
- 🤖 Logistic Regression Machine Learning model
- 🎯 Intent prediction with confidence scores
- ⚠️ Low-confidence detection
- 💬 Automated customer support responses
- 🖥️ Interactive terminal-based chatbot

## 🏷️ Intent Categories

The model can identify the following customer issues:

1. Account Security
2. App Technical Issues
3. Downloads and Offline Issues
4. Family and Student Plans
5. Feature Requests
6. Login Issues
7. Music Content Issues
8. Payment and Refund Issues
9. Playback Issues
10. Premium Subscription Issues

## 📊 Dataset

The project uses customer support conversations extracted from a public Twitter customer support dataset.

### Dataset Processing

- Original dataset: 2.8 million tweets
- Spotify customer support conversations extracted
- Customer and support response pairs created
- Text cleaned and preprocessed
- Useful messages filtered
- Final ML training examples: 4,014

## 🧠 Machine Learning Approach

The project uses:

- **TF-IDF Vectorization** for converting text into numerical features
- **Logistic Regression** for intent classification
- **Train-Test Split** for model evaluation

### Model Performance

🎯 **Test Accuracy: 95.52%**

> Note: The accuracy was measured on a held-out test split of the prepared dataset.

## 🏗️ Project Workflow

```text
Customer Message
       ↓
Text Preprocessing
       ↓
TF-IDF Feature Extraction
       ↓
Logistic Regression Model
       ↓
Intent Classification
       ↓
Confidence Score
       ↓
Customer Support Response
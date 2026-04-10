# itv_reviews_prediction


# GUI APP

# 🍽️ Restaurant Review Analysis System

A Python-based desktop application that uses **Natural Language Processing (NLP)** to analyze customer feedback. The system classifies reviews as Positive or Negative using a **BERT/LSTM** model and provides real-time statistical visualization for restaurant owners.

## 🚀 Features
*   **Customer Review Portal**: Interactive GUI for customers to select food items and submit text reviews.
*   **Sentiment Analysis**: Uses **BERT** (Transformers) or **LSTM** to accurately predict the sentiment of the review.
*   **Owner Dashboard**: Secure login system (`abc` / `12345`) to view data.
*   **Real-time Analytics**: Displays review counts and generates **Pie Charts** using Matplotlib.
*   **Database Integration**: Stores food-specific ratings (Good/Bad/Total) in a MySQL database.

## 🛠️ Tech Stack
*   **GUI**: [Tkinter](https://python.org)
*   **NLP Models**: [Hugging Face Transformers (BERT)](https://huggingface.co), [TensorFlow/Keras (LSTM)](https://tensorflow.org)
*   **Database**: MySQL ([PyMySQL](https://readthedocs.io))
*   **Visualization**: [Matplotlib](https://matplotlib.org)
*   **Language**: Python 3.x

## 📋 Prerequisites
Ensure you have the following installed:
*   **MySQL Server**
*   **Python Libraries**:
    ```bash
    pip install torch transformers tensorflow keras pymysql matplotlib
    ```

## ⚙️ Database Configuration
1. Create a database named `rest_review_db`.
2. Create the `reviews_table` with this schema:
   ```sql
   CREATE TABLE reviews_table (
       food VARCHAR(100) PRIMARY KEY,
       good_review INT DEFAULT 0,
       bad_review INT DEFAULT 0,
       customer INT DEFAULT 0
   );


# FLASK APP

# 🍽️ Restaurant Review Analysis System

A dual-interface sentiment analysis platform that utilizes **BERT** and **LSTM** deep learning models to predict customer satisfaction. This project features a **Flask Web Application** for quick predictions and a **Tkinter Desktop Application** for restaurant management and data visualization.

## 🌟 Key Features
- **Hybrid NLP Engine**: Supports both high-performance **BERT** (Transformers) and efficient **LSTM** (Keras) models.
- **Web Interface (Flask)**: A lightweight web portal for instant review sentiment prediction.
- **Admin Desktop Portal (Tkinter)**: 
    - Secure Owner Login (`abc` / `12345`).
    - Menu-specific review tracking (Idly, Biryani, etc.).
    - Interactive **Pie Charts** for statistical analysis.
- **Database Integration**: Real-time MySQL logging of customer feedback and food performance.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Deep Learning** | PyTorch (BERT), TensorFlow/Keras (LSTM) |
| **Web Framework** | Flask |
| **GUI Framework** | Tkinter |
| **Database** | MySQL (PyMySQL) |
| **Visualization** | Matplotlib |

## requirements.txt
pandas
tensorflow
matplotlib
seaborn
scikit-learn
flask
nltk
pymysql
cryptography
torch
transformers
torchvision -->
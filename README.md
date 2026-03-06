# 🛒 Amazon User Reviews Analysis Dashboard

**Live Application:** [View on Streamlit Cloud](https://amazon-reviews-analysis-fpn7avhj8gxxcfeayq595h.streamlit.app/)

## 📖 Project Overview
This project is a high-performance, interactive Streamlit dashboard designed for analyzing over 250,000 Amazon fine food reviews. It demonstrates advanced data engineering techniques, such as **Parquet conversion** for memory efficiency, a **multi-page architecture**, and **Natural Language Processing (NLP)** for sentiment analysis.

---

### Why this project?
In the massive ecosystem of e-commerce, consumer feedback is the most valuable "unstructured" data available. This project was born out of a desire to solve three specific challenges:

* **Data Scalability:** Handling over 250,000 records efficiently on a web interface by utilizing **Parquet and Brotli compression** for near-instant load times.
* **User Behavior Profiling:** Moving beyond simple averages to identify if **"Frequent" reviewers** provide more critical or detailed feedback than "Casual" ones.
* **Sentiment Gap Analysis:** Detecting **"false positives"**—reviews where a user gives 5 stars but writes a summary with negative polarity—to help brands identify hidden friction points.

---

## 🚀 Key Features

* **Interactive Dashboards:** Switched from static plots to **Plotly Express**, allowing users to zoom, hover, and filter data dynamically.
* **Product Analysis:** Explore score distributions and trends for high-volume products (500+ reviews).
* **Reviewer Behavior:** Comparative analysis of "Frequent" vs. "Casual" reviewers using distribution density and word counts.
* **Sentiment Analysis:** Real-time NLP processing using **TextBlob** to calculate polarity and correlate text with star ratings.
* **Optimized Data Pipeline:** Uses cached Parquet loading to handle large datasets with minimal latency.

---

## 🛠️ Tech Stack

* **Dashboard:** Streamlit (Multi-page)
* **Visualizations:** Plotly Express (Interactive), Seaborn (Statistical)
* **Data Engineering:** Pandas, PyArrow (Parquet)
* **NLP:** TextBlob

---

## ⚙️ Local Setup

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Amazon-Review-Analysis.git](https://github.com/your-username/Amazon-Review-Analysis.git)
   cd Amazon-Review-Analysis

---

## 📂 Project Structure
```text
python-amazon-reviews-analysis/
├── pages/                    # Multi-page application structure
│   ├── Sentiment_Analysis.py
│   └── ...
├── data/                     # Data directory (Parquet files)
├── main.py                   # Entry point for the Streamlit dashboard
├── requirements.txt          # Project dependencies
└── README.md
```


# 🎬 Netflix Streaming Analytics Pipeline

*A mini data engineering project using Python, Pandas, DuckDB, Faker & Jupyter.*

## 📌 Overview

This project simulates Netflix-style streaming activity logs and builds a lightweight analytics pipeline to extract insights such as:

* **Top genres during peak hours (7 PM – 12 AM)**
* **Average session duration**
* **Most binge-watched shows (sessions > 45 mins)**

It demonstrates **data generation, ingestion, transformation, SQL analytics, and visualization** — all without needing Kafka or Spark.

Perfect for a data engineering resume or portfolio.

---

## 🧩 Project Architecture

```
Fake Logs → CSV → DuckDB → Analytics Notebook → Visual Insights
```

### Steps

1. **Generate 5,000 synthetic streaming logs** (genres, timestamps, durations)
2. **Load data into DuckDB** as a table
3. **Run SQL analytics** to compute time-based insights
4. **Visualize results** using Matplotlib

---

## 📁 Project Structure

```
netflix-pipeline/
│── data/                # Generated logs (CSV)
│── db/                  # DuckDB database
│── notebooks/
│    └── analytics.ipynb # SQL queries + charts
│── scripts/
│    ├── generator.py    # Fake data generator
│    └── load_duckdb.py  # Load CSV → DuckDB
│── venv/                # Virtual environment
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/netflix-pipeline
cd netflix-pipeline
```

### 2️⃣ Create virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Pipeline

### **Step 1 — Generate fake logs**

```bash
python scripts/generator.py
```

Creates:

```
data/logs.csv
```

### **Step 2 — Load logs into DuckDB**

```bash
python scripts/load_duckdb.py
```

Creates:

```
db/netflix.db
```

### **Step 3 — Run Analytics Notebook**

Open:

```
notebooks/analytics.ipynb
```

Run all cells to see:

* Peak-hour genre trends
* Most binge-watched shows
* Average watch duration
* Data visualizations

---

## 📊 Example Insights (what your notebook produces)

* **Drama & Sci-Fi dominate evening hours**
* **Average watch duration**: ~35–50 minutes
* **Top binge shows**:

  * Stranger Things
  * Money Heist
  * The Office

(Your values will differ based on random generation.)

---

## 🔧 Technologies Used

| Component            | Purpose                  |
| -------------------- | ------------------------ |
| **Python**           | Data pipeline & scripts  |
| **Faker**            | Synthetic log generation |
| **Pandas**           | Data manipulation        |
| **DuckDB**           | Fast OLAP SQL engine     |
| **Matplotlib**       | Visualization            |
| **Jupyter Notebook** | Analysis environment     |
| **VS Code**          | Development              |

---

## 🎯 Why This Project Matters

This project shows you can:

* Design an **end-to-end data pipeline**
* Work with **time-based analytics**
* Structure real-world data engineering folders
* Use modern tools like **DuckDB**, increasingly popular in DE roles
* Present insights via **visualizations**

Recruiters love projects like this because they demonstrate practical engineering — not just ML notebooks.

---

## 📄 Future Improvements

Here’s what you can add later:

* Real-time ingestion using Kafka or Redpanda
* Airflow or Prefect orchestration
* Parquet storage optimization
* AWS S3 + Athena version
* dbt modeling
* Dockerization

---


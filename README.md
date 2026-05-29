# ⚖️ Weight Prediction MLflow App

A machine learning web application built with **Streamlit** and **Python** that predicts a user's weight based on their height. This project integrates **MLflow** for machine learning lifecycle management, tracking parameters, and model logging.

---

## 🚀 Features
* **Interactive UI**: Clean interface built using Streamlit to input height (in feet) and actual weight (in kg).
* **ML Predictions**: Instantly computes and displays the predicted weight using a trained ML model.
* **Health Insights**: Automatically calculates Body Mass Index (BMI) and identifies the health category (e.g., Normal, Underweight, Overweight).
* **MLflow Tracking**: Complete tracking of model experiments, parameters, and metrics for MLOps compliance.

---

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **Frontend**: Streamlit
* **MLOps / Tracking**: MLflow
* **Libraries**: Pandas, NumPy, Scikit-Learn

---

## 💻 Local Setup & Execution

Follow these steps to run the project locally on your machine:

### 1. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the MLflow UI (For Tracking)
```bash
mlflow ui
```
*The MLflow UI will be available locally at `http://localhost:5000`*

### 4. Run the Streamlit Web Application
```bash
streamlit run app.py
```
*The app will open automatically in your browser at `http://localhost:8503`*

---

## 📊 Sample Output & Metrics
* **Input Height**: 5.80 feet
* **Predicted Weight**: 57.71 kg
* **Calculated BMI**: 24.00
* **Health Category**: Normal

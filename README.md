# MKbias-buster
 AI Fairness Evaluation Toolkit using FastAPI & Streamlit

An AI tool that evaluates prediction bias across sensitive attributes like gender using FastAPI and Streamlit.

## 🚀 How It Works

1. Upload a CSV file with actual, predicted values & a sensitive column (e.g., gender)
2. The backend calculates bias metrics (TPR/FPR) for each group
3. Streamlit UI shows results in real time

---

## 🧪 Tech Stack

- Python
- FastAPI
- Streamlit
- Pandas
- Uvicorn

---

## 📁 Project Structure
├── .github/
MKbias-buster/
 ├── backend/ 
 │ └── app/ │ 
 ├── main.py # FastAPI entry point │
  ├── router.py # API route handlers │ 
└── utils/
 │ └── fairness_metrics.py # Bias evaluation logic
  ├── frontend/ 
  │ └── streamlit_app.py # Streamlit UI to upload and visualize
   ├── data/
    │ └── sample_data.csv # Sample dataset for testing
     ├── tests/
      │ └── test_fairness.py # Future unit tests
      
      ├── .gitignore # Git ignore file for Python projects
       ├── requirements.txt # Python dependencies 
       └── README.md # This file

---



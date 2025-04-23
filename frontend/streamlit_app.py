import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import base64
from io import BytesIO

st.set_page_config(page_title="Bias Buster Dashboard", layout="wide")

# === CUSTOM DASHBOARD CSS ===
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #1d4ed8;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 0.6em 1.5em;
            font-size: 16px;
        }
        .stMarkdown {
            font-size: 18px;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .report-style {
            background-color: #1e293b;
            padding: 1.5em;
            border-radius: 12px;
            margin-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("<h1 style='text-align: center;'>📊 Bias Buster – Fairness Evaluation Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Detect prediction bias by group using FastAPI + Streamlit</p>", unsafe_allow_html=True)

# === FILE UPLOAD ===
st.markdown("### 📤 Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a CSV with 'actual', 'predicted', and 'gender'", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    with st.container():
        st.markdown("### 👁️ Preview of Your Data")
        st.dataframe(df.head(), use_container_width=True)

    if st.button("🚀 Run Bias Evaluation"):
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/evaluate", files=files)

            if response.status_code == 200:
                result = response.json()
                st.success("✅ Bias evaluation complete!")

                # Transform result
                result_df = pd.DataFrame(result).T.reset_index()
                result_df.columns = ["Group", "TPR", "FPR"]

                # === METRICS ===
                st.markdown("### 🧮 Key Metrics")
                for idx, row in result_df.iterrows():
                    st.metric(label=f"Group: {row['Group']}", value=f"TPR: {row['TPR']}", delta=f"FPR: {row['FPR']}")

                # === PLOT ===
                st.markdown("### 📈 Bias Visualization")
                fig, ax = plt.subplots()
                result_df.set_index("Group")[["TPR", "FPR"]].plot(kind="bar", ax=ax)
                plt.title("TPR vs FPR by Group")
                plt.ylabel("Rate")
                plt.xticks(rotation=0)
                st.pyplot(fig)

                # === DOWNLOAD BUTTON ===
                st.markdown("### 📥 Download Report")
                csv = result_df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="bias_report.csv">📄 Download Bias Report</a>'
                st.markdown(href, unsafe_allow_html=True)

            else:
                st.error(f"❌ API Error – Status Code: {response.status_code}")

        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")

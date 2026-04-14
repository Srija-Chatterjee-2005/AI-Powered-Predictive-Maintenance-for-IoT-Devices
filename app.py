import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time
from src.prediction import load_model, predict

# CONFIG
st.set_page_config(page_title="Predictive Maintenance", layout="wide")

#st.markdown("""
#<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
#""", unsafe_allow_html=True)


# LOAD
df = pd.read_csv("data/sensor_data.csv")
#model = load_model()

try:
    model = load_model()
except:
    st.error("⚠️ Model not found. Please run main.py first.")
    st.stop()

# ======================
# SIDEBAR (UPGRADED)
# ======================
st.sidebar.markdown("## ⚙️ Control Panel")

st.sidebar.markdown("### 📊 Navigation")
page = st.sidebar.radio(
    "Navigation", 
    ["🏠 Overview", "📡 Live Monitoring", "📊 Analytics", "🔮 Prediction"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

st.sidebar.markdown("### ⚠️ Alerts")
threshold = st.sidebar.slider("Temperature Threshold", 50, 100, 75)

st.sidebar.markdown("---")

st.sidebar.markdown("### 🟢 Status")
st.sidebar.success("System Active")

st.sidebar.caption("Version 1.0 | AI Monitoring")

# ======================
# OVERVIEW
# ======================
if page == "🏠 Overview":

    st.title("🏭 AI Predictive Maintenance")
    st.caption("Real-time Industrial Monitoring & Failure Prediction System")
    st.markdown(
        "<p style='color:#cfe8ff; font-size:16px;'>Real-time industrial monitoring dashboard</p>",
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Temperature", f"{df['temperature'].mean():.2f}")
    col2.metric("Avg Vibration", f"{df['vibration'].mean():.2f}")
    col3.metric("Failure Rate", f"{df['failure'].mean()*100:.2f}%")

    st.divider()

    st.subheader("📈 Sensor Trends")

    fig = px.line(df, y=["temperature", "vibration", "current"])
    st.plotly_chart(fig, use_container_width=True)

# ======================
# LIVE MONITORING 
# ======================
elif page == "📡 Live Monitoring":
    
    st.title("📡 Live Monitoring (Simulation)")
    st.markdown("Real-time IoT sensor simulation")

    run = st.toggle("▶ Start Monitoring")

    if run:
        placeholder = st.empty()

        for i in range(10):   # reduced to avoid freeze

            temp = np.random.uniform(40, 100)
            vib = np.random.uniform(1, 10)
            curr = np.random.uniform(5, 15)

            with placeholder.container():

                col1, col2, col3 = st.columns(3)

                col1.metric("Temperature", f"{temp:.2f}")
                col2.metric("Vibration", f"{vib:.2f}")
                col3.metric("Current", f"{curr:.2f}")

                if temp > threshold:
                    st.error("⚠️ High Temperature Alert!")

                fig = px.bar(
                    pd.DataFrame({
                        "Sensor": ["Temp", "Vibration", "Current"],
                        "Value": [temp, vib, curr]
                    }),
                    x="Sensor", y="Value"
                )

                st.plotly_chart(fig, use_container_width=True)

            time.sleep(1)

# ======================
# ANALYTICS
# ======================
elif page == "📊 Analytics":

    import os
    
    st.title("📊 Analytics Dashboard")

    st.write("All system insights and failure analysis")
    if not os.path.exists("outputs/output_1.png"):
        st.warning("⚠️ Please run main.py first to generate analytics outputs")

    else: 
        col1, col2 = st.columns(2)

        with col1:
            st.image("outputs/output_1.png")
            st.image("outputs/output_3.png")
            st.image("outputs/output_5.png")
            st.image("outputs/output_7.png")

        with col2:
            st.image("outputs/output_2.png")
            st.image("outputs/output_4.png")
            st.image("outputs/output_6.png")
            st.image("outputs/output_8.png")

# ======================
# PREDICTION
# ======================
#elif page == "🔮 Prediction":
    
    #st.title("🔮 Failure Prediction")

    #st.markdown(
       # "<p style='color:#cfe8ff; font-size:16px;'>Predict machine breakdown using AI</p>",
       # unsafe_allow_html=True
   # )

    # ✅ FIX HERE
   # col1, col2, col3 = st.columns(3)

    #with col1:
       # temp = st.slider("Temperature", 0, 100, 50)

    #with col2:
      #  vib = st.slider("Vibration", 0.0, 10.0, 2.5)

   # with col3:
       # curr = st.slider("Current", 0.0, 20.0, 7.0)

    #st.divider()

    #if st.button("🚀 Run Prediction"):

       # result = predict(model, temp, vib, curr)

       # if result == 1:
       #     st.error("⚠️ High Risk of Failure")
       # else:
          #  st.success("✅ Machine Operating Normally")

    # DOWNLOAD REPORT 
   # report = pd.DataFrame({
     #   "Temperature": [temp],
      #  "Vibration": [vib],
      #  "Current": [curr]
  #  })

    #st.download_button("📥 Download Report", report.to_csv(index=False), "report.csv")

    #st.divider()

    #st.subheader("📊 Input Data")
   # st.dataframe(report)
elif page == "🔮 Prediction":
    
    st.title("🔮 Failure Prediction")

    mode = st.radio("Choose Mode", ["Single Input", "Batch Prediction"])

    # =====================
    # SINGLE INPUT
    # =====================
    if mode == "Single Input":

        col1, col2, col3 = st.columns(3)

        with col1:
            temp = st.slider("Temperature", 0, 100, 50)

        with col2:
            vib = st.slider("Vibration", 0.0, 10.0, 2.5)

        with col3:
            curr = st.slider("Current", 0.0, 20.0, 7.0)

        if st.button("🚀 Predict"):

            result = predict(model, temp, vib, curr)

            if result == 1:
                st.error("⚠️ High Risk of Failure")
            else:
                st.success("✅ Machine Operating Normally")

    # =====================
    # BATCH PREDICTION
    # =====================
    else:

        st.subheader("📂 Upload CSV for Batch Prediction")

        file = st.file_uploader("Upload CSV", type=["csv"])

        if file is not None:

            data = pd.read_csv(file)

            st.write("📊 Uploaded Data")
            st.dataframe(data)

            predictions = []

            for _, row in data.iterrows():
                result = predict(model, row['temperature'], row['vibration'], row['current'])
                predictions.append(result)

            data['Prediction'] = predictions

            st.write("✅ Prediction Results")
            st.dataframe(data)

            st.download_button(
                "📥 Download Results",
                data.to_csv(index=False),
                "predictions.csv"
            )

        #st.bar_chart(data['Prediction'].value_counts())
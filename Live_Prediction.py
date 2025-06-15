
import streamlit as st
import pandas as pd
import joblib
import sqlite3

st.set_page_config(page_title="Live Prediction", layout="wide")

st.title("🔮 Live Failure Prediction")

if not os.path.exists("model.pkl"):
    st.warning("Please train the model first using 'Upload & Analyze' page.")
else:
    model, feature_columns = joblib.load("model.pkl")
    st.info("Enter real-time data for prediction:")

    input_data = {}
    for feature in feature_columns:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)

    if st.button("🚨 Predict"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        result = "Failure" if prediction == 1 else "Normal"
        st.success(f"🔍 Prediction: {result}")

        conn = sqlite3.connect("pump_logs.db")
        input_df["prediction"] = prediction
        input_df.to_sql("predictions", conn, if_exists="append", index=False)
        conn.close()

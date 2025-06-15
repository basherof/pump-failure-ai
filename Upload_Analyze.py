
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import joblib
import os

st.set_page_config(page_title="Upload & Analyze", layout="wide")

st.title("📤 Upload & Analyze Pump Data")

uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=['csv', 'xlsx'])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    label_column = st.selectbox("🎯 Select Target Column", df.columns)
    feature_columns = st.multiselect("📌 Select Features", [col for col in df.columns if col != label_column], default=[col for col in df.columns if col != label_column])

    if feature_columns and label_column:
        X = df[feature_columns]
        y = df[label_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        joblib.dump((model, feature_columns), "model.pkl")

        st.success("✅ Model trained successfully!")
        st.code(classification_report(y_test, y_pred), language='text')
        st.metric("🎯 Accuracy", f"{accuracy_score(y_test, y_pred) * 100:.2f}%")

        st.subheader("🔥 Feature Importance")
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        fig, ax = plt.subplots()
        ax.bar(range(len(importances)), importances[indices])
        ax.set_xticks(range(len(importances)))
        ax.set_xticklabels(np.array(feature_columns)[indices], rotation=45)
        st.pyplot(fig)

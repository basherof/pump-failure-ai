
import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Database Log", layout="wide")

st.title("🗂️ Predictions Log")

if os.path.exists("pump_logs.db"):
    conn = sqlite3.connect("pump_logs.db")
    df = pd.read_sql("SELECT * FROM predictions", conn)
    st.dataframe(df)
else:
    st.warning("No logs found. Predictions will appear here once made.")


import streamlit as st
import pandas as pd
from fpdf import FPDF
import datetime
import os

st.set_page_config(page_title="Reports", layout="wide")

st.title("📑 Generate PDF Report")

if os.path.exists("model.pkl"):
    if st.button("📥 Generate Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Pump Failure Prediction Report", ln=1, align="C")
        pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now()}", ln=2, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt="This is an auto-generated report from the AI monitoring system.", ln=3)

        report_path = "report.pdf"
        pdf.output(report_path)

        with open(report_path, "rb") as f:
            st.download_button("⬇️ Download Report", f, file_name="Pump_Report.pdf")
else:
    st.warning("Model not found. Please train the model first.")

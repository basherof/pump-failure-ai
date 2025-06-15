
# AI-based Pump Failure Detection System

A professional multi-page Streamlit web application for early detection of pump failures using machine learning. Designed for industrial and academic use (e.g., graduation projects in engineering and AI fields).

---

## 🚀 Features

- Upload pump operational data (CSV/Excel)
- Train ML models (Random Forest by default)
- Real-time prediction from manual input
- Generate professional PDF reports
- Store and view all predictions in a database (SQLite)
- Dark theme and modern interface

---

## 📁 Project Structure

```
pump_failure_ai_app/
│
├── Home.py                  ← Landing page
├── Upload_Analyze.py        ← Data upload, training, and analysis
├── Live_Prediction.py       ← Manual input and real-time failure prediction
├── Reports.py               ← PDF report generation
├── Database_Log.py          ← Prediction logs from database
├── pump_logs.db             ← SQLite DB created automatically
├── model.pkl                ← Trained model saved automatically
├── sample_pump_data.xlsx    ← Sample dataset (you can replace it)
```

---

## 🛠️ How to Run

1. Unzip the project folder:
```bash
unzip pump_failure_ai_app.zip
cd pump_failure_ai_app
```

2. Install the required packages:
```bash
pip install streamlit pandas scikit-learn matplotlib joblib fpdf openpyxl
```

3. Run the application:
```bash
streamlit run Home.py
```

---

## 📊 Sample Dataset
A sample Excel file (`sample_pump_data.xlsx`) is provided with the following columns:

- `Vibration`
- `Temperature`
- `Pressure`
- `FlowRate`
- `RPM`
- `Failure` (target: 0 = Normal, 1 = Failure)

---

## 🎓 Suitable For:
- Graduation projects (Engineering / AI / Oil & Gas)
- Industrial applications in predictive maintenance
- Teaching and prototyping ML for real-world systems

---

## 📄 License
This project is provided for academic and demonstration purposes.

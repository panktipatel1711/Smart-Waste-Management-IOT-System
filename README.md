# ♻️ Smart Waste Management & Bin Level Detection System

An enterprise-grade, high-contrast Industrial IoT (IIoT) Dashboard built with **Streamlit** and **Plotly** to monitor, track, and simulate waste accumulation levels across smart city nodes in real-time.

---

## 🌌 Project Overview
This project serves as the centralized **Fleet Control Matrix** for urban infrastructure waste tracking. It visualizes data streams from IoT nodes (like ESP32/Ultrasonic sensors), logs telemetry inputs into an automated data layer, and dynamically triggers high-visibility **Critical Alerts** when storage thresholds are breached.

### 🚀 Key Features
- **Interactive Fleet Control:** Sidebar integration allowing manual operation injection (`Inject New Waste Data`) to simulate live hardware streams without background script dependency.
- **Dynamic Alerts Engine:** Immediate dashboard theme-switch to **Red Alert Mode** (`🔴 OVERFLOW RISK`) once storage exceeds 80% utilization.
- **Advanced Volumetrics:** Real-time asset progression using Plotly Gauge indicators and interactive time-series progression graphs.
- **Automated Ledger:** Live tracking feed showing the last 10 historical network telemetry logs with descending timestamps.

---

## 🛠️ Tech Stack
- **Dashboard Interface:** Streamlit (Python-based UI/UX Canvas)
- **Data Analytics & Logging:** Pandas, Python File I/O Engine
- **Data Visualization:** Plotly Graph Objects & Plotly Express
- **Version Control & Deployment:** Git, GitHub

---

## 📂 Project Structure
```text
Smart-Waste-Management-Bin-Level-Detection-System/
├── data/
│   └── waste_log.csv       # Automated telemetry database matrix
├── app.py                  # Streamlit dashboard engine & UI layout
└── README.md               # Professional project documentation
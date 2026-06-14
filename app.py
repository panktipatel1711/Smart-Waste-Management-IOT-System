import os
import random
import datetime
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# --- Ultra Pro UI/UX Canvas Configuration ---
st.set_page_config(
    page_title="Industrial IoT Waste Matrix Portal",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

CSV_FILE_PATH = "./data/waste_log.csv"
BIN_TOTAL_HEIGHT_CM = 50.0

# --- Automatic Data File Initialization ---
if not os.path.exists("./data"):
    os.makedirs("./data")

if not os.path.exists(CSV_FILE_PATH) or os.stat(CSV_FILE_PATH).st_size == 0:
    init_df = pd.DataFrame([{
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Distance_CM": 48.0,
        "Fill_Percentage": 4.0,
        "Status_Code": "SYSTEM_OK_EMPTY",
        "Alert_Status": 0
    }])
    init_df.to_csv(CSV_FILE_PATH, index=False)

# --- Fetch Data Layer Safely ---
df = pd.read_csv(CSV_FILE_PATH)

# --- Dynamic CSS Injection: Premium Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* SIDEBAR TEXT VISIBILITY FIXES */
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stMarkdown p {
        color: #f1f5f9 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
    }
    
    /* KPI Cards Styling */
    .metric-card-container {
        background-color: #ffffff !important;
        padding: 22px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: 1px solid #cbd5e1;
        margin-bottom: 15px;
    }
    .card-title {
        color: #475569 !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        margin: 0 0 6px 0 !important;
    }
    .card-value {
        color: #0f172a !important;
        font-size: 30px !important;
        font-weight: 800 !important;
        margin: 0 0 4px 0 !important;
    }
    .card-footer {
        color: #1e293b !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        margin: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Fleet Control Sidebar Panel ---
st.sidebar.markdown("## 🌐 Fleet Control Matrix")
st.sidebar.markdown("---")

st.sidebar.markdown("### 🕹️ Hardware Control Panel")

# THE MASTER BUTTON: INJECT DATA OPERATION + AUTO ALERT PROTOCOL
if st.sidebar.button("🚀 Inject New Waste Data", use_container_width=True):
    last_record = df.iloc[-1]
    last_fill = float(last_record['Fill_Percentage'])
    
    # Reset logic if bin is full
    if last_fill >= 90.0:
        new_fill = random.uniform(4.0, 8.0)
    else:
        # Step operation: Har click par kachra badhega
        new_fill = min(last_fill + random.uniform(12.0, 18.0), 100.0)
        
    new_dist = round(BIN_TOTAL_HEIGHT_CM - (new_fill / 100.0 * BIN_TOTAL_HEIGHT_CM), 2)
    
    # Alert assignment logic boundaries
    if new_fill >= 80.0:
        new_status = "CRITICAL_FULL"
        new_alert = 1
    elif new_fill >= 50.0:
        new_status = "WARNING_HALF"
        new_alert = 0
    else:
        new_status = "SYSTEM_OK_EMPTY"
        new_alert = 0
        
    # Append the newly calculated operational row to the database
    new_row = pd.DataFrame([{
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Distance_CM": new_dist,
        "Fill_Percentage": round(new_fill, 2),
        "Status_Code": new_status,
        "Alert_Status": new_alert
    }])
    
    new_row.to_csv(CSV_FILE_PATH, mode='a', header=False, index=False)
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 🖥️ Asset Framework Status")
st.sidebar.code("Device ID: IoT-BLD-NODE-01\nStatus: INTEGRATED_ENGINE_OK", language="text")

# --- Process Extracted Telemetry Matrix ---
latest_record = df.iloc[-1]
current_fill = latest_record['Fill_Percentage']
current_dist = latest_record['Distance_CM']
current_status = str(latest_record['Status_Code'])
alert_triggered = int(latest_record['Alert_Status'])
critical_alerts_count = df[df['Alert_Status'] == 1].shape[0]

# --- Dynamic Theme Alerts Engine ---
if current_fill >= 80:
    status_color = "#dc2626" 
    status_badge = "🔴 OVERFLOW RISK (ALERT ACTIVE)"
elif current_fill >= 50:
    status_color = "#d97706" 
    status_badge = "🟡 LOADING WARNING"
else:
    status_color = "#059669" 
    status_badge = "🟢 STABLE OPERATION"

# --- Dashboard Header Brand Banner ---
st.markdown("<h1 style='color:#0f172a; font-weight:800; margin-bottom:5px;'>♻️ Smart Waste Management System</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#334155; font-size:15px; font-weight:500; margin-top:0px;'>Enterprise Urban Infrastructure Asset Tracking Network Dashboard Panel</p>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top:10px; margin-bottom:25px; border-color:#cbd5e1;'>", unsafe_allow_html=True)

# --- ROW 1: Core Metrics Grid ---
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(f"""<div class='metric-card-container' style='border-left: 5px solid #2563eb;'><p class='card-title'>📍 Deployment Anchor</p><p class='card-value'>Zone Alpha</p><p class='card-footer'>Central Core Sector</p></div>""", unsafe_allow_html=True)
with kpi_col2:
    st.markdown(f"""<div class='metric-card-container' style='border-left: 5px solid #0891b2;'><p class='card-title'>📏 Sensor Headroom</p><p class='card-value'>{current_dist} cm</p><p class='card-footer'>Distance to Material Face</p></div>""", unsafe_allow_html=True)
with kpi_col3:
    st.markdown(f"""<div class='metric-card-container' style='border-left: 5px solid {status_color};'><p class='card-title'>📊 Storage Utilization</p><p class='card-value' style='color:{status_color} !important;'>{current_fill} %</p><p class='card-footer'>State: <span style='color:{status_color}; font-weight:800;'>{status_badge}</span></p></div>""", unsafe_allow_html=True)
with kpi_col4:
    st.markdown(f"""<div class='metric-card-container' style='border-left: 5px solid #dc2626;'><p class='card-title'>⚠️ Total Route Alerts</p><p class='card-value' style='color:#dc2626 !important;'>{critical_alerts_count}</p><p class='card-footer'>Collection Demands Dispatched</p></div>""", unsafe_allow_html=True)
    
st.markdown("<br>", unsafe_allow_html=True)

# --- ROW 2: Interactive High-Contrast Charts Layout ---
viz_col1, viz_col2 = st.columns([1, 2])

with viz_col1:
    st.markdown("<h4 style='color:#0f172a; font-weight:700; margin-top:0; margin-bottom:10px;'>Asset Volumetrics</h4>", unsafe_allow_html=True)
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_fill,
        domain = {'x': [0, 1], 'y': [0, 1]},
        number = {'font': {'size': 50, 'color': '#0f172a', 'family': 'Arial'}, 'suffix': "%"},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#0f172a", 'tickfont': {'color': '#0f172a'}},
            'bar': {'color': "#0f172a", 'thickness': 0.25}, 
            'bgcolor': "#f8fafc",
            'borderwidth': 1,
            'bordercolor': "#cbd5e1",
            'steps': [
                {'range': [0, 50], 'color': '#bbf7d0'}, 
                {'range': [50, 80], 'color': '#fef08a'}, 
                {'range': [80, 100], 'color': '#fca5a5'} 
            ],
        }
    ))
    fig_gauge.update_layout(height=240, margin=dict(l=15, r=15, t=10, b=15), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_gauge, use_container_width=True)
    
with viz_col2:
    st.markdown("<h4 style='color:#0f172a; font-weight:700; margin-top:0; margin-bottom:10px;'>Time-Series Load Progression Graph</h4>", unsafe_allow_html=True)
    df_slice = df.tail(30)
    fig_trend = px.line(df_slice, x="Timestamp", y="Fill_Percentage", template="plotly_white")
    fig_trend.update_traces(line_color="#1d4ed8", line_width=4, mode="lines+markers", marker=dict(size=7, color="#0f172a"))
    fig_trend.add_hline(y=80, line_dash="dash", line_color="#b91c1c", line_width=2)
    fig_trend.update_layout(
        height=240, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title_font=dict(color='#0f172a', size=12), tickfont=dict(color='#0f172a')),
        yaxis=dict(title_font=dict(color='#0f172a', size=12), tickfont=dict(color='#0f172a'))
    )
    st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- ROW 3: Network Telemetry Ledger Log Sheet ---
st.markdown("<h3 style='color:#0f172a; font-weight:700;'>📑 Network Telemetry Log Stream Feed</h3>", unsafe_allow_html=True)
st.dataframe(df.tail(10).sort_values(by="Timestamp", ascending=False), use_container_width=True)
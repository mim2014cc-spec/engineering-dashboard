import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from services.humidity import classify_humidity

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="Advanced Humidity", page_icon="💧", layout="wide")

# แทรก CSS ตกแต่ง Card อัตโนมัติ
st.markdown("""
<style>
    .metric-card {
        background-color: #1E1E1E; padding: 20px; border-radius: 15px;
        text-align: center; border: 1px solid #333; box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    .status-text { font-size: 28px; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("💧 แผงควบคุมความชื้นระดับอุตสาหกรรม")
st.markdown("---")

# 1. ย้ายแผงควบคุมไปไว้ Sidebar
with st.sidebar:
    st.header("🎛️ Simulator Control")
    humid = st.slider("จำลองค่าความชื้น (%)", 0.0, 100.0, 50.0, 0.5)
    status = classify_humidity(humid)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.expander("ℹ️ Contract (เกณฑ์การประเมิน)"):
        st.write("🟢 **NORMAL:** 40 - 60%")
        st.write("🟡 **WARNING:** 30 - 70%")
        st.write("🔴 **CRITICAL:** < 30% หรือ > 70%")

# กำหนดสีตามสถานะ
color_map = {"NORMAL": "#00CC96", "WARNING": "#FFA15A", "CRITICAL": "#EF553B"}
icon_map = {"NORMAL": "✅", "WARNING": "⚠️", "CRITICAL": "🚨"}
current_color = color_map.get(status, "#ffffff")

# 2. แถวบน: สรุปข้อมูล (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("ความชื้นสัมพัทธ์ (RH)", f"{humid:.1f} %", "Real-time Update")
col3.metric("อุณหภูมิห้องเซิร์ฟเวอร์", "24.5 °C", "-0.2 °C (จำลอง)")

with col2:
    st.markdown(f"""
        <div class='metric-card'>
            <span style='color: gray; font-size: 14px;'>SYSTEM STATUS</span><br>
            <div class='status-text' style='color: {current_color};'>{icon_map[status]} {status}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3. แถวกลาง: กราฟิกแสดงผล
chart_col1, chart_col2 = st.columns([1, 1.5])

with chart_col1:
    # หน้าปัด Gauge Chart สไตล์รถสปอร์ต/เครื่องจักร
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = humid,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': current_color},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': "rgba(239, 85, 59, 0.2)"},
                {'range': [30, 40], 'color': "rgba(255, 161, 90, 0.2)"},
                {'range': [40, 60], 'color': "rgba(0, 204, 150, 0.2)"},
                {'range': [60, 70], 'color': "rgba(255, 161, 90, 0.2)"},
                {'range': [70, 100], 'color': "rgba(239, 85, 59, 0.2)"}],
        }
    ))
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    # กราฟเส้นจำลองข้อมูล 24 ชั่วโมงย้อนหลัง
    st.markdown("<h5 style='text-align: center; color: gray;'>📈 แนวโน้มความชื้น 24 ชั่วโมงย้อนหลัง (Trend)</h5>", unsafe_allow_html=True)
    np.random.seed(42)
    time_index = pd.date_range(end=pd.Timestamp.now(), periods=24, freq="h")
    sim_data = np.random.normal(loc=50, scale=8, size=24)
    sim_data[-1] = humid # บังคับจุดสุดท้ายให้ตรงกับสไลเดอร์ปัจจุบัน
    
    df = pd.DataFrame({"Time": time_index, "Humidity (%)": sim_data}).set_index("Time")
    st.line_chart(df, color=current_color, height=270)
import streamlit as st
from services.humidity import classify_humidity

st.title("💧 Humidity Monitoring")
humid = st.slider("ความชื้นสัมพัทธ์ (%)", 0.0, 100.0, 50.0, 0.5)
status = classify_humidity(humid)

st.metric("ความชื้น", f"{humid:.1f} %")
status_display = {"NORMAL": st.success, "WARNING": st.warning, "CRITICAL": st.error}
status_display[status](f"สถานะ: {status}")
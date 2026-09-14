# pages/3_Power.py
import streamlit as st
from services.power import calculate_power, classify_power

st.set_page_config(page_title="Power Monitoring", page_icon="⚡")

st.title("⚡ Power Monitoring")
st.write("จำลองการตรวจวัดแรงดันไฟฟ้าและกระแสไฟฟ้า เพื่อคำนวณกำลังไฟฟ้าและประเมินสถานะของระบบ")

col1, col2 = st.columns(2)

with col1:
    voltage = st.slider(
        label="แรงดันไฟฟ้า - Voltage (V)",
        min_value=1.0,
        max_value=250.0,
        value=220.0,
        step=1.0,
        help="ค่าแรงดันไฟฟ้าต้องมากกว่า 0 V"
    )

with col2:
    current = st.slider(
        label="กระแสไฟฟ้า - Current (A)",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=0.1,
        help="ค่ากระแสไฟฟ้าต้องมากกว่าหรือเท่ากับ 0 A"
    )

try:
    power = calculate_power(voltage, current)
    status = classify_power(power)

    st.divider()

    # แสดงผลตัวเลขค่าที่คำนวณได้
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Voltage", f"{voltage:.1f} V")
    col_m2.metric("Current", f"{current:.2f} A")
    col_m3.metric("Power", f"{power:.2f} W")

    st.write("### สถานะระบบ (System Status)")
    status_display = {
        "NORMAL": (st.success, "สถานะปกติ (NORMAL) - กำลังไฟฟ้าอยู่ในเกณฑ์ที่ปลอดภัย (< 500 W)"),
        "WARNING": (st.warning, "แจ้งเตือน (WARNING) - กำลังไฟฟ้าค่อนข้างสูง (500 - 1000 W)"),
        "CRITICAL": (st.error, "อันตราย (CRITICAL) - กำลังไฟฟ้าเกินเกณฑ์ความปลอดภัย (> 1000 W)")
    }

    ui_component, message = status_display[status]
    ui_component(f"**{status}**: {message}")

except ValueError as e:
    st.error(f"เกิดข้อผิดพลาดของข้อมูลนำเข้า: {e}")
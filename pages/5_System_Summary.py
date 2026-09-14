import streamlit as st

st.set_page_config(page_title="System Summary", page_icon="📊", layout="wide")
st.title("📊 สรุปภาพรวมระบบ (System Summary)")

st.subheader("📌 เกณฑ์การประเมินสถานะของแต่ละโมดูล")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **1. อุณหภูมิ (Temperature Monitoring):**
    - 🟢 **NORMAL:** 20.0°C - 30.0°C
    - 🟡 **WARNING:** 15.0°C - 19.9°C หรือ 30.1°C - 35.0°C
    - 🔴 **CRITICAL:** น้อยกว่า 15.0°C หรือมากกว่า 35.0°C
    
    **2. ความชื้นสัมพัทธ์ (Humidity Monitoring):**
    - 🟢 **NORMAL:** 40.0% - 60.0%
    - 🟡 **WARNING:** 30.0% - 39.9% หรือ 60.1% - 70.0%
    - 🔴 **CRITICAL:** น้อยกว่า 30.0% หรือมากกว่า 70.0%
    """)

with col2:
    st.markdown("""
    **3. กำลังไฟฟ้า (Power Monitoring):**
    - 🟢 **NORMAL:** โหลดต่ำกว่า 75.0% ของพิกัด
    - 🟡 **WARNING:** โหลด 75.0% - 90.0%
    - 🔴 **CRITICAL:** โหลดเกิน 90.0%
    
    **4. ระบบสัญญาณเตือนภัย (Safety Alarm System):**
    - 🟢 **NORMAL:** สถานะปกติ ไม่พบสัญญาณผิดปกติ
    - 🔴 **CRITICAL:** ตรวจพบการแจ้งเตือนฉุกเฉิน
    """)

st.divider()
st.subheader("👥 ผู้รับผิดชอบโครงการ")
st.write("1. ภีม - โมดูลที่ 1: Temperature Monitoring")
st.write("2. เนติธร - โมดูลที่ 2: Humidity Monitoring")
st.write("3. เมธา - โมดูลที่ 3: Power Monitoring")
st.write("4. ธนโชค - โมดูลที่ 4: Safety Alarm System")
st.write("5. จิตติ - โมดูลที่ 5: System Summary & QA Lead")

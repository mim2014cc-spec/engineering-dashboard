import streamlit as st
from services.alarm import generate_alarms

st.set_page_config(page_title="Safety Alarm Monitoring", page_icon="🚨", layout="wide")

st.title("🚨 Safety Alarm Monitoring")
st.caption("จำลองสถานะระบบเพื่อตรวจสอบความผิดปกติและการแจ้งเตือนอัตโนมัติ")

status_options = ["NORMAL", "WARNING", "CRITICAL"]

col1, col2, col3 = st.columns(3)

with col1:
    temp_status = st.select_slider("🌡️ Temperature", options=status_options, value="NORMAL")
    if temp_status == "NORMAL":
        st.badge("Normal", icon="✅")
    elif temp_status == "WARNING":
        st.badge("Warning", icon="⚠️")
    else:
        st.badge("Critical", icon="🔥")

with col2:
    humid_status = st.select_slider("💧 Humidity", options=status_options, value="NORMAL")
    if humid_status == "NORMAL":
        st.badge("Normal", icon="✅")
    elif humid_status == "WARNING":
        st.badge("Warning", icon="⚠️")
    else:
        st.badge("Critical", icon="🔥")

with col3:
    power_status = st.select_slider("⚡ Power", options=status_options, value="NORMAL")
    if power_status == "NORMAL":
        st.badge("Normal", icon="✅")
    elif power_status == "WARNING":
        st.badge("Warning", icon="⚠️")
    else:
        st.badge("Critical", icon="🔥")

alarms = generate_alarms(temp_status, humid_status, power_status)

st.divider()
st.subheader("🔔 รายการแจ้งเตือน (Active Alarms)")

if not alarms:
    st.success("✅ ระบบทำงานปกติ ไม่มีการแจ้งเตือน (All Systems Normal)")
else:
    for alarm in alarms:
        if "CRITICAL" in alarm:
            st.error(alarm, icon="🚨")
        else:
            st.warning(alarm, icon="⚠️")

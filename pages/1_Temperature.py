import streamlit as st
from services.temperature import TemperatureService

st.title("🌡️ Temperature Monitoring")

# 1. กำหนดค่าเริ่มต้นใน Session State
if "temp_val" not in st.session_state:
    st.session_state.temp_val = 37.0

# 2. ฟังก์ชัน Synchronize ค่าเมื่อ widget ตัวใดตัวหนึ่งเปลี่ยน
def update_from_input():
    st.session_state.temp_val = st.session_state.num_input_key

def update_from_slider():
    st.session_state.temp_val = st.session_state.slider_key

# 3. สร้าง Widgets โดยใช้ key แยกกัน และใส่ on_change
col_in1, col_in2 = st.columns([1, 2])

with col_in1:
    st.number_input(
        "Enter (°C):", 
        min_value=30.0, 
        max_value=45.0, 
        value=st.session_state.temp_val,
        key="num_input_key", 
        on_change=update_from_input,
        step=0.1
    )

with col_in2:
    st.slider(
        "Adjust via Slider (°C):", 
        min_value=30.0, 
        max_value=45.0, 
        value=st.session_state.temp_val,
        key="slider_key", 
        on_change=update_from_slider,
        step=0.1
    )

temp_input = st.session_state.temp_val

# 4. ส่วนคำนวณและแสดงผล
if st.button("Check Status", use_container_width=True):
    status = TemperatureService.check_status(temp_input)
    temp_f = TemperatureService.celsius_to_fahrenheit(temp_input)
    
    st.divider()
    
    c_delta = temp_input - 37.0
    f_delta = temp_f - 98.6

    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Celsius (°C)", 
            value=f"{temp_input:.1f} °C", 
            delta=f"{c_delta:+.1f} °C from normal",
            delta_color="inverse"
        )
    with col2:
        st.metric(
            label="Fahrenheit (°F)", 
            value=f"{temp_f:.2f} °F", 
            delta=f"{f_delta:+.2f} °F from normal",
            delta_color="inverse"
        )
        
    if temp_input >= 38.0:
        st.error(f"🔥 **Status:** {status} (ไข้สูง/อุณหภูมิสูงเกินไป!)")
        st.toast("⚠️ Warning: High Temperature!", icon="🔥")
    elif temp_input <= 35.0:
        st.warning(f"❄️ **Status:** {status} (อุณหภูมิต่ำเกินไป)")
        st.snow()
    else:
        st.success(f"✅ **Status:** {status} (อุณหภูมิปกติ)")
        st.balloons()
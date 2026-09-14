import streamlit as st

st.set_page_config(page_title="System Summary", layout="wide")
st.title("📊 Engineering Monitoring - System Summary")

st.markdown("""
### ภาพรวมระบบ (System Overview)
ระบบแดชบอร์ดจำลองการติดตามสถานะทางวิศวกรรม แบ่งออกเป็น 4 โมดูลหลัก สามารถเลือกใช้งานได้จากแถบเมนูด้านซ้าย:
""")

st.subheader("📋 เกณฑ์สถานะของแต่ละโมดูล")

col1, col2 = st.columns(2)

with col1:
    st.info("🌡️ **1. Temperature Monitoring**\n\n"
            "- ช่วงค่าที่รองรับ: -20 ถึง 80 °C\n"
            "- **NORMAL:** ≤ 30 °C\n"
            "- **WARNING:** > 30 ถึง 35 °C\n"
            "- **CRITICAL:** > 35 °C")
    
    st.warning("⚡ **3. Power Monitoring**\n\n"
               "- คำนวณจากสูตร: P = V × I\n"
               "- เงื่อนไข: V > 0, I ≥ 0\n"
               "- **NORMAL:** < 500 W\n"
               "- **WARNING:** 500 ถึง 1000 W\n"
               "- **CRITICAL:** > 1000 W")

with col2:
    st.success("💧 **2. Humidity Monitoring**\n\n"
               "- ช่วงค่าที่รองรับ: 0 ถึง 100 %\n"
               "- **NORMAL:** 40 ถึง 60 %\n"
               "- **WARNING:** 30 ถึง 70 % (ที่ไม่ใช่ NORMAL)\n"
               "- **CRITICAL:** < 30 % หรือ > 70 %")

    st.error("🚨 **4. Safety Alarm**\n\n"
             "- รวมสถานะจาก Temp, Humid, Power\n"
             "- แจ้งเตือนเรียงตามลำดับโมดูลเมื่อพบ WARNING หรือ CRITICAL\n"
             "- คืนค่าว่าง [] เมื่อทุกระบบปกติ (NORMAL)")

st.divider()

st.subheader("👥 สมาชิกในกลุ่มและบทบาทหน้าที่")
st.markdown("""
1. **ภีม อภิสิทธิ์สันติกุล (คนที่ 1):** Temperature Monitoring (`services/temperature.py`, `pages/1_Temperature.py`, `tests/test_temperature.py`)
2. **เนติธร ตันต๊ะ (คนที่ 2):** Humidity Monitoring (`services/humidity.py`, `pages/2_Humidity.py`, `tests/test_humidity.py`)
3. **เมธา ไกรทอง (คนที่ 3):** Power Monitoring (`services/power.py`, `pages/3_Power.py`, `tests/test_power.py`)
4. **ธนโชค อิ่นแก้ว (คนที่ 4):** Safety Alarm (`services/alarm.py`, `pages/4_Safety_Alarm.py`, `tests/test_alarm.py`)
5. **จิตติ ศรีทิน (คนที่ 5):** Summary + QA + README (`pages/5_System_Summary.py`, `README.md`)
""")
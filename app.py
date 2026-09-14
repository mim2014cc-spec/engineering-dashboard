import streamlit as st

st.set_page_config(
    page_title="Engineering Dashboard",
    page_icon="⚙️",
    layout="wide"
)

st.title("ระบบบริหารจัดการข้อมูลทางวิศวกรรม (Engineering Dashboard)")
st.info("👈 เลือกเมนูการทำงานที่แถบซ้ายมือ (Sidebar) เพื่อดูข้อมูลของแต่ละโมดูล")

st.subheader("👥 รายชื่อสมาชิกในกลุ่ม")
members = [
    "1. ภีม (Temperature Monitoring)",
    "2. เนติธร (Humidity Monitoring)",
    "3. เมธา (Power Monitoring)",
    "4. ธนโชค (Safety Alarm System)",
    "5. จิตติ (System Summary & QA Lead)"
]

for member in members:
    st.write(member)

import streamlit as st

st.set_page_config(
    page_title="Engineering Dashboard",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Engineering Dashboard System")
st.subheader("ยินดีต้อนรับสู่ระบบบริหารจัดการข้อมูลทางวิศวกรรม")

# แสดงเมนูการใช้งาน
st.info("👈 เลือกเมนูการทำงานที่แถบซ้ายมือ (Sidebar) เพื่อดูข้อมูล Temperature Monitoring")

st.divider()

# แสดงรายชื่อสมาชิกในกลุ่ม
st.markdown("### 👥 รายชื่อสมาชิกในกลุ่ม")

members = [
    "1. ภีม",
    "2. เมธา",
    "3. มาร์ก",
    "4. ธนโชค",
    "5. จิตติ"
]

for member in members:
    st.write(member)
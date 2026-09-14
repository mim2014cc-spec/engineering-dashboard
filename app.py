import streamlit as st

st.title("My Dashboard!")

temp = st.slider("Temperature", -20.0, 80.0, 28.0, 1.0)
st.metric("Temperature", f"{temp:.1f} °C")
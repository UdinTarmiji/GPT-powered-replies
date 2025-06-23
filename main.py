import streamlit as st
st.write("API Key found:", st.secrets["OPENAI_API_KEY"][:6] + "...")

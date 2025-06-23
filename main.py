import streamlit as st
from openai import OpenAI
import os

# --- Set up Streamlit page ---
st.set_page_config(page_title="Mood Chatbot", page_icon="🧠")

st.title("🤖 Mood & Motivation Chatbot (GPT-Powered)")
st.write("Talk to me! I’ll respond like a smart friend using GPT 💬")

# --- Load API Key from secrets.toml ---
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
# --- GPT Response Function ---

def ask_gpt(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly chatbot that gives helpful, motivational replies."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()


# --- Chat history ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- User input ---
user_input = st.text_input("Type your message here:")

if st.button("Ask") and user_input:
    with st.spinner("GPT is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            gpt_reply = response.choices[0].message.content
            st.markdown(f"**GPT:** {gpt_reply}")
        except Exception as e:
            st.error(f"Error: {e}")

        # Save to chat history
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", gpt_reply))

# --- Show chat history in bubbles ---
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(
            f"<div style='background:#e0f7fa;padding:10px;border-radius:10px;margin-bottom:5px;text-align:right;color:black'><b>🧍 {sender}:</b> {message}</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='background:#f1f8e9;padding:10px;border-radius:10px;margin-bottom:5px;color:black'><b>🤖 {sender}:</b> {message}</div>",
            unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with 💙 by Dafiq")

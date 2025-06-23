import streamlit as st
import openai

# --- Set up Streamlit page ---
st.set_page_config(page_title="Mood Chatbot", page_icon="🧠")

st.title("🤖 Mood & Motivation Chatbot (GPT-Powered)")
st.write("Talk to me! I’ll respond like a smart friend using GPT 💬")

# --- Load API Key from secrets.toml ---
openai.api_key = st.secrets["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"]

# --- GPT Response Function ---
def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a friendly chatbot that gives helpful, kind, and motivational replies."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()

# --- Chat history ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- User input ---
user_input = st.text_input("💬 Type your message:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something.")
    else:
        # Get GPT reply
        gpt_reply = ask_gpt(user_input)

        # Save to chat history
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", gpt_reply))

# --- Show chat history in bubbles ---
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(
            f"<div style='background:#e0f7fa;padding:10px;border-radius:10px;margin-bottom:5px;text-align:right;color:black'><b>🧍 {sender}:</b> {message}</div>",
            unsafe_allow_html=true)

st.markdown("---")
st.caption("Made with 💙 by Dafiq ")


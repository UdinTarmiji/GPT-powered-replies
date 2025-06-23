import streamlit as st
from openai import OpenAI

# --- Set up Streamlit page ---
st.set_page_config(page_title="Mood Chatbot", page_icon="🧠")

st.title("🤖 Mood & Motivation Chatbot (GPT-Powered)")
st.write("Talk to me! I’ll respond like a smart friend using GPT 💬")

# --- Load API Key from secrets.toml ---
api_key = st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY not found in secrets.toml!")
    st.stop()

client = OpenAI(api_key=api_key)

# --- GPT Response Function ---
def ask_gpt(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly chatbot that gives helpful, motivational replies."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error from GPT: {e}"

# --- Chat history ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- User input ---
user_input = st.text_input("Type your message here:", key="user_input")

if st.button("Ask") and user_input:
    with st.spinner("GPT is thinking..."):
        gpt_reply = ask_gpt(user_input)

    # Save to chat history
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", gpt_reply))

# --- Show chat history in bubbles ---
for sender, message in st.session_state.chat:
    bubble_color = "#e0f7fa" if sender == "You" else "#f1f8e9"
    alignment = "right" if sender == "You" else "left"
    icon = "🧍" if sender == "You" else "🤖"

    st.markdown(
        f"""
        <div style='background:{bubble_color};padding:10px;border-radius:10px;margin-bottom:5px;text-align:{alignment};color:black'>
            <b>{icon} {sender}:</b> {message}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Made with 💙 by Dafiq")

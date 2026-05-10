import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page config
st.set_page_config(page_title="NGO AI Assistant", layout="centered")

st.title("🤖 NGO AI Assistant")

# -------------------------------
# MODEL
# -------------------------------
model = genai.GenerativeModel("gemini-flash-latest")

# -------------------------------
# SYSTEM PROMPT (BRAIN)
# -------------------------------
SYSTEM_PROMPT = """
You are an AI assistant for an NGO.

Help users with:
- Volunteering
- NGO services
- Donations

Be natural, conversational, and helpful.
"""

# -------------------------------
# SESSION STATE
# -------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(
        history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]}
        ]
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

# -------------------------------
# USER INPUT
# -------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response (REAL AI, no keywords)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
            reply = response.text
            st.write(reply)

    # Save AI response
    st.session_state.messages.append(("assistant", reply))

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.messages = []
        st.rerun()
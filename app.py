import streamlit as st
from utils.llm_chain import create_chain
import os
from dotenv import load_dotenv

# Load environment variables (optional if using Streamlit secrets instead)
load_dotenv()

st.write("🔑 API key found?", bool(os.getenv("OPENROUTER_API_KEY")))
st.write("🔑 Key preview (first 10 chars):", os.getenv("OPENROUTER_API_KEY")[:10] if os.getenv("OPENROUTER_API_KEY") else "Not loaded")

st.set_page_config(page_title="Ph1l - AI Career Counselor", layout="centered")

# -------- SIDEBAR ----------
with st.sidebar:
    st.markdown("""
        <style>
        .centered-logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 0rem 0;
        }
        .sidebar-button {
            display: block;
            background-color: #343541;
            color: white;
            padding: 0.6rem 1rem;
            margin: 0.5rem 0;
            border: none;
            border-radius: 6px;
            width: 100%;
            font-weight: 500;
            text-align: center;
            cursor: pointer;
        }
        .sidebar-button:hover {
            background-color: #444654;
        }
        .sidebar-divider {
            margin: 1rem 0;
            border-bottom: 1px solid #444;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="centered-logo-container">', unsafe_allow_html=True)
    st.image("static/ph1l_logo.png", width=80)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🆕 New Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hey! 👋 I’m Ph1l, your AI career buddy. Are you a student, working, or just exploring your options?"}
        ]
        st.rerun()

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    with st.expander("ℹ️ About Ph1l"):
        st.markdown("""
        Ph1l is your AI-powered career counselor 🤖  
        Helping students and professionals make smarter career decisions.
        """)

    with st.expander("⚙️ Settings"):
        st.markdown("_Coming soon_: personalize advice based on your profile!")

    with st.expander("📞 Contact"):
        st.markdown("""
        📧 Email: ph1l@yourdomain.com  
        💬 Telegram: [@Ph1lBot](https://t.me/Ph1lBot)  
        🌐 Website: [ph1l.ai](https://ph1l.ai)
        """)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown("<small style='color: #888;'>© 2025 Ph1l</small>", unsafe_allow_html=True)

# -------- MAIN HEADER ----------
st.markdown(
    "<h2 style='text-align: center; color: #6a1b9a;'>🎓 Ph1l - Your Career Counselor</h2>",
    unsafe_allow_html=True
)

# -------- INIT LANGCHAIN & MEMORY --------
if "chain" not in st.session_state:
    st.session_state.chain = create_chain()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! 👋 I’m Ph1l, your AI career buddy. Are you a student, working, or just exploring your options?"}
    ]

# -------- DISPLAY CHAT HISTORY --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------- USER INPUT & RESPONSE --------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Ph1l is thinking..."):
            try:
                reply = st.session_state.chain.run(user_input)
            except Exception as e:
                reply = "⚠️ Sorry, there was an issue processing your request."
                st.error(f"Error: {e}")
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

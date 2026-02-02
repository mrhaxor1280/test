import streamlit as st
import random

st.set_page_config(page_title="For Hira 💎", page_icon="💎", layout="centered")

# Pink background
st.markdown("""
<style>
    .stApp {
        background-color: #ffe6f0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Hira 💎</h1>", unsafe_allow_html=True)

# Initialize session state
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "answered_yes" not in st.session_state:
    st.session_state.answered_yes = False

no_messages = [
    "Are you sure? 😏",
    "Think again 💭",
    "That doesn’t sound right…",
    "Your heart says yes ❤️",
    "Wrong answer 😌",
    "Don’t break my heart 💔",
]

if not st.session_state.answered_yes:
    st.markdown("<h3 style='text-align:center;'>Do you love me?</h3>", unsafe_allow_html=True)

    # Create 3 columns for “moving” No button
    cols = st.columns(3)
    no_pos = random.randint(0, 2)  # No button moves randomly

    # Yes button fixed
    if cols[0].button("Yes 💖", key="yes_button"):
        st.session_state.answered_yes = True

    # No button floats randomly
    if cols[no_pos].button("No 😢", key=f"no_button_{st.session_state.no_clicks}"):
        st.session_state.no_clicks += 1
        msg = no_messages[st.session_state.no_clicks % len(no_messages)]
        st.warning(msg)

else:
    st.success("Thank you ❤️ I knew it! 🥰✨💎")
    st.balloons()

st.markdown("<p style='text-align:center;color:#555;margin-top:40px;'>Made with love by Fahad Khan</p>", unsafe_allow_html=True)

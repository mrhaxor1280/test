import streamlit as st
import random

# Page setup
st.set_page_config(page_title="For Hira 💎", page_icon="💎", layout="centered")

# Pink background
st.markdown("""
<style>
    .stApp {
        background-color: #ffe6f0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>Hira 💎</h1>", unsafe_allow_html=True)

# Initialize session state
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "answered_yes" not in st.session_state:
    st.session_state.answered_yes = False

# Playful No button messages
no_messages = [
    "Are you sure? 😏",
    "Think again 💭",
    "That doesn’t sound right…",
    "Your heart says yes ❤️",
    "Wrong answer 😌",
    "Don’t break my heart 💔",
    "I don’t accept that 😢",
    "Try again 💕",
    "You’re lying 😜",
    "I know the truth 😎",
    "C’mon, admit it 😘",
    "Nope, that’s wrong 😇",
    "Your brain says no, but heart says yes ❤️",
    "Not convinced 😏",
    "Try harder 😅",
    "I see what you did there 😌",
    "You know the answer 😘",
    "Don’t give up now 💖",
    "I won’t let you say no 😎",
    "Your heart knows better 💓"
]

# Question
st.markdown("<h3 style='text-align:center;'>Do you love me?</h3>", unsafe_allow_html=True)

if not st.session_state.answered_yes:

    # Yes button always in center
    if st.button("Yes 💖", key="yes_button"):
        st.session_state.answered_yes = True

    # Randomly "teleport" No button by adding blank lines
    teleport_lines = random.randint(0, 12)  # adjust for mobile height
    for _ in range(teleport_lines):
        st.write("\n")

    # No button
    if st.button("No 😢", key=f"no_button_{st.session_state.no_clicks}"):
        st.session_state.no_clicks += 1
        msg = random.choice(no_messages)
        st.warning(msg)

else:
    # End screen
    st.success("Thank you ❤️ I knew it! 🥰✨💎")
    st.balloons()

# Footer
st.markdown("<p style='text-align:center;color:#555;margin-top:40px;'>Made with love by Fahad Khan</p>", unsafe_allow_html=True)

import streamlit as st
import random

# Page setup
st.set_page_config(page_title="For Hira 💎", page_icon="💎", layout="centered")

# Beautiful pink background with emojis
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe6f0 0%, #ffd9ec 50%, #ffcce0 100%);
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    h1, h3 {
        font-family: 'Comic Sans MS', cursive, sans-serif;
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

# Mixed playful messages (English + Pashto + emojis)
no_messages = [
    "Are you sure? 😏",
    "Think again 💭",
    "That doesn’t sound right…",
    "Your heart says yes ❤️",
    "Wrong answer 😌",
    "Don’t break my heart 💔",
    "Makwa spai 🐶",
    "Tasra ba goram lewanai 🤪",
    "Sabar uka za drzam tasra ba goram 😜",
    "Ta bya no select ko 🙈",
    "Try again 💕",
    "I won’t let you say no 😎",
    "You know the answer 😘",
    "C’mon, admit it 💖",
    "Not convinced 😏",
    "I see what you did there 😌",
    "Your brain says no, heart says yes ❤️",
    "Nope, that’s wrong 😇",
    "Try harder 😅",
    "Your heart knows better 💓"
]

# Question
st.markdown("<h3 style='text-align:center;'>Do you love me?</h3>", unsafe_allow_html=True)

if not st.session_state.answered_yes:

    # Yes button always visible at center
    if st.button("Yes 💖", key="yes_button"):
        st.session_state.answered_yes = True

    # Vertical "teleport"
    vertical_space = random.randint(0, 10)
    for _ in range(vertical_space):
        st.write("\n")

    # Horizontal "run away" using random number of columns each click
    max_cols = 5  # More columns = more horizontal movement
    random_col_index = random.randint(0, max_cols - 1)
    cols = st.columns(max_cols)

    # No button appears in random column
    if cols[random_col_index].button("No 😢", key=f"no_button_{st.session_state.no_clicks}"):
        st.session_state.no_clicks += 1
        # Pick random message
        msg = random.choice(no_messages)
        st.warning(msg)

else:
    # End screen
    st.balloons()
    st.success("Thank you ❤️ I knew it! 🥰✨💎")

# Footer
st.markdown("<p style='text-align:center;color:#555;margin-top:40px;'>Made with love by Fahad Khan 💖💎</p>", unsafe_allow_html=True)

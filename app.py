import streamlit as st
import random

# Page setup
st.set_page_config(page_title="For Hira 💎", page_icon="💎", layout="wide")

# Beautiful pink gradient background with emojis
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

# Mixed English + Pashto messages
no_messages = [
    "Are you sure? 😏",
    "Think again 💭",
    "Makwa spai 🐶",
    "Tasra ba goram lewanai 🤪",
    "Sabar uka za drzam tasra ba goram 😜",
    "Ta bya no select ko 🙈",
    "I won’t let you say no 😎",
    "Try again 💕",
    "You know the answer 😘",
    "C’mon, admit it 💖",
    "Not convinced 😏",
    "Your heart knows better 💓",
    "Wrong answer 😌",
    "Don’t break my heart 💔",
    "I see what you did there 😌",
    "Your brain says no, heart says yes ❤️"
]

st.markdown("<h3 style='text-align:center;'>Do you love me?</h3>", unsafe_allow_html=True)

if not st.session_state.answered_yes:
    # Random vertical spacing before buttons
    vertical_space_no = random.randint(0, 8)
    vertical_space_yes = random.randint(0, 8)

    for _ in range(vertical_space_no):
        st.write("\n")

    # Horizontal movement using columns
    max_cols = 5
    no_col_idx = random.randint(0, max_cols - 1)
    yes_col_idx = no_col_idx  # Yes starts near No initially

    cols = st.columns(max_cols)
    # No button
    if cols[no_col_idx].button("No 😢", key=f"no_button_{st.session_state.no_clicks}"):
        st.session_state.no_clicks += 1
        msg = random.choice(no_messages)
        st.warning(msg)
        # Move Yes closer to No: random column near No
        yes_col_idx = max(0, min(max_cols - 1, no_col_idx + random.choice([-1, 0, 1])))
        # Add vertical spacing for Yes too
        vertical_space_yes = random.randint(0, 5)
        for _ in range(vertical_space_yes):
            st.write("\n")
        if cols[yes_col_idx].button("Yes 💖", key=f"yes_button_{st.session_state.no_clicks}"):
            st.session_state.answered_yes = True
    else:
        # Show Yes button in random vertical space
        for _ in range(vertical_space_yes):
            st.write("\n")
        if cols[yes_col_idx].button("Yes 💖", key="yes_button"):
            st.session_state.answered_yes = True

else:
    # End screen
    st.balloons()
    st.success("Thank you ❤️ I knew it! 🥰✨💎")

st.markdown("<p style='text-align:center;color:#555;margin-top:40px;'>Made with love by Fahad Khan 💖💎</p>", unsafe_allow_html=True)

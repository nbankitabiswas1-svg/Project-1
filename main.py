import streamlit as st
import random

st.set_page_config(
    page_title="Enchanted Dreamland",
    page_icon="🧚",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #170d30, #49265f, #17152f
    );
    color: #fff0ff;
}
h1, h2, h3, p, label {
    color: #fff0ff !important;
}
.stButton > button {
    background: #d7a8ff;
    color: #29143d;
    border-radius: 18px;
    border: none;
    padding: 10px 22px;
    font-weight: bold;
}
.stButton > button:hover {
    background: #ffc8e8;
    color: #29143d;
}
div[data-testid="stTextInput"] input {
    background: #fff0ff;
    color: #301641;
}
</style>
""", unsafe_allow_html=True)

st.title("🧚 Enchanted Dreamland")
st.subheader("✨ A little magic is waiting for you...")

st.write(
    "Welcome, little dreamer! "
    "The stars have been waiting for your arrival. 🌙"
)

name = st.text_input("💌 What shall we call you?")

power = st.selectbox(
    "🔮 Choose your magical power",
    ["Moon Magic 🌙", "Love Magic 💗",
     "Starlight ✨", "Nature Magic 🌿"]
)

if st.button("Reveal My Destiny ✨"):

    if name.strip() == "":
        st.warning("The fairies need your name first! 🧚")

    else:
        prophecies = {
            "Moon Magic 🌙": [
                "The moon will guide you through every darkness.",
                "A beautiful secret awaits you beneath the stars.",
                "Your quiet strength is your greatest magic."
            ],
            "Love Magic 💗": [
                "Your kindness will create a little miracle.",
                "A beautiful chapter of love awaits your heart.",
                "Never forget that you deserve a love that feels safe."
            ],
            "Starlight ✨": [
                "You were born to chase extraordinary dreams.",
                "A surprising adventure is closer than you think.",
                "Your brightest days are still waiting to unfold."
            ],
            "Nature Magic 🌿": [
                "Like a flower, you will bloom in your own time.",
                "Peace and wonderful discoveries await you.",
                "Even the smallest seed can grow into a mighty tree."
            ]
        }

        st.balloons()
        st.markdown("---")
        st.header(f"🌷 Welcome to your destiny, {name}!")
        st.write(f"Your chosen power: **{power}**")

        st.success(
            "📜 Your Magical Prophecy\n\n"
            + random.choice(prophecies[power])
        )

        st.caption(
            "✨ Remember: your real magic is what you "
            "choose to do with your life. ✨"
        )

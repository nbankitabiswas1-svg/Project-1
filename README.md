import streamlit as st
import random

st.set_page_config(
    page_title="A Little Magic for My Bestie 💗",
    page_icon="💖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffd6eb, #f5caff, #ffe6f2);
    color: #a02d70;
}

h1 {
    color: #d63384;
    text-align: center;
    text-shadow: 0 0 15px #ff8ac4;
}

p, label {
    color: #9c2870 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #ff69b4, #da70d6);
    color: white;
    border: 2px solid white;
    border-radius: 30px;
    padding: 12px;
    font-size: 17px;
    box-shadow: 0 0 18px #ff69b4;
    transition: 0.3s;
}

.stButton > button:hover {
    box-shadow: 0 0 30px #ff1493;
    transform: scale(1.03);
}

.magic-popup {
    background: rgba(255, 255, 255, 0.88);
    border: 3px solid #ff9ed2;
    border-radius: 25px;
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0 0 30px #ff8ac4;
    animation: appear 0.8s ease-out;
    color: #b52b78;
    font-size: 21px;
}

@keyframes appear {
    from {opacity: 0; transform: scale(0.7);}
    to {opacity: 1; transform: scale(1);}
}

.footer {
    text-align: center;
    color: #c13584;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

messages = {
    "Sad 😢": [
        "My precious girl, it's okay to cry. You don't have to be strong every second. If I were there, I'd hug you until your heart felt lighter. 💗🫂",
        "Hey princess! 🌷 This is just a difficult chapter, not your whole story. Better days are coming, and you deserve every bit of happiness.",
        "A little fairy told me that someone very special needs a hug today. Guess who? YOU! Sending you a million magical hugs! 🧚‍♀️💕"
    ],
    "Lonely 🥺": [
        "Close your eyes for a second, bestie. Imagine me sitting beside you, holding your hand and saying, 'I'm so glad you exist.' 💞",
        "Even on the days you feel forgotten, please remember that you are a beautiful soul who deserves love, care and kindness. 🌙💗"
    ],
    "Stressed 😵‍💫": [
        "Shhh, my little star. ✨ You don't have to figure out your entire life tonight. Take a breath. One little step at a time.",
        "Official royal decree 👑: My princess is allowed to rest, eat something yummy and stop worrying for five minutes! 💕"
    ],
    "Unmotivated 😴": [
        "You are a little star, and stars shine even in the darkest skies. Keep going, my girl. I believe in you! 🌟",
        "Your progress doesn't have to be perfect to be beautiful. Get up gently and try again. I'm cheering for you! 🎀"
    ],
    "Angry 😤": [
        "Breathe in, breathe out, princess. 🌸 You can feel everything without letting one difficult moment control your whole day.",
        "Sending you a pink bubble of peace! 🫧 Leave the stress outside for a moment. You deserve a little calm."
    ],
    "Happy 🥰": [
        "ALERT! 🚨 The world's cutest smile has been spotted! Please keep smiling, bestie. You make ordinary days magical! 💖",
        "If happiness were glitter, you'd have enough to decorate the entire universe! ✨🌷"
    ]
}

st.markdown("<h1>🩷 A Little Magic for You 🩷</h1>",
            unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;font-size:18px;'>"
    "✨ A tiny magical world made just for you ✨</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;font-size:32px;'>"
    "🦋 💗 🧚‍♀️ 💗 🦋</p>",
    unsafe_allow_html=True
)

st.write("")

mood = st.selectbox(
    "🌸 Tell your fairy how you're feeling...",
    list(messages.keys())
)

if st.button("✨ Open your magical surprise 💌",
             use_container_width=True):
    quote = random.choice(messages[mood])

    st.session_state["message"] = quote
    st.session_state["mood"] = mood

if "message" in st.session_state:
    st.markdown(
        f"""
        <div class="magic-popup">
            <div style="font-size:38px;">🧚‍♀️ ✨ 💗 ✨</div>
            <h3 style="color:#e754a1;">
                A little message just for you!
            </h3>
            <p>{st.session_state["message"]}</p>
            <div style="font-size:30px;">🦋 🌷 💖 🌷 🦋</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("💖 Another magical message"):
        st.session_state["message"] = random.choice(
            messages[st.session_state["mood"]]
        )
        st.rerun()

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🌙 Made with a little pink magic and lots of love 🌙<br>
        Never forget how special you are, bestie. 💗
    </div>
    """,
    unsafe_allow_html=True
)

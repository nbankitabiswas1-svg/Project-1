import streamlit as st
import random
import os

st.set_page_config(
    page_title="My Werewolf Prince",
    page_icon="🐺",
    layout="centered"
)

# Fantasy appearance
st.markdown("""
<style>
.stApp {
    background: linear-gradient(160deg, #100d20, #302044, #101426);
    color: #fff1ff;
}
h1, h2, p, label {
    color: #fff1ff !important;
}
[data-testid="stChatMessage"] {
    background: rgba(180, 140, 220, 0.12);
    border: 1px solid #72558c;
    border-radius: 18px;
    padding: 12px;
}
.stChatInput textarea {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌙 My Werewolf Prince")
st.caption("A moonlit castle. A dangerous prince. A love story.")

# Add werewolf.png to the same folder as main.py
if os.path.exists("werewolf.png"):
    st.image("werewolf.png", use_container_width=True)
else:
    st.markdown("## 🐺 Prince Lucien")
    st.caption("Upload a fantasy werewolf portrait as werewolf.png")

st.markdown("### 🖤 Your future husband")
st.write("Silver-haired Werewolf King • Romantic • Playful")

# Dialogue rules
def prince_reply(message):
    text = message.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello, darling! ❤️ My little wife, ready to marry me?",
            "There you are, my princess! I've been waiting all day for you.",
            "Come here, sweetheart. Your wolf missed you terribly. 🐺"
        ])

    elif any(word in text for word in ["marry", "wedding", "wife"]):
        return random.choice([
            "YES! 💍 I've already imagined you walking towards me in a moonlit wedding dress!",
            "My little wife! Say yes, darling, and I'll give you the moonlit castle.",
            "*He kneels and opens a velvet ring box.* Will you marry me, my princess?"
        ])

    elif any(word in text for word in ["sad", "cry", "hurt", "upset"]):
        return random.choice([
            "Oh, my little princess. Who hurt you? Come here. You don't have to hide your tears from me. ❤️",
            "*He gently opens his arms.* Come to me, darling. Tell me everything. I'm listening.",
            "My little wife, you deserve tenderness. Tell me what's troubling your heart."
        ])

    elif any(word in text for word in ["love", "miss", "kiss"]):
        return random.choice([
            "I love you, darling. Now come here and give your wolf a kiss. 💋",
            "You have no idea what you do to my heart, little princess.",
            "*He smiles and kisses your forehead.* My favourite person in every universe."
        ])

    elif any(word in text for word in ["angry", "mad", "jealous"]):
        return random.choice([
            "Oh, sweetheart. Tell me what happened. I want to understand.",
            "*His ears twitch.* My little princess is angry with me? Tell me why, darling.",
            "Come on, love. Let's talk about it. I don't want you feeling unheard."
        ])

    elif any(word in text for word in ["bye", "goodnight", "sleep"]):
        return random.choice([
            "Goodnight, my little moonbeam. Dream of our castle. 🌙",
            "Already leaving me, darling? *He smiles.* Sleep well, my princess.",
            "Sweet dreams, my love. I'll be right here when you return."
        ])

    else:
        return random.choice([
            "Really, darling? ❤️ Tell me more. Your wolf is listening.",
            "*He tilts his head, his amber eyes watching you.* And what else, my little princess?",
            "Come sit beside me, sweetheart. I want to hear everything.",
            "*He takes your hand and smiles.* You know you can tell me anything, don't you?"
        ])

# Start the conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello, darling. 💍 My little wife, are you ready to marry me? I've been waiting for you all evening."
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    avatar = "🐺" if msg["role"] == "assistant" else "💗"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# Let the user type anything
user_text = st.chat_input("Say something to your werewolf prince...")

if user_text:
    st.session_state.messages.append({
        "role": "user",
        "content": user_text
    })

    with st.chat_message("user", avatar="💗"):
        st.markdown(user_text)

    answer = prince_reply(user_text)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant", avatar="🐺"):
        st.markdown(answer)

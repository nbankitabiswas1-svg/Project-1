import streamlit as st
import random

st.set_page_config(
    page_title="The Monster King's Queen",
    page_icon="👑",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(160deg, #100812, #26101f, #100d20);
    color: #f8e5ef;
}
h1, h2, h3, p, label, .stMarkdown {
    color: #f8e5ef;
}
div.stButton > button {
    background: #54172f;
    color: #ffe8f0;
    border: 1px solid #c59a63;
    border-radius: 14px;
}
div.stButton > button:hover {
    background: #762746;
    border-color: #f5d49a;
}
.letter {
    background: #241323;
    border: 1px solid #b58a65;
    border-radius: 16px;
    padding: 20px;
    margin: 12px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("👑 The Monster King's Queen")
st.markdown(
    "*Two kingdoms. One arranged marriage. "
    "One monster who learned to love.*"
)

st.markdown("---")

st.markdown("""
<div class="letter">
<h3>💌 A letter from your husband</h3>
<p>To my Queen,</p>
<p>The entire world calls me a monster.
They say I have no heart, no mercy, no love.</p>
<p>Perhaps they were right. Until you.</p>
<p>You are the only person who dares to
argue with me, steal my cloak, and fall asleep
in my throne room as if you own the world.</p>
<p>You do, little queen. At least, my world.</p>
<p>Yours, even when the kingdoms fall,<br>
<strong>Your Monster King 🖤</strong></p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "The great doors of the throne room open. "
                "The feared King rises from his black throne. "
                "His cold expression softens when he sees you. "
                "\n\n'You are finally here, my queen. "
                "Come here. I have been waiting for you.'"
            )
        }
    ]

def king_reply(message):
    text = message.lower()

    if any(word in text for word in
           ["hello", "hi", "hey", "darling"]):
        return random.choice([
            "There you are, my little queen. "
            "Do you know how many times I have looked at that door, "
            "waiting for you? Come here. 🖤",
            "Hello, wife. The entire royal council fears me, "
            "yet I have been waiting like a fool for one message "
            "from you.",
            "My queen! Finally. I was about to send the royal guards "
            "to ask why my favourite person had forgotten me."
        ])

    if any(word in text for word in
           ["how are you", "how r u", "are you okay"]):
        return random.choice([
            "The kingdom is troublesome, the council is unbearable, "
            "and I have a mountain of work. But you are here now, "
            "so tell me about your day, my heart.",
            "I was a monster before breakfast, a tyrant by noon, "
            "and a miserable husband missing his wife by evening. "
            "I am perfectly fine, darling. Come sit beside me.",
            "Better now that my queen has asked. And you? "
            "Tell me honestly. I want to hear everything."
        ])

    if any(word in text for word in
           ["love you", "i love u", "i love you"]):
        return (
            "The King goes completely still. The man who has "
            "never feared a battlefield looks at you as though "
            "you hold his entire soul.\n\n"
            "'Say it again, little queen. I have conquered "
            "kingdoms, but nothing has ever conquered me "
            "the way your love has.' ❤️"
        )

    if any(word in text for word in
           ["miss you", "miss u", "where are you"]):
        return (
            "He puts down his crown and opens his arms.\n\n"
            "'I am right here, my wife. I miss you even when "
            "you are only one corridor away. Come to me. "
            "Let the kingdoms wait.'"
        )

    if any(word in text for word in
           ["angry", "mad", "hate you", "upset"]):
        return (
            "His expression changes. He kneels before you, "
            "setting his crown aside.\n\n"
            "'Look at me, my queen. I will not command you "
            "to forgive me. Tell me what I did wrong. "
            "You deserve to be heard, especially by me.'"
        )

    if any(word in text for word in
           ["sorry", "apologize", "forgive"]):
        return (
            "'Come here, my love.' His voice becomes quiet. "
            "'You never need to be afraid of telling me the truth. "
            "We are husband and wife, not enemies on a battlefield.'"
        )

    if any(word in text for word in
           ["kiss", "hug", "cuddle"]):
        return (
            "The fearsome King dismisses his guards with one look "
            "and draws you into his warm embrace.\n\n"
            "'Five minutes, you said? No, my queen. "
            "I am keeping you here until you stop looking so "
            "adorably tired.' 💋"
        )

    if any(word in text for word in
           ["goodnight", "good night", "sleep"]):
        return (
            "He pulls a velvet blanket over you and brushes "
            "a kiss against your forehead.\n\n"
            "'Sleep, my little queen. I shall be right beside you. "
            "Let the world tremble outside these walls. "
            "Tonight, you need only rest.' 🌙"
        )

    if any(word in text for word in
           ["queen", "kingdom", "king"]):
        return (
            "'Your kingdom and mine may have been enemies "
            "for a hundred years,' he says, taking your hand. "
            "'But you are my wife. No crown, treaty, or throne "
            "will ever matter more to me than you.'"
        )

    return random.choice([
        "The King listens carefully, his usual cold gaze "
        "softening. 'Go on, my queen. I am listening.'",
        "'You know,' he murmurs, 'I used to silence every "
        "person who entered this room. Now I wait for you "
        "to tell me stories. Look what you have done to me.'",
        "He reaches for your hand. 'Tell me more, darling. "
        "I want to know what is happening inside that "
        "clever little head of yours.'",
        "'The royal council can wait,' he declares, closing "
        "his book. 'My wife is speaking, and that is far "
        "more important.'"
    ])

st.markdown("### 🕯️ Speak to your husband")
st.caption(
    "You are the Queen of the neighbouring kingdom. "
    "He is waiting for your message."
)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Write a message to your king..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    reply = king_reply(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    st.rerun()

st.markdown("---")

st.markdown("### 💌 A secret from the Monster King")

if st.button("Read his most secret letter"):
    st.markdown("""
    <div class="letter">
    <p>My beloved wife,</p>
    <p>I was taught that a king must never bend,
    never apologise, and never show weakness.</p>
    <p>Then you looked at me and asked why I was so cruel.</p>
    <p>No one had ever asked me to be better.
    They had only asked me to be stronger.</p>
    <p>You did not remove the monster from me in a day.
    You taught me that I could choose what kind of man
    I wanted to become.</p>
    <p>If the world remembers me as a monster,
    let it. You will know the man who loves you.</p>
    <p>Forever yours,<br><strong>Your King 🖤</strong></p>
    </div>
    """, unsafe_allow_html=True)

if st.button("🌹 Let him send me roses"):
    st.balloons()
    st.success(
        "A thousand crimson roses arrive at your castle. "
        "Their card reads: 'For my queen, who made my "
        "dark world bloom.' — Your devoted husband"
    )

if st.button("🔄 Begin our story again"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "The doors of the throne room open. "
                "'My queen, you have returned. "
                "Come here. I have missed you.'"
            )
        }
    ]
    st.rerun()

st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>"
    "🖤 Two crowns. Two kingdoms. One love. 🖤"
    "</p>",
    unsafe_allow_html=True
)

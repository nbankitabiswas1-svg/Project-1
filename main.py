import streamlit as st
import random
import time

st.set_page_config(
    page_title="Haunted Halloween Night",
    page_icon="🎃",
    layout="wide"
)

# -------------------- STYLE --------------------

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top, #39204e 0%, #160d25 48%, #080711 100%);
    color: #fff0dc;
}
h1, h2, h3 {
    color: #ff9e35 !important;
}
p, label, li {
    color: #f6e9ff;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1c102c, #090711);
}
div.stButton > button {
    background: linear-gradient(135deg, #ff8c24, #e34816);
    color: white;
    border: 1px solid #ffbf69;
    border-radius: 14px;
    font-weight: bold;
    min-height: 45px;
    transition: 0.2s;
}
div.stButton > button:hover {
    background: #ffb347;
    color: #180b20;
    border: 1px solid white;
}
.haunted-banner {
    background: linear-gradient(120deg, #351446, #171024, #4b1e2d);
    border: 1px solid #a45a9c;
    border-radius: 22px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 0 30px #612b6644;
}
.big-emoji {
    font-size: 65px;
    text-align: center;
}
.ghost-card {
    background: #241633;
    border: 1px solid #75458b;
    padding: 20px;
    border-radius: 18px;
    margin: 8px 0;
}
.story {
    background: #100d1b;
    border-left: 5px solid #ff8c24;
    padding: 20px;
    border-radius: 10px;
    line-height: 1.9;
}
.small-note {
    color: #cbb5df;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------- GAME DATA --------------------

if "candy" not in st.session_state:
    st.session_state.candy = 0
if "visited" not in st.session_state:
    st.session_state.visited = []
if "chat" not in st.session_state:
    st.session_state.chat = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False
if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = None
if "story" not in st.session_state:
    st.session_state.story = None
if "fortune" not in st.session_state:
    st.session_state.fortune = None

# -------------------- SIDEBAR --------------------

st.sidebar.markdown("# 🎃 HALLOWEEN")
st.sidebar.caption("Your midnight adventure begins...")

page = st.sidebar.radio(
    "Choose your destination",
    [
        "🏰 Haunted Home",
        "🚪 Explore the Mansion",
        "👻 Talk to a Ghost",
        "🔮 Fortune Teller",
        "📖 Spooky Story",
        "🍬 Trick or Treat",
        "🧠 Halloween Quiz",
        "🦇 Creature Gallery"
    ]
)

st.sidebar.divider()
st.sidebar.metric("🍬 Candy collected", st.session_state.candy)
st.sidebar.write(
    f"🚪 Rooms explored: {len(st.session_state.visited)}/5"
)
st.sidebar.caption("Best experienced after dark. 🌙")

# -------------------- HOME --------------------

if page == "🏰 Haunted Home":

    st.markdown("""
    <div class="haunted-banner">
        <div style="font-size:75px">🎃 🦇 👻</div>
        <h1 style="font-size:43px">HAUNTED HALLOWEEN NIGHT</h1>
        <h3 style="color:#e9b4ff !important">
            One night. One haunted mansion. Countless secrets.
        </h3>
        <p>
        The moon is rising. The gates are opening.
        Something inside the mansion knows your name...
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    a, b, c = st.columns(3)

    with a:
        st.markdown("### 🏚️")
        st.markdown("**Explore**")
        st.write("Unlock the secrets hidden inside five mysterious rooms.")

    with b:
        st.markdown("### 👻")
        st.markdown("**Meet the Spirits**")
        st.write("Speak with the ghost who has been waiting for you.")

    with c:
        st.markdown("### 🔮")
        st.markdown("**Discover Your Fate**")
        st.write("Ask the fortune teller what awaits you at midnight.")

    st.divider()
    st.subheader("🌙 The Midnight Invitation")

    st.write("""
    Dear visitor,

    You have been invited to Blackthorn Manor.

    At midnight, the clock will strike thirteen times.
    A door that has been locked for a hundred years will open.
    Your mission is to explore the mansion, collect enchanted candy,
    uncover a ghost's secret, and survive the Halloween night.

    **Will you enter?**
    """)

    if st.button("🕯️ ENTER THE HAUNTED MANSION", use_container_width=True):
        st.session_state.visited.append("Entrance Hall")
        st.success("The iron gates creak open. Welcome to Blackthorn Manor!")
        st.balloons()

    st.markdown(
        '<p class="small-note">October 31 • The witching hour approaches...</p>',
        unsafe_allow_html=True
    )

# -------------------- MANSION --------------------

elif page == "🚪 Explore the Mansion":

    st.title("🏚️ Explore Blackthorn Manor")
    st.write("Choose a door. Every room holds a different secret.")

    rooms = {
        "🕯️ Candlelit Hall": (
            "A thousand candles flicker, although there is no wind. "
            "A portrait follows your movements with its eyes."
        ),
        "🪞 The Mirror Room": (
            "Your reflection smiles a second later than you do. "
            "Behind the glass, a shadow raises its hand."
        ),
        "📚 Forbidden Library": (
            "Dusty books whisper forgotten names. One book opens "
            "by itself to a page describing tonight's visitor."
        ),
        "⚰️ The Forgotten Crypt": (
            "Cold mist curls around ancient stone coffins. "
            "A silver key glows beneath a cracked tombstone."
        ),
        "🧙 The Witch's Kitchen": (
            "A purple potion bubbles in a copper cauldron. "
            "A black cat guards a jar filled with glowing stars."
        )
    }

    for room, description in rooms.items():
        with st.expander(room):
            st.write(description)

            if st.button("Explore this room", key=room):
                if room not in st.session_state.visited:
                    st.session_state.visited.append(room)
                    st.session_state.candy += random.randint(1, 3)
                    st.success("Secret discovered! You found enchanted candy. 🍬")
                else:
                    st.info("You've already explored this room.")

    st.divider()
    st.write("**Your discoveries:**")
    if st.session_state.visited:
        for room in st.session_state.visited:
            st.write("✅ " + room)
    else:
        st.write("No rooms explored yet. Pick a door!")

# -------------------- GHOST CHAT --------------------

elif page == "👻 Talk to a Ghost":

    st.title("👻 Meet Casper, the Midnight Ghost")

    st.markdown("""
    <div class="ghost-card">
        <div class="big-emoji">👻</div>
        <h2 style="text-align:center">CASPER</h2>
        <p style="text-align:center">
        "Oh! A visitor! I've been alone for 200 years.
        Please don't run away. I only haunt people on weekends."
        </p>
    </div>
    """, unsafe_allow_html=True)

    for who, message in st.session_state.chat:
        st.markdown(f"**{who}:** {message}")

    with st.form("ghost_chat_form", clear_on_submit=True):
        user_message = st.text_input(
            "Say something to Casper...",
            placeholder="Hello, Casper! What's your secret?"
        )
        submitted = st.form_submit_button("Send message 👻")

    if submitted and user_message.strip():
        st.session_state.chat.append(("You", user_message))

        msg = user_message.lower()

        if any(word in msg for word in ["hello", "hi", "hey"]):
            reply = "Hello, little mortal! Welcome to my haunted home. 👻"
        elif any(word in msg for word in ["secret", "mystery", "hide"]):
            reply = "The mirror room hides a secret. Never trust the reflection!"
        elif any(word in msg for word in ["scared", "afraid", "fear"]):
            reply = "Don't be afraid. Even ghosts were beginners once!"
        elif any(word in msg for word in ["love", "friend", "lonely"]):
            reply = "Even a ghost needs a friend. Stay a little longer? 💜"
        elif any(word in msg for word in ["vampire", "dracula", "blood"]):
            reply = "The vampire upstairs is terribly dramatic. He sleeps in a coffin with velvet pillows."
        elif any(word in msg for word in ["bye", "goodbye", "leave"]):
            reply = "Farewell, brave visitor! The gates will remember you."
        elif "name" in msg:
            reply = "I'm Casper Blackthorn, the friendliest ghost in this manor!"
        elif "why" in msg:
            reply = "Some mysteries are older than the moon. Perhaps you'll discover the answer."
        else:
            reply = random.choice([
                "Ooooh! That's an interesting thought, little mortal.",
                "The spirits are whispering, but I can't quite hear them.",
                "Try exploring the mirror room. It might answer your question.",
                "Boo! Sorry, I still haven't mastered a proper haunting.",
                "Ask me about the manor's secret. I know more than I reveal!"
            ])

        st.session_state.chat.append(("Casper 👻", reply))
        st.rerun()

    if st.button("🧹 Clear conversation"):
        st.session_state.chat = []
        st.rerun()

    st.caption("Casper uses a collection of programmed replies, not a live AI model.")

# -------------------- FORTUNE TELLER --------------------

elif page == "🔮 Fortune Teller":

    st.title("🔮 Madame Raven's Fortune Tent")

    st.markdown("""
    <div class="big-emoji">🔮 🕯️ 🔮</div>
    <div class="ghost-card">
    <p style="text-align:center">
    "Come closer, dear visitor. The stars have been waiting
    to reveal something mysterious about your Halloween night."
    </p>
    </div>
    """, unsafe_allow_html=True)

    topic = st.selectbox(
        "What would you like to discover?",
        ["Your Halloween destiny", "Love & friendship",
         "Courage & adventure", "A mysterious secret"]
    )

    fortunes = {
        "Your Halloween destiny": [
            "A mysterious door will open when you least expect it.",
            "Your courage will reveal a path hidden from everyone else.",
            "The moon has chosen you to discover the manor's secret."
        ],
        "Love & friendship": [
            "A small act of kindness may create an unforgettable memory.",
            "Someone may surprise you with unexpected warmth.",
            "The strongest bonds are built through honesty and care."
        ],
        "Courage & adventure": [
            "The room you fear most may hold your greatest discovery.",
            "A brave choice can turn a frightening night into an adventure.",
            "You are capable of more than your fears suggest."
        ],
        "A mysterious secret": [
            "Look behind the oldest portrait in the mansion.",
            "Listen carefully when the clock strikes midnight.",
            "The answer may be hiding in a place you have already visited."
        ]
    }

    if st.button("✨ Reveal my fortune", use_container_width=True):
        st.session_state.fortune = random.choice(fortunes[topic])

    if st.session_state.fortune:
        st.markdown(
            f'<div class="ghost-card"><h3>✨ The Crystal Speaks</h3>'
            f'<p>{st.session_state.fortune}</p></div>',
            unsafe_allow_html=True
        )
        st.caption("A playful Halloween fortune, for entertainment.")

# -------------------- SPOOKY STORY --------------------

elif page == "📖 Spooky Story":

    st.title("📖 The Book of Midnight Tales")

    setting = st.selectbox(
        "Choose your nightmare",
        ["The Haunted Mansion", "The Enchanted Forest",
         "The Abandoned School", "The Vampire's Castle"]
    )

    hero = st.text_input("Your character's name", value="Ankita")

    if st.button("🕯️ Write my spooky story", use_container_width=True):

        openings = {
            "The Haunted Mansion": (
                f"On Halloween night, {hero} received a black envelope "
                "with no address. Inside was a key and a note: "
                "'Come home before midnight.' The strange thing was, "
                "the mansion in the photograph belonged to nobody alive."
            ),
            "The Enchanted Forest": (
                f"{hero} stepped into a forest where the trees whispered "
                "secrets. Blue lights floated between the branches, "
                "and every path led to the same ancient oak."
            ),
            "The Abandoned School": (
                f"At 11:59 PM, {hero} heard a school bell ring inside "
                "an abandoned building. Every classroom was empty, "
                "except one desk with a fresh name carved into it."
            ),
            "The Vampire's Castle": (
                f"{hero} arrived at a castle beneath a crimson moon. "
                "Its mysterious owner offered a warm welcome, "
                "but every mirror in the castle was covered."
            )
        }

        endings = [
            "At the final moment, the hidden door opened. Behind it "
            "was a room filled with hundreds of clocks, all ticking "
            "backwards. One clock suddenly stopped. It bore "
            "your character's name.",

            "A shadow emerged from the darkness. It wasn't a monster, "
            "but a guardian who had been waiting for someone brave "
            "enough to uncover the truth. The secret was finally free.",

            "The moon disappeared behind a cloud. When the light "
            "returned, the entire place was gone. In your pocket "
            "lay a silver key, warm to the touch."
        ]

        st.session_state.story = (
            openings[setting] + "\n\n" + random.choice(endings)
        )

    if st.session_state.story:
        st.markdown(
            '<div class="story">' +
            st.session_state.story.replace("\n\n", "<br/><br/>") +
            '</div>',
            unsafe_allow_html=True
        )

# -------------------- TRICK OR TREAT --------------------

elif page == "🍬 Trick or Treat":

    st.title("🍬 Trick or Treat Adventure")
    st.write("Visit mysterious Halloween houses and see what you receive.")

    st.metric("Your candy bag", f"{st.session_state.candy} 🍬")

    houses = {
        "🏠 The Pumpkin Cottage": [
            ("The witch gives you a handful of candy!", 5),
            ("A friendly skeleton hands you two sweets.", 2),
            ("A pumpkin opens its mouth and says BOO!", 0)
        ],
        "🏚️ The Crooked House": [
            ("A ghost drops a giant candy bar into your bag.", 4),
            ("You find three mysterious chocolates.", 3),
            ("A vampire offers you a riddle instead of candy.", 0)
        ],
        "🏰 The Vampire's Castle": [
            ("The vampire gives you a royal candy treasure!", 8),
            ("A bat delivers a tiny candy pumpkin.", 2),
            ("The count laughs and gives you... one raisin.", 1)
        ]
    }

    for house, rewards in houses.items():
        with st.expander(house):
            if st.button("Knock on the door 🚪", key=house):
                message, reward = random.choice(rewards)
                st.session_state.candy += reward
                st.write(message)
                if reward:
                    st.success(f"You collected {reward} candy!")
                else:
                    st.warning("No candy this time. Try another house!")
                st.rerun()

    st.divider()
    st.subheader("🏆 Candy Collector's Rank")

    candy = st.session_state.candy
    if candy >= 30:
        st.success("👑 Halloween Legend — the entire town knows your name!")
    elif candy >= 15:
        st.success("🧙 Master Trick-or-Treater — impressive collection!")
    elif candy >= 5:
        st.info("🦇 Candy Explorer — keep knocking!")
    else:
        st.info("🎃 Halloween Rookie — your adventure has just begun!")

# -------------------- QUIZ --------------------

elif page == "🧠 Halloween Quiz":

    st.title("🧠 Halloween Knowledge Challenge")

    questions = [
        {
            "q": "Which vegetable is traditionally carved into a jack-o'-lantern?",
            "options": ["Watermelon", "Pumpkin", "Cucumber", "Potato"],
            "answer": "Pumpkin",
            "fact": "Pumpkins are carved into glowing Halloween lanterns."
        },
        {
            "q": "Which creature is traditionally associated with transforming into a bat?",
            "options": ["Werewolf", "Witch", "Vampire", "Zombie"],
            "answer": "Vampire",
            "fact": "Vampires in folklore and fiction are often associated with bats."
        },
        {
            "q": "What date is Halloween celebrated on?",
            "options": ["October 13", "October 31", "November 1", "December 31"],
            "answer": "October 31",
            "fact": "Halloween takes place on October 31 each year."
        },
        {
            "q": "What do trick-or-treaters traditionally collect?",
            "options": ["Flowers", "Coins only", "Candy", "Books"],
            "answer": "Candy",
            "fact": "Candy and other treats are traditional Halloween rewards."
        },
        {
            "q": "What is a group of witches commonly called in folklore?",
            "options": ["A coven", "A colony", "A fleet", "A pack"],
            "answer": "A coven",
            "fact": "A coven is a gathering of witches in folklore and fiction."
        }
    ]

    if st.session_state.quiz_question is None:
        st.session_state.quiz_question = random.sample(questions, 5)

    if not st.session_state.quiz_done:
        with st.form("halloween_quiz"):
            answers = []
            for i, question in enumerate(st.session_state.quiz_question):
                st.markdown(f"### Question {i + 1}")
                st.write(question["q"])
                answers.append(
                    st.radio(
                        "Choose your answer:",
                        question["options"],
                        key=f"quiz_{i}"
                    )
                )

            submitted = st.form_submit_button("🦇 Submit my answers")

        if submitted:
            score = 0
            for question, answer in zip(
                st.session_state.quiz_question, answers
            ):
                if answer == question["answer"]:
                    score += 1

            st.session_state.quiz_score = score
            st.session_state.quiz_done = True
            st.rerun()

    else:
        score = st.session_state.quiz_score
        st.markdown(f"## 🎃 Your score: {score}/5")

        if score == 5:
            st.success("Halloween Genius! You know your spooky facts.")
        elif score >= 3:
            st.info("Well done! You're becoming a Halloween expert.")
        else:
            st.warning("The spirits challenge you to try again!")

        for i, question in enumerate(st.session_state.quiz_question):
            st.write(f"**{i + 1}. {question['q']}**")
            st.write(f"Correct answer: {question['answer']}")
            st.caption(question["fact"])

        if st.button("🔄 Play again"):
            st.session_state.quiz_question = random.sample(questions, 5)
            st.session_state.quiz_done = False
            st.session_state.quiz_score = 0
            st.rerun()

# -------------------- CREATURE GALLERY --------------------

elif page == "🦇 Creature Gallery":

    st.title("🦇 The Creatures of Halloween")
    st.write("Discover the legends that haunt Blackthorn Manor.")

    creatures = [
        ("🧛", "The Vampire", "Elegant, mysterious, and centuries old.",
         "Secret ability: Hypnotic charm."),
        ("🐺", "The Werewolf", "A fierce guardian beneath the full moon.",
         "Secret ability: Supernatural strength."),
        ("👻", "The Ghost", "A wandering spirit with unfinished business.",
         "Secret ability: Passing through walls."),
        ("🧙", "The Witch", "A keeper of ancient spells and strange potions.",
         "Secret ability: Enchanted magic."),
        ("🧟", "The Zombie", "A slow-moving visitor from beyond the grave.",
         "Secret ability: Never giving up."),
        ("🦇", "The Shadow Bat", "A silent creature that guards the towers.",
         "Secret ability: Disappearing into darkness.")
    ]

    for i in range(0, len(creatures), 2):
        left, right = st.columns(2)
        for column, creature in zip(
            [left, right], creatures[i:i + 2]
        ):
            emoji, name, description, ability = creature
            with column:
                st.markdown(
                    f'<div class="ghost-card">'
                    f'<div class="big-emoji">{emoji}</div>'
                    f'<h3 style="text-align:center">{name}</h3>'
                    f'<p>{description}</p>'
                    f'<p><b>{ability}</b></p>'
                    f'</div>',
                    unsafe_allow_html=True
                )

    st.divider()
    st.subheader("🌕 Choose your Halloween identity")

    creature_choice = st.selectbox(
        "Which creature would you be?",
        [c[1] for c in creatures]
    )

    if st.button("Reveal my creature identity"):
        selected = next(c for c in creatures if c[1] == creature_choice)
        st.success(
            f"You are {selected[1]}! {selected[2]} {selected[3]}"
        )

# -------------------- FOOTER --------------------

st.sidebar.divider()
st.sidebar.caption("🕸️ Blackthorn Manor • Halloween Edition")
st.sidebar.caption("Created with Python + Streamlit")

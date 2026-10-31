import streamlit as st
import random
import time

st.set_page_config(page_title="Fae Hollow • Fairy Whimsical", page_icon="🧚", layout="wide")

# --- Fairy Whimsical Theme ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative&family=Quicksand:wght@300;400&display=swap');
.stApp {
  background: radial-gradient(circle at top, #fff8fd 0%, #f3e8ff 30%, #e0f2fe 70%, #fef9c3 100%);
  color: #4a3f5a;
}
h1, h2, h3 { font-family: 'Cinzel Decorative', cursive; color: #7c5cbf !important; }
.card {
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.9);
  padding: 24px; border-radius: 24px;
  box-shadow: 0 10px 30px rgba(124,92,191,0.15);
}
.stButton>button {
  background: linear-gradient(90deg, #d8b4fe, #f0abfc, #a5f3fc);
  color: #4a3f5a; border: none; border-radius: 30px;
  font-weight: 600; padding: 10px 24px;
}
.stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 15px #f0abfc; }
</style>
""", unsafe_allow_html=True)

if 'stardust' not in st.session_state: st.session_state.stardust = 44
if 'wings' not in st.session_state: st.session_state.wings = []

# Sidebar
with st.sidebar:
    st.markdown("# 🧚 Fae Hollow")
    st.caption("where wishes grow like wildflowers...")
    page = st.radio("Wander to", ["Enchanted Home", "Fairy Name Ritual", "Whisper to a Fae", "Potion Garden", "Dress Up - Fairy Queen", "Starlight Wishes", "Creature Friends"], label_visibility="collapsed")
    st.markdown("---")
    st.metric("✨ Stardust collected", st.session_state.stardust)
    st.write("🎀 Wings:", ", ".join(st.session_state.wings) if st.session_state.wings else "none yet")
    st.caption("Best experienced at golden hour")

# Header
st.markdown("<h1 style='text-align:center'>Welcome to Fae Hollow, darling fairy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-family:Quicksand'>The air smells like peach tea & moss. The fairies left you an invitation.</p>", unsafe_allow_html=True)

# Pages
if page == "Enchanted Home":
    col1, col2 = st.columns([1.2,1])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🌙 The Midnight Petal Invitation")
        st.write("Dearest human, You have been invited to the hollow where time folds like silk. At twilight, the mushrooms glow. A tiny door you missed as a child will open again.")
        st.write("Collect stardust, name your wings, and let the forest remember you.")
        if st.button("ENTER THE HOLLOW ✨ →"):
            st.session_state.stardust += 5
            st.balloons()
            st.success("The moss opens. A circle of fireflies guides you in...")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("#### Today's Meadow Mood")
        mood = random.choice(["Soft & sleepy", "Giggly & glittery", "Wistful & wise", "Wildflower wild"])
        st.info(f"🌸 {mood} — perfect for collecting dewdrops")

elif page == "Fairy Name Ritual":
    st.markdown("### 🪄 Your Fairy Name")
    human = st.text_input("Your human name", placeholder="e.g. Aisha")
    vibe = st.select_slider("Choose your vibe", options=["moonlit", "sun-kissed", "mossy", "stardust", "honeyed"])
    if st.button("Reveal my name"):
        first = ["Lumi", "Elowen", "Sora", "Faye", "Aeri", "Mabel"]
        last = ["Petalwhisper", "Dewdance", "Starling", "Briarlight", "Honeythorn", "Wisp"]

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ankita Biswas | The Legacy",
    page_icon="♛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;1,500&family=Inter:wght@300;400;500;600;700&display=swap');

.stApp {
    background: #080808;
    color: #eee8dc;
}
header, footer {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    padding-bottom: 5rem;
    max-width: 1250px;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
}

p, li {
    font-family: 'Inter', sans-serif;
    line-height: 1.9;
    color: #c9c1b4;
}

.gold {
    color: #d8b56d;
}

.hero {
    text-align: center;
    padding: 100px 15px 90px;
    border-top: 1px solid #69552c;
    border-bottom: 1px solid #69552c;
    background: radial-gradient(ellipse at center, #292014 0%, #080808 70%);
}

.hero-small {
    color: #d8b56d;
    letter-spacing: 7px;
    font-size: 12px;
    font-weight: 600;
}

.hero h1 {
    font-size: clamp(42px, 8vw, 100px);
    color: #e5c47c;
    letter-spacing: 5px;
    margin: 25px 0;
    line-height: 1.2;
}

.hero-sub {
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    font-style: italic;
    color: #ded4c1;
}

.gold-line {
    width: 100px;
    height: 2px;
    background: #c6a45c;
    margin: 30px auto;
}

.section-title {
    color: #d8b56d;
    font-size: 30px;
    margin-top: 65px;
    margin-bottom: 20px;
}

.eyebrow {
    color: #bd9b5a;
    font-size: 11px;
    letter-spacing: 5px;
}

.panel {
    background: linear-gradient(145deg, #19150f, #0d0d0d);
    border: 1px solid #493b24;
    padding: 28px;
    border-radius: 5px;
    min-height: 190px;
    margin-bottom: 15px;
}

.panel h3 {
    color: #d9b86e;
    font-size: 19px;
}

.panel p {
    font-size: 14px;
}

.quote {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    font-style: italic;
    text-align: center;
    padding: 60px 20px;
    color: #e4c783;
    border-top: 1px solid #493b24;
    border-bottom: 1px solid #493b24;
    margin: 60px 0;
}

.number {
    color: #d8b56d;
    font-family: 'Cinzel', serif;
    font-size: 36px;
}

.timeline {
    border-left: 1px solid #ad8c4e;
    margin-left: 12px;
    padding-left: 25px;
}

.timeline-item {
    padding: 10px 0 30px;
}

.timeline-item h3 {
    color: #d8b56d;
    font-size: 18px;
}

.footer {
    text-align: center;
    padding: 55px 10px;
    border-top: 1px solid #493b24;
    color: #9b8760;
    letter-spacing: 3px;
    font-size: 11px;
}

div[data-testid="stMetric"] {
    background: #15120e;
    border: 1px solid #493b24;
    padding: 18px;
    border-radius: 5px;
}
div[data-testid="stMetricValue"] {
    color: #d8b56d;
}
.stButton button {
    background: #c5a45f;
    color: #100d08;
    border: none;
    border-radius: 2px;
    padding: 12px 25px;
    font-weight: 700;
}
.stButton button:hover {
    background: #f0d99c;
    color: black;
}
[data-testid="stSidebar"] {
    background: #100e0a;
    border-right: 1px solid #493b24;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.markdown("""
<h1 style='color:#d8b56d; font-size:25px;'>
♛ ANKITA BISWAS
</h1>
<p style='letter-spacing:3px;font-size:10px;'>
THE LEGACY ARCHIVE
</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "EXPLORE THE ARCHIVE",
    [
        "The Beginning",
        "Who Is Ankita?",
        "Intellectual Identity",
        "The Philosophy",
        "The Empire",
        "The Vision",
        "The Manifesto"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='color:#bda36c;font-size:11px;'>"
    "A LIFE BEYOND ORDINARY DEFINITIONS.</p>",
    unsafe_allow_html=True
)


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <div class="hero-small">AN INDIVIDUAL. AN IDEOLOGY. A LEGACY.</div>
    <h1>ANKITA<br>BISWAS</h1>
    <div class="gold-line"></div>
    <div class="hero-sub">
        "The world is not a boundary. It is a canvas."
    </div>
    <br>
    <p style="letter-spacing:4px;font-size:11px;color:#a99570;">
        INTELLECT • AMBITION • LEADERSHIP • LEGACY
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- PAGE 1 ----------------

if page == "The Beginning":

    st.markdown('<p class="eyebrow">01 / THE INTRODUCTION</p>',
                unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title">Some stories are not written to be ordinary.</h2>
    <p>
    There are people who seek a place in the world, and there are
    people who aspire to build something that changes their place
    in it.
    </p>
    <p>
    Ankita Biswas belongs to the latter category of dreamers.
    A young mind with an expansive imagination, an interest in
    technology, a fascination with business and an ambition that
    refuses to remain confined to a single professional identity.
    </p>
    <p>
    Her story is not defined by a title she already possesses.
    It is defined by the scale of what she intends to create.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"I was never interested in simply fitting into the world. I wanted to understand it, build within it, and leave something meaningful behind."</div>',
                unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="panel"><div class="number">01</div><h3>The Mind</h3><p>Curiosity, learning, technology and intellectual independence.</p></div>',
                    unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="panel"><div class="number">02</div><h3>The Vision</h3><p>Entrepreneurship, global exposure and the creation of lasting value.</p></div>',
                    unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="panel"><div class="number">03</div><h3>The Legacy</h3><p>Building something that outlives a moment of recognition.</p></div>',
                    unsafe_allow_html=True)


# ---------------- PAGE 2 ----------------

elif page == "Who Is Ankita?":

    st.markdown('<p class="eyebrow">02 / THE IDENTITY</p>',
                unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title">Who is Ankita Biswas?</h2>
    <p>
    She is a student of Computer Science and Engineering,
    specialising in Artificial Intelligence and Machine Learning.
    But her interests do not end with algorithms, programming
    languages or technological systems.
    </p>
    <p>
    She is deeply interested in the architecture of businesses,
    the psychology of leadership, the economics of opportunity,
    and the art of transforming ideas into institutions.
    </p>
    <p>
    She admires the intersection of intelligence and influence:
    the ability to understand a technology, recognise a market,
    lead people and make decisions with long-term consequences.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"A degree may introduce me to the world. What I build with my knowledge will define my contribution to it."</div>',
                unsafe_allow_html=True)

    st.markdown("### The dimensions of her identity")

    details = [
        ("The Technologist", "Exploring AI, machine learning, programming and emerging technologies."),
        ("The Strategist", "Interested in markets, competition, management and long-term planning."),
        ("The Entrepreneurial Mind", "Dreaming of creating and leading an independent business."),
        ("The Global Thinker", "Aspiring to learn, work and build relationships across borders."),
        ("The Individual", "Valuing independence, personal growth, discipline and intellectual curiosity.")
    ]

    for title, desc in details:
        st.markdown(f"""
        <div class="panel">
        <h3>{title}</h3>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------- PAGE 3 ----------------

elif page == "Intellectual Identity":

    st.markdown('<p class="eyebrow">03 / ACADEMIC AND PROFESSIONAL DEVELOPMENT</p>',
                unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">The architecture of knowledge.</h2>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline">
      <div class="timeline-item">
        <h3>THE FOUNDATION</h3>
        <p>Developing an academic foundation in science, mathematics,
        logical thinking and technology.</p>
      </div>
      <div class="timeline-item">
        <h3>THE TECHNOLOGY CHAPTER</h3>
        <p>B.Tech in Computer Science and Engineering,
        with a specialisation in Artificial Intelligence
        and Machine Learning.</p>
      </div>
      <div class="timeline-item">
        <h3>THE INDUSTRY CHAPTER</h3>
        <p>A future ambition to gain professional experience,
        understand organisations and participate in real-world
        technological development.</p>
      </div>
      <div class="timeline-item">
        <h3>THE BUSINESS CHAPTER</h3>
        <p>Aspirations for advanced business education,
        strategic management and entrepreneurial leadership.</p>
      </div>
      <div class="timeline-item">
        <h3>THE LEADERSHIP CHAPTER</h3>
        <p>The long-term vision of creating, directing and
        expanding an organisation with global ambitions.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Fields of intellectual interest")

    subjects = [
        "Artificial Intelligence",
        "Machine Learning",
        "Business Strategy",
        "Entrepreneurship",
        "Economics",
        "Organisational Leadership",
        "Innovation",
        "Management"
    ]

    cols = st.columns(2)

    for i, subject in enumerate(subjects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="panel">
            <h3>{subject}</h3>
            <p>A field for continuous exploration and development.</p>
            </div>
            """, unsafe_allow_html=True)


# ---------------- PAGE 4 ----------------

elif page == "The Philosophy":

    st.markdown('<p class="eyebrow">04 / PERSONAL PHILOSOPHY</p>',
                unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">The principles behind the ambition.</h2>',
                unsafe_allow_html=True)

    principles = [
        ("01 — Knowledge", "Knowledge should never become a decoration. It should become the instrument through which better decisions are made."),
        ("02 — Independence", "Financial, intellectual and personal independence are essential components of a meaningful life."),
        ("03 — Excellence", "Mediocrity should never become a permanent destination. Improvement must remain a lifelong process."),
        ("04 — Leadership", "Leadership is not merely the authority to command. It is the responsibility to create direction and opportunity."),
        ("05 — Courage", "A meaningful vision requires the willingness to begin before the outcome becomes certain."),
        ("06 — Integrity", "Success without character is an incomplete achievement.")
    ]

    for heading, description in principles:
        st.markdown(f"""
        <div class="panel">
        <h3>{heading}</h3>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"Let the scale of my dreams be matched by the discipline of my actions."</div>',
                unsafe_allow_html=True)


# ---------------- PAGE 5 ----------------

elif page == "The Empire":

    st.markdown('<p class="eyebrow">05 / THE ENTREPRENEURIAL VISION</p>',
                unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Beyond a career. Towards an institution.</h2>',
                unsafe_allow_html=True)

    st.markdown("""
    <p>
    The ultimate entrepreneurial ambition is not simply to occupy
    a position in an established organisation.
    It is to understand how organisations are created,
    how they grow, how they innovate and how they create value.
    </p>
    <p>
    The long-term dream is to build an independent business group
    with a culture of innovation, strategic thinking and
    international ambition.
    </p>
    """ , unsafe_allow_html=True)

    divisions = [
        ("TECHNOLOGY", "AI-driven products, software, intelligent systems and digital innovation."),
        ("INNOVATION", "Research, experimentation, emerging technologies and future-facing ideas."),
        ("BUSINESS", "Strategic management, operations, finance and organisational development."),
        ("GLOBAL EXPANSION", "International partnerships, new markets and sustainable growth.")
    ]

    cols = st.columns(2)

    for i, (heading, desc) in enumerate(divisions):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="panel">
            <h3>{heading}</h3>
            <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"The ambition is not merely to join the architecture of the business world. It is to create something within it."</div>',
                unsafe_allow_html=True)


# ---------------- PAGE 6 ----------------

elif page == "The Vision":

    st.markdown('<p class="eyebrow">06 / THE FUTURE</p>',
                unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">A horizon without borders.</h2>',
                unsafe_allow_html=True)

    st.markdown("""
    <p>
    The future imagined by Ankita extends beyond a conventional
    professional trajectory.
    </p>
    <p>
    It includes advanced education, international exposure,
    entrepreneurial independence, meaningful professional
    relationships, financial freedom and the opportunity
    to build a life of intellectual and personal richness.
    </p>
    """ , unsafe_allow_html=True)

    ambitions = [
        "Become deeply competent in technology and AI.",
        "Gain meaningful professional industry experience.",
        "Explore world-class business education.",
        "Develop expertise in strategic leadership.",
        "Create an independent business venture.",
        "Build an organisation with international reach.",
        "Create opportunities for other people.",
        "Achieve a balance between professional ambition and personal freedom."
    ]

    for item in ambitions:
        st.markdown(f"""
        <div class="panel" style="min-height:75px;">
        <p><span style="color:#d8b56d;">✦</span> {item}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"Think globally. Learn relentlessly. Build fearlessly."</div>',
                unsafe_allow_html=True)


# ---------------- PAGE 7 ----------------

elif page == "The Manifesto":

    st.markdown('<p class="eyebrow">07 / THE PERSONAL MANIFESTO</p>',
                unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title">This is not a declaration of arrival.</h2>
    <h2 style="color:#d8b56d;font-size:35px;">
    IT IS A DECLARATION OF INTENT.
    </h2>
    <br>
    <p>
    I do not need to pretend that I have already conquered the world.
    I have something more important: the opportunity to prepare,
    to learn, to fail, to improve and to create.
    </p>
    <p>
    I will not measure my potential by the limitations of my
    current circumstances. I will measure my progress by
    the quality of my decisions and the consistency of my work.
    </p>
    <p>
    I will study technology not merely to earn a qualification,
    but to understand the systems shaping the future.
    </p>
    <p>
    I will study business not merely to obtain a title,
    but to understand how ideas become enterprises,
    how people become teams and how vision becomes reality.
    </p>
    <p>
    I will pursue ambition without abandoning character.
    I will pursue influence without losing humility.
    I will pursue success without forgetting the people
    and principles that matter.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="quote">"Remember the name. Respect the journey. Watch the work."</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align:center;color:#d8b56d;">
    ANKITA BISWAS
    </h2>
    <p style="text-align:center;letter-spacing:4px;">
    THE STORY IS STILL BEING WRITTEN.
    </p>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    ANKITA BISWAS<br><br>
    A VISION IN PROGRESS · A LEGACY IN THE MAKING<br><br>
    © 2026 | PERSONAL PORTFOLIO
</div>
""", unsafe_allow_html=True)

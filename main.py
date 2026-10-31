import streamlit as st

st.set_page_config(
    page_title="Ankita Biswas | Mortison Group",
    page_icon="👑",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #0b1019;
    color: #f5f1e8;
}
h1, h2, h3 {
    color: #e8c887 !important;
}
p, li, label {
    color: #e4e4e7;
}
.hero {
    padding: 55px 30px;
    background: linear-gradient(120deg, #172333, #28202a, #10141d);
    border: 1px solid #947749;
    border-radius: 20px;
    text-align: center;
}
.hero h1 {
    font-size: 46px;
    letter-spacing: 3px;
}
.hero p {
    font-size: 18px;
}
.panel {
    background: #151c28;
    border: 1px solid #594a35;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 15px;
}
.gold {
    color: #e8c887;
    font-weight: bold;
}
div.stButton > button {
    background: #c8a76a;
    color: #10141d;
    border-radius: 8px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<p>THE MORTISON GROUP • LEADERSHIP PROFILE</p>
<h1>ANKITA BISWAS</h1>
<h3>Chief Marketing Officer | Entrepreneur | Strategist</h3>
<p>Vision beyond boundaries. Leadership beyond titles.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Navigation
page = st.radio(
    "Explore the empire",
    [
        "Executive Overview",
        "Education",
        "Career Journey",
        "My Business",
        "Leadership Vision"
    ],
    horizontal=True
)

st.markdown("---")

if page == "Executive Overview":
    st.title("The Woman Behind the Vision")

    st.markdown("""
    <div class="panel">
    Ankita Biswas is presented as a visionary business leader
    serving as Chief Marketing Officer of Mortison Group.
    With a foundation in artificial intelligence, computer
    science, corporate experience and advanced business
    education, she brings technology and strategy together.
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    a.metric("Education", "BTech + MBA")
    b.metric("Work Experience", "3 Years")
    c.metric("Leadership", "CMO")

    st.subheader("Her Philosophy")
    st.write(
        '"Think like a strategist. Build like an entrepreneur. '
        'Lead with courage."'
    )

    st.info(
        "This is an aspirational profile. Add verified "
        "achievements as your real career progresses."
    )

elif page == "Education":
    st.title("Education & Excellence")

    st.markdown("""
    <div class="panel">
    <h3>01 • BTech in Computer Science Engineering</h3>
    <p>Specialization: Artificial Intelligence & Machine Learning</p>
    <p>Duration: 4 Years</p>
    <p>Focus: Programming, intelligent systems, data, "
    "technology and analytical thinking.</p>
    </div>
    """.replace('"', ''), unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
    <h3>02 • Professional Experience</h3>
    <p>Duration: 3 Years</p>
    <p>Developed practical knowledge of business operations,
    teamwork, professional communication and strategy.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
    <h3>03 • Harvard Business School</h3>
    <p>Goal: MBA in Business Administration</p>
    <p>Aspirational achievement: Top student in the class.</p>
    <p>Areas of interest: Leadership, finance, marketing,
    entrepreneurship and global business.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Career Journey":
    st.title("The Journey to the Boardroom")

    st.markdown("""
    <div class="panel">
    <h3>Chapter I — The Technologist</h3>
    Built a foundation in AI, machine learning and
    computer science.
    </div>
    <div class="panel">
    <h3>Chapter II — The Professional</h3>
    Spent three years learning how companies operate,
    solve problems and create value.
    </div>
    <div class="panel">
    <h3>Chapter III — The Harvard Dream</h3>
    Pursued advanced business education, developing
    the mindset to lead teams and make strategic decisions.
    </div>
    <div class="panel">
    <h3>Chapter IV — The Executive</h3>
    Aspires to lead marketing, brand strategy, growth
    and innovation at Mortison Group.
    </div>
    """, unsafe_allow_html=True)

elif page == "My Business":
    st.title("Founder. Creator. Entrepreneur.")

    business_name = st.text_input(
        "Give your own company a name",
        "Ankita Global Ventures"
    )

    industry = st.selectbox(
        "Choose your business sector",
        [
            "AI & Technology",
            "Luxury & Lifestyle",
            "Beauty & Fashion",
            "Global Consulting",
            "Finance & Investments",
            "A business empire across industries"
        ]
    )

    vision = st.text_area(
        "Describe your business vision",
        "Building an innovative global company that "
        "creates value, empowers people and transforms industries."
    )

    if st.button("Create my founder profile"):
        st.success("Your entrepreneurial vision is ready!")

        st.markdown(f"""
        <div class="panel">
        <h2>{business_name}</h2>
        <p><b>Founder:</b> Ankita Biswas</p>
        <p><b>Industry:</b> {industry}</p>
        <p><b>Vision:</b> {vision}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Leadership Vision":
    st.title("A Vision for the Future")

    st.markdown("""
    <div class="panel">
    <h3>01 • Global Leadership</h3>
    Build the skills to lead international teams
    and understand global markets.
    </div>
    <div class="panel">
    <h3>02 • Technology Meets Business</h3>
    Use AI and data to make smarter business decisions
    and discover new opportunities.
    </div>
    <div class="panel">
    <h3>03 • Build Something of My Own</h3>
    Create a sustainable business with a distinctive
    identity, strong values and long-term ambition.
    </div>
    <div class="panel">
    <h3>04 • A Legacy That Matters</h3>
    Become a leader whose success creates opportunities
    for others.
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:20px;">
<h3>ANKITA BISWAS</h3>
<p>Ambition is the beginning. Execution builds the empire.</p>
<p>© Personal aspirational portfolio</p>
</div>
""", unsafe_allow_html=True)

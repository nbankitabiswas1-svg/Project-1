import streamlit as st
import pandas as pd
import random
from datetime import date

st.set_page_config(
    page_title="Modison Group | CEO Office",
    page_icon="👑",
    layout="wide"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: #0b1120;
    color: #e5e7eb;
}
[data-testid="stSidebar"] {
    background: #111a2b;
    border-right: 1px solid #29364b;
}
h1, h2, h3 {
    color: #e8c779 !important;
}
p, label, li {
    color: #d1d8e5;
}
div[data-testid="stMetric"] {
    background: #151f32;
    border: 1px solid #2b3a52;
    padding: 17px;
    border-radius: 12px;
}
div[data-testid="stMetricValue"] {
    color: #f0d18a;
}
div.stButton > button {
    background: #c7a55e;
    color: #111827;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}
div.stButton > button:hover {
    background: #efd69d;
    color: #111827;
}
hr {
    border-color: #29364b;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION DATA ----------
if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "Project": "Project Orion",
            "Department": "Technology",
            "Budget (₹ Cr)": 18.0,
            "Progress (%)": 68,
            "Status": "In Progress"
        },
        {
            "Project": "Global Expansion 2030",
            "Department": "Strategy",
            "Budget (₹ Cr)": 35.0,
            "Progress (%)": 32,
            "Status": "In Progress"
        },
        {
            "Project": "Brand Renaissance",
            "Department": "Marketing",
            "Budget (₹ Cr)": 8.5,
            "Progress (%)": 82,
            "Status": "In Progress"
        },
        {
            "Project": "Green Future",
            "Department": "Sustainability",
            "Budget (₹ Cr)": 12.0,
            "Progress (%)": 45,
            "Status": "Under Review"
        },
        {
            "Project": "Customer First AI",
            "Department": "Technology",
            "Budget (₹ Cr)": 6.0,
            "Progress (%)": 55,
            "Status": "In Progress"
        }
    ]

if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"Task": "Review quarterly growth strategy",
         "Priority": "High", "Done": False},
        {"Task": "Approve global marketing proposal",
         "Priority": "High", "Done": False},
        {"Task": "Meet the technology leadership team",
         "Priority": "Medium", "Done": False},
        {"Task": "Review sustainability roadmap",
         "Priority": "Medium", "Done": True}
    ]

if "notes" not in st.session_state:
    st.session_state.notes = []

if "decisions" not in st.session_state:
    st.session_state.decisions = []

if "meetings" not in st.session_state:
    st.session_state.meetings = []

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## ◈ MODISON GROUP")
    st.caption("EXECUTIVE COMMAND CENTER")
    st.markdown("---")

    st.markdown("### 👑 Ankita Biswas")
    st.caption("Chief Executive Officer")

    page = st.radio(
        "OFFICE NAVIGATION",
        [
            "CEO Dashboard",
            "Corporate Strategy",
            "Project Portfolio",
            "Finance & Analytics",
            "Marketing & Growth",
            "Boardroom",
            "CEO Tasks",
            "Executive Journal"
        ]
    )

    st.markdown("---")
    st.caption("EXECUTIVE ACCESS")
    st.caption("Private workspace · Demo environment")

# ---------- HEADER ----------
st.markdown(
    f"### MODISON GROUP  /  {page.upper()}"
)
st.markdown(
    f"# Good day, Ankita. 👑"
)
st.caption(
    f"CEO OFFICE  •  {date.today().strftime('%d %B %Y')}  "
    "•  Fictional business simulation"
)
st.markdown("---")

# ---------- CEO DASHBOARD ----------
if page == "CEO Dashboard":

    st.subheader("Executive Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Illustrative Revenue", "₹248 Cr", "+12.4%")
    c2.metric("Operating Margin", "18.6%", "+2.1 pp")
    c3.metric("Active Projects",
              str(len(st.session_state.projects)))
    c4.metric("Markets Targeted", "12", "+3")

    st.caption(
        "All financial figures and company statistics are "
        "fictional demonstration data, not actual company results."
    )

    left, right = st.columns([1.5, 1])

    with left:
        st.subheader("Revenue Growth")
        revenue = pd.DataFrame({
            "Quarter": ["Q1", "Q2", "Q3", "Q4"],
            "Revenue (₹ Cr)": [165, 184, 213, 248]
        }).set_index("Quarter")

        st.line_chart(revenue)

        st.subheader("Strategic Priorities")

        priorities = [
            ("01", "Expand international presence",
             "Target markets and partnerships"),
            ("02", "Accelerate AI adoption",
             "Automation and intelligent products"),
            ("03", "Strengthen brand positioning",
             "Customer trust and brand visibility"),
            ("04", "Improve operational efficiency",
             "Cost management and execution")
        ]

        for number, title, description in priorities:
            with st.container(border=True):
                st.markdown(f"**{number}  |  {title}**")
                st.caption(description)

    with right:
        st.subheader("CEO's Daily Briefing")

        st.info(
            "STRATEGY\n\nReview the proposed international "
            "expansion roadmap."
        )
        st.warning(
            "DECISION REQUIRED\n\nEvaluate budget allocation "
            "for the AI innovation programme."
        )
        st.success(
            "MILESTONE\n\nBrand Renaissance has reached "
            "82% completion in the sample portfolio."
        )

        st.subheader("Portfolio Status")
        projects_df = pd.DataFrame(st.session_state.projects)

        if not projects_df.empty:
            st.bar_chart(
                projects_df.set_index("Project")[["Progress (%)"]]
            )

# ---------- CORPORATE STRATEGY ----------
elif page == "Corporate Strategy":

    st.title("Corporate Strategy & Intelligence")
    st.write(
        "Explore the proposed strategic initiatives for "
        "the Modison Group simulation."
    )

    strategy_data = [
        {
            "name": "Strategy 01 — Global Expansion",
            "goal": "Enter selected international markets.",
            "actions": [
                "Research customer demand and competitors.",
                "Evaluate local partners and regulations.",
                "Build a market-entry business case.",
                "Pilot before committing major capital."
            ],
            "measure": "Market traction, margin and customer growth"
        },
        {
            "name": "Strategy 02 — AI Transformation",
            "goal": "Use AI to improve productivity and services.",
            "actions": [
                "Identify repetitive business processes.",
                "Run small, measurable automation pilots.",
                "Establish data privacy and security controls.",
                "Measure adoption and return on investment."
            ],
            "measure": "Time saved, adoption and cost per process"
        },
        {
            "name": "Strategy 03 — Brand Leadership",
            "goal": "Build a distinctive and trusted brand.",
            "actions": [
                "Research customer needs and brand perception.",
                "Define a clear brand positioning.",
                "Launch targeted marketing campaigns.",
                "Measure customer retention and acquisition."
            ],
            "measure": "Brand awareness, retention and acquisition cost"
        },
        {
            "name": "Strategy 04 — Sustainable Operations",
            "goal": "Improve resource efficiency responsibly.",
            "actions": [
                "Audit current energy and material use.",
                "Identify achievable efficiency improvements.",
                "Evaluate suppliers and operational risks.",
                "Track measurable sustainability indicators."
            ],
            "measure": "Waste reduction, efficiency and compliance"
        },
        {
            "name": "Strategy 05 — Customer Experience",
            "goal": "Make customer interactions more effective.",
            "actions": [
                "Map the customer journey.",
                "Identify common complaints and delays.",
                "Test improvements with a small customer group.",
                "Track satisfaction and repeat business."
            ],
            "measure": "Satisfaction, response time and retention"
        }
    ]

    for strategy in strategy_data:
        with st.expander(strategy["name"], expanded=False):
            st.write("**Strategic objective:**", strategy["goal"])
            st.write("**Execution roadmap:**")
            for action in strategy["actions"]:
                st.write("- ", action)
            st.write("**Key performance indicators:**",
                     strategy["measure"])

    st.subheader("Build a New Strategy")

    with st.form("strategy_form"):
        strategy_name = st.text_input("Strategy name")
        objective = st.text_area("Business objective")
        owner = st.text_input("Responsible department or leader")
        success_metric = st.text_input("Success metric")

        submitted = st.form_submit_button("Save Strategy")

        if submitted:
            if strategy_name.strip() and objective.strip():
                st.session_state.notes.append({
                    "Type": "Strategy",
                    "Title": strategy_name,
                    "Details": (
                        f"Objective: {objective} | "
                        f"Owner: {owner} | KPI: {success_metric}"
                    )
                })
                st.success("Strategy saved to your executive journal.")
            else:
                st.error("Enter a strategy name and objective.")

# ---------- PROJECT PORTFOLIO ----------
elif page == "Project Portfolio":

    st.title("Enterprise Project Portfolio")

    projects_df = pd.DataFrame(st.session_state.projects)

    if not projects_df.empty:
        st.dataframe(projects_df, use_container_width=True)
        st.metric(
            "Total Proposed Portfolio Budget",
            f"₹{projects_df['Budget (₹ Cr)'].sum():.1f} Cr"
        )

    st.subheader("Create a New Project")

    with st.form("project_form"):
        project_name = st.text_input("Project name")
        department = st.selectbox(
            "Department",
            [
                "Technology", "Finance", "Marketing",
                "Strategy", "Operations", "Human Resources",
                "Sustainability", "Research & Development"
            ]
        )
        budget = st.number_input(
            "Proposed budget (₹ Cr)",
            min_value=0.0,
            max_value=10000.0,
            value=1.0,
            step=0.5
        )
        progress = st.slider("Completion (%)", 0, 100, 0)
        status = st.selectbox(
            "Project status",
            ["Planned", "In Progress", "Under Review", "Completed"]
        )

        save_project = st.form_submit_button("Add to Portfolio")

        if save_project:
            if project_name.strip():
                st.session_state.projects.append({
                    "Project": project_name,
                    "Department": department,
                    "Budget (₹ Cr)": budget,
                    "Progress (%)": progress,
                    "Status": status
                })
                st.success("Project added to the portfolio.")
                st.rerun()
            else:
                st.error("Please enter a project name.")

    st.subheader("Project Health Check")

    if not projects_df.empty:
        selected = st.selectbox(
            "Select a project",
            projects_df["Project"].tolist()
        )

        selected_project = next(
            p for p in st.session_state.projects
            if p["Project"] == selected
        )

        st.write("**Department:**", selected_project["Department"])
        st.write("**Status:**", selected_project["Status"])
        st.progress(selected_project["Progress (%)"] / 100)
        st.caption(
            f"Reported completion: "
            f"{selected_project['Progress (%)']}%"
        )

        new_status = st.selectbox(
            "Update project status",
            ["Planned", "In Progress", "Under Review", "Completed"],
            index=[
                "Planned", "In Progress",
                "Under Review", "Completed"
            ].index(selected_project["Status"])
        )

        if st.button("Update Selected Project"):
            selected_project["Status"] = new_status
            st.success("Project status updated.")
            st.rerun()

    st.download_button(
        "Download Project Portfolio (CSV)",
        pd.DataFrame(st.session_state.projects).to_csv(index=False),
        file_name="modison_project_portfolio.csv",
        mime="text/csv"
    )

# ---------- FINANCE ----------
elif page == "Finance & Analytics":

    st.title("Financial Intelligence")

    st.caption(
        "Illustrative figures for learning and simulation only."
    )

    a, b, c = st.columns(3)
    a.metric("Revenue", "₹248 Cr")
    b.metric("Operating Costs", "₹202 Cr")
    c.metric("Operating Profit", "₹46 Cr")

    st.subheader("Financial Performance")

    financials = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Revenue": [165, 184, 213, 248],
        "Operating Costs": [145, 155, 176, 202],
        "Operating Profit": [20, 29, 37, 46]
    }).set_index("Quarter")

    st.line_chart(financials)

    st.subheader("Budget Planning Tool")

    revenue_target = st.number_input(
        "Planned annual revenue (₹ Cr)",
        min_value=0.0,
        value=300.0,
        step=10.0
    )

    margin_target = st.slider(
        "Target operating margin (%)",
        1, 50, 20
    )

    expected_profit = revenue_target * margin_target / 100

    x, y = st.columns(2)
    x.metric("Revenue Target", f"₹{revenue_target:.1f} Cr")
    y.metric("Illustrative Operating Profit",
             f"₹{expected_profit:.1f} Cr")

    st.caption(
        "This is a simple planning estimate, not a forecast "
        "or audited financial statement."
    )

# ---------- MARKETING ----------
elif page == "Marketing & Growth":

    st.title("Marketing & Growth Command Center")

    st.subheader("Sample Campaign Portfolio")

    campaigns = pd.DataFrame([
        {
            "Campaign": "Future Forward",
            "Channel": "Digital",
            "Budget (₹ Lakh)": 35,
            "Objective": "Brand awareness"
        },
        {
            "Campaign": "Beyond Borders",
            "Channel": "International",
            "Budget (₹ Lakh)": 60,
            "Objective": "Market entry"
        },
        {
            "Campaign": "Customer First",
            "Channel": "Customer Relations",
            "Budget (₹ Lakh)": 20,
            "Objective": "Retention"
        },
        {
            "Campaign": "Innovation Week",
            "Channel": "Events",
            "Budget (₹ Lakh)": 15,
            "Objective": "Product engagement"
        }
    ])

    st.dataframe(campaigns, use_container_width=True)

    st.subheader("Create a Campaign Brief")

    with st.form("campaign_form"):
        campaign = st.text_input("Campaign name")
        audience = st.text_input("Target audience")
        channel = st.selectbox(
            "Primary channel",
            [
                "Social Media", "Search", "Email",
                "Events", "Public Relations", "Partnerships"
            ]
        )
        objective = st.text_area("Campaign objective")
        kpi = st.text_input("Primary KPI")

        save_campaign = st.form_submit_button("Save Campaign Brief")

        if save_campaign:
            if campaign.strip() and objective.strip():
                st.session_state.notes.append({
                    "Type": "Campaign",
                    "Title": campaign,
                    "Details": (
                        f"Audience: {audience} | Channel: {channel} | "
                        f"Objective: {objective} | KPI: {kpi}"
                    )
                })
                st.success("Campaign brief saved.")
            else:
                st.error("Enter the campaign name and objective.")

    st.subheader("Marketing Strategy Checklist")

    for item in [
        "Define positioning and brand message",
        "Research customer segments",
        "Review campaign budgets",
        "Set conversion and retention targets",
        "Schedule performance reviews"
    ]:
        st.checkbox(item, key="marketing_" + item)

# ---------- BOARDROOM ----------
elif page == "Boardroom":

    st.title("The Executive Boardroom")

    st.subheader("Meeting Agenda")

    agenda = [
        "Quarterly business performance",
        "Global expansion proposal",
        "AI transformation investment",
        "Brand strategy and customer growth",
        "Risk management and compliance",
        "Next-quarter priorities"
    ]

    for i, item in enumerate(agenda, 1):
        st.write(f"**{i:02d}.** {item}")

    st.markdown("---")
    st.subheader("Record a Board Decision")

    with st.form("decision_form"):
        topic = st.text_input("Decision topic")
        decision = st.text_area("Decision or proposed action")
        owner = st.text_input("Responsible person or department")
        due_date = st.date_input("Target review date", value=date.today())
        status = st.selectbox(
            "Decision status",
            ["Proposed", "Approved", "Deferred", "Rejected"]
        )

        save_decision = st.form_submit_button("Record Decision")

        if save_decision:
            if topic.strip() and decision.strip():
                st.session_state.decisions.append({
                    "Topic": topic,
                    "Decision": decision,
                    "Owner": owner,
                    "Review Date": str(due_date),
                    "Status": status
                })
                st.success("Decision recorded in this session.")
            else:
                st.error("Add a topic and decision.")

    st.subheader("Decision Register")

    if st.session_state.decisions:
        st.dataframe(
            pd.DataFrame(st.session_state.decisions),
            use_container_width=True
        )
    else:
        st.info("No decisions recorded yet.")

    st.subheader("Schedule a Meeting")

    with st.form("meeting_form"):
        meeting_title = st.text_input("Meeting title")
        attendees = st.text_input("Participants")
        meeting_date = st.date_input(
            "Meeting date",
            value=date.today(),
            key="meeting_date"
        )
        meeting_time = st.time_input(
            "Meeting time",
            key="meeting_time"
        )
        meeting_notes = st.text_area("Agenda and preparation")

        save_meeting = st.form_submit_button("Add Meeting")

        if save_meeting:
            if meeting_title.strip():
                st.session_state.meetings.append({
                    "Meeting": meeting_title,
                    "Participants": attendees,
                    "Date": str(meeting_date),
                    "Time": str(meeting_time),
                    "Notes": meeting_notes
                })
                st.success("Meeting added.")
            else:
                st.error("Enter a meeting title.")

    if st.session_state.meetings:
        st.dataframe(
            pd.DataFrame(st.session_state.meetings),
            use_container_width=True
        )

# ---------- TASKS ----------
elif page == "CEO Tasks":

    st.title("CEO's Personal Task Manager")

    with st.form("task_form"):
        task_name = st.text_input("New task")
        priority =

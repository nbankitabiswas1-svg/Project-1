import streamlit as st
import json
import os
from datetime import date

st.set_page_config(
    page_title="Modison Group | CEO Office",
    page_icon="👑",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: #0b1120;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background: #111a2b;
}
h1, h2, h3 {
    color: #e8c779 !important;
}
p, label {
    color: #dbe3ef;
}
div[data-testid="stMetric"] {
    background: #151f32;
    border: 1px solid #35425a;
    border-radius: 12px;
    padding: 15px;
}
div.stButton > button {
    background: #c7a55e;
    color: #111827;
    border-radius: 8px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
DATA_FILE = "modison_data.json"

def load_data():
    default = {
        "projects": [
            {
                "name": "Project Orion AI",
                "department": "Technology",
                "budget": 18.0,
                "progress": 68,
                "status": "In Progress"
            },
            {
                "name": "Global Expansion",
                "department": "Strategy",
                "budget": 35.0,
                "progress": 32,
                "status": "In Progress"
            },
            {
                "name": "Brand Renaissance",
                "department": "Marketing",
                "budget": 8.5,
                "progress": 82,
                "status": "In Progress"
            }
        ],
        "tasks": [
            {
                "name": "Review growth strategy",
                "priority": "High",
                "done": False
            },
            {
                "name": "Approve marketing proposal",
                "priority": "High",
                "done": False
            },
            {
                "name": "Review AI investment plan",
                "priority": "Medium",
                "done": False
            }
        ],
        "decisions": [],
        "notes": []
    }

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                saved = json.load(file)
            for key in default:
                if key not in saved:
                    saved[key] = default[key]
            return saved
        except (OSError, ValueError):
            pass

    return default

if "data" not in st.session_state:
    st.session_state.data = load_data()

def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                st.session_state.data,
                file,
                indent=4,
                ensure_ascii=False
            )
        return True
    except OSError:
        return False

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("# ◈ MODISON")
    st.caption("GROUP • CEO COMMAND CENTER")
    st.markdown("---")
    st.markdown("### 👑 Ankita Biswas")
    st.caption("Chief Executive Officer")

    page = st.radio(
        "NAVIGATION",
        [
            "CEO Dashboard",
            "Corporate Strategy",
            "Project Portfolio",
            "Finance & Planning",
            "Marketing & Growth",
            "Boardroom",
            "CEO Task Manager",
            "Executive Journal"
        ]
    )

    st.markdown("---")
    st.caption("Executive workspace")

data = st.session_state.data

# ---------- HEADER ----------
st.caption(
    "MODISON GROUP  /  EXECUTIVE OFFICE  /  "
    + date.today().strftime("%d %B %Y")
)
st.title("Good day, Ankita. 👑")
st.markdown("---")

# ---------- DASHBOARD ----------
if page == "CEO Dashboard":
    st.subheader("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Illustrative Revenue", "₹248 Cr", "+12.4%")
    col2.metric("Operating Margin", "18.6%", "+2.1 pp")
    col3.metric("Active Projects", str(len(data["projects"])))
    col4.metric(
        "Pending Tasks",
        str(sum(1 for t in data["tasks"] if not t["done"]))
    )

    st.caption(
        "Demonstration figures only. These are not actual "
        "Modison Group financial results."
    )

    left, right = st.columns([1.4, 1])

    with left:
        st.subheader("Revenue Performance")

        st.line_chart({
            "Revenue (₹ Cr)": [165, 184, 213, 248]
        })

        st.subheader("Strategic Priorities")

        for title, detail in [
            ("Global Expansion",
             "Research markets, partners and entry costs."),
            ("AI Transformation",
             "Identify automation opportunities and measure ROI."),
            ("Brand Leadership",
             "Improve customer trust and market positioning."),
            ("Operational Excellence",
             "Improve productivity and control costs.")
        ]:
            with st.container(border=True):
                st.markdown("**" + title + "**")
                st.write(detail)

    with right:
        st.subheader("CEO Briefing")

        st.info(
            "DECISION: Review the proposed AI investment plan."
        )
        st.warning(
            "PRIORITY: Assess risks before entering a new market."
        )
        st.success(
            "MILESTONE: Brand Renaissance is 82% complete."
        )

        st.subheader("Project Progress")

        for project in data["projects"]:
            st.write(project["name"])
            st.progress(
                max(0, min(100, project["progress"])) / 100
            )
            st.caption(str(project["progress"]) + "% complete")

# ---------- STRATEGY ----------
elif page == "Corporate Strategy":
    st.header("Corporate Strategy & Intelligence")

    strategies = [
        (
            "01. Global Expansion",
            [
                "Research market size and customer demand.",
                "Compare competitors and pricing.",
                "Evaluate local partners and regulations.",
                "Prepare a pilot launch and risk assessment."
            ]
        ),
        (
            "02. AI Transformation",
            [
                "Identify repetitive processes.",
                "Evaluate potential AI solutions.",
                "Protect confidential company data.",
                "Measure time saved and return on investment."
            ]
        ),
        (
            "03. Brand Leadership",
            [
                "Define brand positioning.",
                "Study customer preferences.",
                "Plan digital marketing campaigns.",
                "Measure customer acquisition and retention."
            ]
        ),
        (
            "04. Sustainable Operations",
            [
                "Audit energy and material usage.",
                "Identify efficiency improvements.",
                "Review supplier standards.",
                "Track environmental performance."
            ]
        ),
        (
            "05. Customer Experience",
            [
                "Map the customer journey.",
                "Identify common complaints.",
                "Improve support and response times.",
                "Measure customer satisfaction."
            ]
        )
    ]

    for title, actions in strategies:
        with st.expander(title):
            for action in actions:
                st.write("• " + action)

    st.subheader("Create a Strategy")

    with st.form("strategy_form"):
        name = st.text_input("Strategy name")
        objective = st.text_area("Business objective")
        owner = st.text_input("Responsible department")
        kpi = st.text_input("How will success be measured?")
        submitted = st.form_submit_button("Save Strategy")

    if submitted:
        if name.strip() and objective.strip():
            data["notes"].append({
                "type": "Strategy",
                "title": name,
                "details": objective,
                "owner": owner,
                "kpi": kpi
            })
            if save_data():
                st.success("Strategy saved successfully.")
            else:
                st.error("Could not save the file.")
        else:
            st.error("Enter a strategy name and objective.")

# ---------- PROJECTS ----------
elif page == "Project Portfolio":
    st.header("Enterprise Project Portfolio")

    st.write("Your current projects:")

    for i, project in enumerate(data["projects"]):
        with st.expander(project["name"]):
            st.write("Department:", project["department"])
            st.write("Budget: ₹", project["budget"], "Cr")
            st.write("Status:", project["status"])
            st.progress(
                max(0, min(100, project["progress"])) / 100
            )
            st.write(str(project["progress"]) + "% complete")

            new_progress = st.slider(
                "Update completion",
                0, 100, int(project["progress"]),
                key="progress_" + str(i)
            )

            new_status = st.selectbox(
                "Update status",
                ["Planned", "In Progress", "Under Review", "Completed"],
                index=[
                    "Planned", "In Progress",
                    "Under Review", "Completed"
                ].index(
                    project["status"]
                    if project["status"] in [
                        "Planned", "In Progress",
                        "Under Review", "Completed"
                    ]
                    else "Planned"
                ),
                key="status_" + str(i)
            )

            if st.button("Save Project Update", key="save_" + str(i)):
                project["progress"] = new_progress
                project["status"] = new_status
                if save_data():
                    st.success("Project updated.")
                    st.rerun()
                else:
                    st.error("Could not save the project.")

    st.subheader("Add New Project")

    with st.form("project_form"):
        name = st.text_input("Project name")
        department = st.selectbox(
            "Department",
            [
                "Technology", "Finance", "Marketing",
                "Strategy", "Operations", "Research & Development"
            ]
        )
        budget = st.number_input(
            "Budget (₹ Cr)",
            min_value=0.0,
            value=1.0,
            step=0.5
        )
        progress = st.slider("Initial progress (%)", 0, 100, 0)
        status = st.selectbox(
            "Initial status",
            ["Planned", "In Progress", "Under Review", "Completed"]
        )
        submitted = st.form_submit_button("Add Project")

    if submitted:
        if name.strip():
            data["projects"].append({
                "name": name,
                "department": department,
                "budget": budget,
                "progress": progress,
                "status": status
            })
            if save_data():
                st.success("Project added.")
                st.rerun()
            else:
                st.error("Could not save project data.")
        else:
            st.error("Please enter a project name.")

    st.download_button(
        "Download Project Data",
        json.dumps(data["projects"], indent=2),
        file_name="modison_projects.json",
        mime="application/json"
    )

# ---------- FINANCE ----------
elif page == "Finance & Planning":
    st.header("Finance & Planning")

    st.caption("All values are fictional planning examples.")

    a, b, c = st.columns(3)
    a.metric("Illustrative Revenue", "₹248 Cr")
    b.metric("Operating Costs", "₹202 Cr")
    c.metric("Operating Profit", "₹46 Cr")

    st.subheader("Plan Your Business Targets")

    revenue = st.number_input(
        "Annual revenue target (₹ Cr)",
        min_value=0.0,
        value=300.0,
        step=10.0
    )

    margin = st.slider("Target operating margin (%)", 1, 50, 20)
    profit = revenue * margin / 100

    x, y = st.columns(2)
    x.metric("Revenue Target", f"₹{revenue:.1f} Cr")
    y.metric("Target Operating Profit", f"₹{profit:.1f} Cr")

    st.subheader("Illustrative Quarterly Revenue")
    st.bar_chart({"Revenue (₹ Cr)": [165, 184, 213, 248]})

# ---------- MARKETING ----------
elif page == "Marketing & Growth":
    st.header("Marketing & Growth")

    campaigns = [
        ("Future Forward", "Brand awareness", 35),
        ("Beyond Borders", "International expansion", 60),
        ("Customer First", "Customer retention", 20),
        ("Innovation Week", "Product engagement", 15)
    ]

    for name, objective, budget in campaigns:
        with st.container(border=True):
            st.markdown("**" + name + "**")
            st.write("Objective:", objective)
            st.write("Illustrative budget: ₹", budget, "lakh")

    st.subheader("Create Marketing Campaign")

    with st.form("campaign_form"):
        name = st.text_input("Campaign name")
        audience = st.text_input("Target audience")
        channel = st.selectbox(
            "Channel",
            ["Social Media", "Search", "Email", "Events", "Public Relations"]
        )
        objective = st.text_area("Campaign objective")
        kpi = st.text_input("Success metric")
        submitted = st.form_submit_button("Save Campaign")

    if submitted:
        if name.strip() and objective.strip():
            data["notes"].append({
                "type": "Campaign",
                "title": name,
                "details": objective,
                "audience": audience,
                "channel": channel,
                "kpi": kpi
            })
            if save_data():
                st.success("Campaign saved.")
            else:
                st.error("Could not save campaign.")
        else:
            st.error("Enter a campaign name and objective.")

# ---------- BOARDROOM ----------
elif page == "Boardroom":
    st.header("Executive Boardroom")

    st.subheader("Board Meeting Agenda")

    for i, item in enumerate([
        "Quarterly performance review",
        "Global expansion proposal",
        "AI investment decision",
        "Marketing strategy",
        "Risk and compliance",
        "Next-quarter priorities"
    ], 1):
        st.write(str(i) + ". " + item)

    st.subheader("Record a Decision")

    with st.form("decision_form"):
        topic = st.text_input("Decision topic")
        decision = st.text_area("Decision details")
        owner = st.text_input("Responsible department")
        review_date = st.date_input("Review date")
        status = st.selectbox(
            "Decision status",
            ["Proposed", "Approved", "Deferred", "Rejected"]
        )
        submitted = st.form_submit_button("Save Decision")

    if submitted:
        if topic.strip() and decision.strip():
            data["decisions"].append({
                "topic": topic,
                "decision": decision,
                "owner": owner,
                "review_date": str(review_date),
                "status": status
            })
            if save_data():
                st.success("Decision recorded.")
            else:
                st.error("Could not save decision.")
        else:
            st.error("Enter the topic and decision.")

    st.subheader("Decision Register")

    if data["decisions"]:
        for item in data["decisions"]:
            with st.container(border=True):
                st.markdown("**" + item["topic"] + "**")
                st.write(item["decision"])
                st.caption(
                    item["status"] + " | Owner: " + item["owner"]
                    + " | Review: " + item["review_date"]
                )
    else:
        st.info("Your decision register is empty.")

# ---------- TASK MANAGER ----------
elif page == "CEO Task Manager":
    st.header("CEO Task Manager")

    with st.form("task_form"):
        name = st.text_input("Task description")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        submitted = st.form_submit_button("Add Task")

    if submitted:
        if name.strip():
            data["tasks"].append({
                "name": name,
                "priority": priority,
                "done": False
            })
            if save_data():
                st.rerun()
            else:
                st.error("Could not save task.")
        else:
            st.error("Enter a task.")

    st.subheader("Your Workday")

    for i, task in enumerate(data["tasks"]):
        completed = st.checkbox(
            task["name"] + " (" + task["priority"] + ")",
            value=task["done"],
            key="task_" + str(i)
        )

        if completed != task["done"]:
            task["done"] = completed
            save_data()

    total = len(data["tasks"])
    done = sum(1 for task in data["tasks"] if task["done"])

    st.progress(done / total if total else 0)
    st.write(f"{done} of {total} tasks completed.")

    st.download_button(
        "Download Tasks",
        json.dumps(data["tasks"], indent=2),
        file_name="ceo_tasks.json",
        mime="application/json"
    )

# ---------- JOURNAL ----------
elif page == "Executive Journal":
    st.header("Executive Journal")

    with st.form("journal_form"):
        title = st.text_input("Entry title")
        category = st.selectbox(
            "Category",
            ["Leadership", "Business Idea", "Strategy", "Research", "Reflection"]
        )
        details = st.text_area("Write your thoughts", height=180)
        submitted = st.form_submit_button("Save Entry")

    if submitted:
        if title.strip() and details.strip():
            data["notes"].append({
                "type": category,
                "title": title,
                "details": details
            })
            if save_data():
                st.success("Journal entry saved.")
            else:
                st.error("Could not save journal entry.")
        else:
            st.error("Enter a title and some notes.")

    st.subheader("Saved Strategies, Campaigns & Notes")

    if data["notes"]:
        for item in data["notes"]:
            with st.expander(
                item.get("type", "Note") + " — " + item.get("title", "Untitled")
            ):
                st.write(item.get("details", ""))
                for key, value in item.items():
                    if key not in ["type", "title", "details"]:
                        st.caption(str(key).title() + ": " + str(value))
    else:
        st.info("No saved notes yet.")

    st.download_button(
        "Export Journal",
        json.dumps(data["notes"], indent=2, ensure_ascii=False),
        file_name="executive_journal.json",
        mime="application/json"
    )

# ---------- FOOTER ----------
st.markdown("---")
st.caption(
    "MODISON GROUP | CEO COMMAND CENTER | "
    "Fictional business simulation for personal use."
)

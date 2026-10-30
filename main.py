import streamlit as st
from datetime import date

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Study Planner",
    page_icon="📚",
    layout="wide"
)

# ---------------- DESIGN - FIXED ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F7F8FC;
}
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* FORCE ALL TEXT TO BE DARK - THIS FIXES YOUR ISSUE */
.stApp, .stApp p, .stApp span, .stApp div, .stApp label, .stApp h1, .stApp h2, .stApp h3,
.stMarkdown, .stMarkdown p, .stCaption, [data-testid="stWidgetLabel"] p {
    color: #24264B !important;
}

/* FORCE INPUTS TO BE WHITE WITH BLACK TEXT - FIXES BLACK SEARCH BAR */
div[data-baseweb="base-input"], 
div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input,
div[data-testid="stDateInput"] input,
textarea {
    background-color: white !important;
    color: #24264B !important;
    border-color: #E5E7F2 !important;
}
div[data-baseweb="base-input"] input,
div[data-baseweb="select"] span,
div[data-baseweb="select"] div {
    color: #24264B !important;
}

/* Placeholder color */
input::placeholder {
    color: #888 !important;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E5E7F2;
    padding: 18px;
    border-radius: 14px;
}
div[data-testid="stMetric"] label, div[data-testid="stMetric"] div {
    color: #24264B !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border-radius: 14px;
}
div[data-testid="stVerticalBlockBorderWrapper"] * {
    color: #24264B !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

SUBJECTS = [
    "Python Programming",
    "Engineering Mathematics",
    "Data Structures",
    "Artificial Intelligence",
    "Other"
]

PRIORITIES = ["High", "Medium", "Low"]

# ---------------- HEADER ----------------
st.title("📚 Student Productivity Planner")
st.write("Plan your studies, manage assignments, and track your progress.")
st.divider()

# ---------------- DASHBOARD ----------------
tasks = st.session_state.tasks

total = len(tasks)
completed = sum(1 for task in tasks if task["completed"])
pending = total - completed
progress = completed / total if total else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("📋 Total Tasks", total)
col2.metric("✅ Completed", completed)
col3.metric("⏳ Pending", pending)
col4.metric("📈 Progress", f"{progress * 100:.0f}%")

st.progress(progress)

# ---------------- ADD TASK ----------------
st.subheader("➕ Add a New Task")

with st.form("add_task_form", clear_on_submit=True):
    task_name = st.text_input(
        "Task name",
        placeholder="e.g. Complete Python assignment"
    )

    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox("Subject", SUBJECTS)
        deadline = st.date_input("Deadline", value=date.today())

    with col2:
        priority = st.selectbox("Priority", PRIORITIES)
        task_type = st.selectbox(
            "Task type",
            ["Assignment", "Study", "Exam Preparation", "Project"]
        )

    description = st.text_input(
        "Notes (optional)",
        placeholder="Add a short note"
    )

    submitted = st.form_submit_button(
        "Add Task",
        use_container_width=True
    )

if submitted:
    if task_name.strip():
        new_task = {
            "id": st.session_state.next_id,
            "name": task_name.strip(),
            "subject": subject,
            "deadline": deadline,
            "priority": priority,
            "type": task_type,
            "notes": description.strip(),
            "completed": False
        }

        st.session_state.tasks.append(new_task)
        st.session_state.next_id += 1

        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a task name.")

# ---------------- SEARCH AND FILTERS ----------------
st.divider()
st.subheader("📝 Your Study Tasks")

search_text = st.text_input(
    "🔍 Search tasks",
    placeholder="Search by task name or notes"
)

filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:
    selected_subject = st.selectbox(
        "Filter by subject",
        ["All Subjects"] + SUBJECTS
    )

with filter_col2:
    selected_status = st.selectbox(
        "Filter by status",
        ["All Tasks", "Pending", "Completed"]
    )

with filter_col3:
    selected_priority = st.selectbox(
        "Filter by priority",
        ["All Priorities"] + PRIORITIES
    )

filtered_tasks = []

for task in st.session_state.tasks:
    matches_search = (
        search_text.strip().lower() in task["name"].lower()
        or search_text.strip().lower() in task["notes"].lower()
    )

    matches_subject = (
        selected_subject == "All Subjects"
        or task["subject"] == selected_subject
    )

    matches_status = (
        selected_status == "All Tasks"
        or (selected_status == "Completed" and task["completed"])
        or (selected_status == "Pending" and not task["completed"])
    )

    matches_priority = (
        selected_priority == "All Priorities"
        or task["priority"] == selected_priority
    )

    if (
        matches_search
        and matches_subject
        and matches_status
        and matches_priority
    ):
        filtered_tasks.append(task)

# ---------------- DISPLAY TASKS ----------------
if not filtered_tasks:
    st.info("No matching tasks yet. Add a task using the form above.")
else:
    for task in filtered_tasks:
        with st.container(border=True):
            task_col, action_col = st.columns([4, 1])

            with task_col:
                if task["completed"]:
                    st.markdown(f"### ✅ ~~{task['name']}~~")
                else:
                    st.markdown(f"### 📘 {task['name']}")

                st.write(
                    f"**Subject:** {task['subject']}  ·  "
                    f"**Type:** {task['type']}"
                )

                st.write(
                    f"**Deadline:** {task['deadline'].strftime('%d %b %Y')}  ·  "
                    f"**Priority:** {task['priority']}"
                )

                if task["notes"]:
                    st.caption(task["notes"])

                if task["deadline"] < date.today() and not task["completed"]:
                    st.warning("Deadline has passed!")

            with action_col:
                if not task["completed"]:
                    if st.button(
                        "Complete",
                        key=f"complete_{task['id']}",
                        use_container_width=True
                    ):
                        for saved_task in st.session_state.tasks:
                            if saved_task["id"] == task["id"]:
                                saved_task["completed"] = True
                        st.rerun()
                else:
                    if st.button(
                        "Undo",
                        key=f"undo_{task['id']}",
                        use_container_width=True
                    ):
                        for saved_task in st.session_state.tasks:
                            if saved_task["id"] == task["id"]:
                                saved_task["completed"] = False
                        st.rerun()

                if st.button(
                    "Delete",
                    key=f"delete_{task['id']}",
                    use_container_width=True
                ):
                    st.session_state.tasks = [
                        saved_task
                        for saved_task in st.session_state.tasks
                        if saved_task["id"] != task["id"]
                    ]
                    st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "Study Planner | Built with Python and Streamlit"
)

import streamlit as st

st.title("Campus Lost & Found")
st.write("Report lost items and search for them.")

if "items" not in st.session_state:
    st.session_state.items = []

st.header("Add an Item")

name = st.text_input("Item name")
location = st.text_input("Where was it lost or found?")

if st.button("Add Item"):
    if name.strip() and location.strip():
        st.session_state.items.append({
            "name": name.strip(),
            "location": location.strip()
        })
        st.success("Item added successfully!")
    else:
        st.warning("Please fill in both fields.")

st.header("Search for an Item")
search = st.text_input("Enter item name")

if st.button("Search Item"):
    results = [
        item for item in st.session_state.items
        if search.lower() in item["name"].lower()
    ]

    if results:
        for item in results:
            st.write("Item:", item["name"])
            st.write("Location:", item["location"])
    else:
        st.info("No matching items found.")

st.header("All Items")

for item in st.session_state.items:
    st.write(f'{item["name"]} — {item["location"]}')

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "https://fastapi-project-5-skillswap-platform.onrender.com"

st.set_page_config(
    page_title="SkillSwap Platform",
    page_icon="🔁",
    layout="wide"
)

# ------------------------------
# Sidebar Navigation
# ------------------------------

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "View Skills",
        "Add Skill",
        "Search Skill",
        "Skill Matches",
        "Update User",
        "Delete User"
    ]
)

# ------------------------------
# DASHBOARD
# ------------------------------

if menu == "Dashboard":

    st.title("🔁 SkillSwap Platform")
    st.subheader("Exchange skills instead of money")

    if st.button("🔄 Refresh Data"):
        st.rerun()

    try:
        response = requests.get(f"{API_URL}/skills", timeout=10)
        data = response.json()
        df = pd.DataFrame(data)

        if not df.empty:

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Users", len(df))
            col2.metric("Unique Skills", df["can_teach"].nunique())
            col3.metric("Learning Requests", df["wants_to_learn"].nunique())

            st.divider()

            st.subheader("🔥 Most Popular Skills")

            skill_counts = df["can_teach"].value_counts().reset_index()
            skill_counts.columns = ["Skill", "Count"]

            fig = px.bar(
                skill_counts,
                x="Skill",
                y="Count",
                text="Count",
                color="Skill",
                title="Skill Popularity"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.divider()

            st.subheader("👥 Users on Platform")

            st.dataframe(df, use_container_width=True)

        else:
            st.info("No users yet. Add some skills!")

    except requests.exceptions.RequestException:
        st.error("⚠ Backend server is not responding. Render may be waking up.")

# ------------------------------
# VIEW SKILLS
# ------------------------------

elif menu == "View Skills":

    st.header("All Skills")

    try:
        r = requests.get(f"{API_URL}/skills", timeout=10)
        df = pd.DataFrame(r.json())

        st.dataframe(df, use_container_width=True)

    except:
        st.error("Could not load skills")

# ------------------------------
# ADD SKILL
# ------------------------------

elif menu == "Add Skill":

    st.header("Add New Skill")

    username = st.text_input("Username")
    can_teach = st.text_input("Skill You Can Teach")
    wants_to_learn = st.text_input("Skill You Want to Learn")

    if st.button("Add Skill"):

        if username and can_teach and wants_to_learn:

            payload = {
                "username": username,
                "can_teach": can_teach,
                "wants_to_learn": wants_to_learn
            }

            try:
                requests.post(f"{API_URL}/skills/add", json=payload, timeout=10)
                st.success("Skill added successfully")

            except:
                st.error("Error adding skill")

        else:
            st.warning("Please fill all fields")

# ------------------------------
# SEARCH SKILL
# ------------------------------

elif menu == "Search Skill":

    st.header("Search Users by Skill")

    skill = st.text_input("Enter Skill")

    if st.button("Search"):

        if skill:

            try:
                r = requests.get(
                    f"{API_URL}/skills/search",
                    params={"skill": skill},
                    timeout=10
                )

                df = pd.DataFrame(r.json())

                if df.empty:
                    st.warning("No users found with this skill")
                else:
                    st.dataframe(df)

            except:
                st.error("Search failed")

        else:
            st.warning("Please enter a skill")

# ------------------------------
# MATCHES
# ------------------------------

elif menu == "Skill Matches":

    st.header("Skill Exchange Matches")

    try:
        r = requests.get(f"{API_URL}/skills/match", timeout=10)

        df = pd.DataFrame(r.json())

        if df.empty:
            st.info("No matches found yet")
        else:
            st.dataframe(df)

    except:
        st.error("Could not load matches")

# ------------------------------
# UPDATE USER
# ------------------------------

elif menu == "Update User":

    st.header("Update User Skill")

    username = st.text_input("Username")
    can_teach = st.text_input("New Teaching Skill")
    wants_to_learn = st.text_input("New Learning Skill")

    if st.button("Update User"):

        if username and can_teach and wants_to_learn:

            payload = {
                "username": username,
                "can_teach": can_teach,
                "wants_to_learn": wants_to_learn
            }

            try:
                requests.put(
                    f"{API_URL}/skills/update",
                    json=payload,
                    timeout=10
                )

                st.success("User updated successfully")

            except:
                st.error("Update failed")

        else:
            st.warning("Please fill all fields")

# ------------------------------
# DELETE USER
# ------------------------------

elif menu == "Delete User":

    st.header("Delete User")

    username = st.text_input("Username")

    if st.button("Delete User"):

        if username:

            try:
                requests.delete(
                    f"{API_URL}/skills/delete/{username}",
                    timeout=10
                )

                st.success("User deleted successfully")

            except:
                st.error("Delete failed")

        else:
            st.warning("Please enter a username")

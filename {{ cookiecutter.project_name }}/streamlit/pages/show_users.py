from datetime import datetime

import streamlit as st
from {{cookiecutter.project_slug}}.db.sync.services import get_all_users, find_user_by_username
from {{cookiecutter.project_slug}}.schemas import UserModel


def main():
    st.set_page_config(page_title="Show users", page_icon="📈")

    st.title("Find user")
    username = st.text_input("Username")

    if username:
        if found_user := find_user_by_username(username=username):
            st.write(f"User found: {found_user.age} years old")
        else:
            st.error("User not found")

    st.divider()
    st.title("All users")

    users = get_all_users()
    for user in users:
        st.subheader(f"User ID: {user.id}")
        st.markdown(f"**Name:** {user.username}")
        st.markdown(f"**Age:** {user.age}")
        st.markdown("---")

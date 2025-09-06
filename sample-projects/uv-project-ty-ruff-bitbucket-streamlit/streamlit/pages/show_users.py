import streamlit as st
from uv_project_ty_ruff_bitbucket_streamlit.db.sync.services import find_user_by_username, get_all_users

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

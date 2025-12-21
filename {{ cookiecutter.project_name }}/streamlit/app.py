import streamlit as st
from config import AppSettings

app_settings = AppSettings()

if app_settings.create_all_tables:
    # Debug mode - just create all models as is
    # If you need to update models - wipe down your DB
    st.write("Creating DB tables explicitly")
    from {{cookiecutter.project_slug}}.db.sync.engine import Base, engine

    Base.metadata.create_all(engine)

st.set_page_config(page_title="User management", page_icon=":robot:", layout="wide")

pages = [
    st.Page("pages/show_users.py", url_path="users", title="Users"),
    st.Page("pages/add_user.py", url_path="new-user", title="Add user"),
]

navigator = st.navigation(pages, position="sidebar", expanded=True)
navigator.run()

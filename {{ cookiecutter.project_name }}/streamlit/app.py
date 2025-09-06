from pages import add_user, show_users

import streamlit as st
from {{cookiecutter.project_slug}}.settings import StreamlitAppSettings


app_settings = StreamlitAppSettings()

if app_settings.create_all_tables:
    # Debug mode - just create all models as is
    # If you need to update models - wipe down your DB
    st.write("Creating DB tables explicitly")
    from {{cookiecutter.project_slug}}.db.sync.engine import Base, engine

    Base.metadata.create_all(engine)

st.set_page_config(page_title="User management", page_icon=":robot:", layout="wide")

pages = [
    st.Page(show_users.main, url_path="users", title="Users"),
    st.Page(add_user.main, url_path="new-user", title="Add user"),
]

navigator = st.navigation(pages, position="sidebar", expanded=True)
navigator.run()

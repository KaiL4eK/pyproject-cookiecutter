import streamlit as st
from {{cookiecutter.project_slug}}.db.sync.services import add_new_user
from {{cookiecutter.project_slug}}.schemas import UserModel


def main():
    st.set_page_config(page_title="Add user")

    username = st.text_input("Username")
    age = st.text_input("Age")

    if st.button("Add user"):
        new_user = UserModel(username=username, age=age)
        add_new_user(new_user)
        st.success("Successfully added user!")

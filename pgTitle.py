import streamlit as st


#Startup Page

st.title("CI-QUALITY WEEK GAMES")

if st.button(label="Escape Room", key=None, help=None, type="primary", icon=None,
            disabled=False, use_container_width=True):
    st.switch_page("pg1.py")
if st.button(label="Jeopardy", key=None, help=None, type="primary", icon=None,
            disabled=False, use_container_width=True):
        st.switch_page("pg2.py")
if st.button(label="Root Cause Analysis", key=None, help=None, type="primary", icon=None,
            disabled=False, use_container_width=True):
        st.switch_page("pg3.py")
import streamlit as st


#Startup Page

st.title("8 STEP A3 PROBLEM SOLVING")
st.title("MISSION IMPOSSIBLE")

if st.button(label="Begin Mission", key=None, help=None, type="primary", icon=None,
            disabled=False, use_container_width=True):
    st.switch_page("pg1.py")

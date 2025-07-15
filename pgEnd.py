import streamlit as st


#Startup Page
st.title("MISSION IMPOSSIBLE: COMPLETE")
st.header("8 STEP A3 PROBLEM SOLVING", divider="red")


if st.button(label="Begin Mission", key=None, help=None, type="primary", icon=None,
            disabled=False, use_container_width=True):
    st.switch_page("pg1.py")

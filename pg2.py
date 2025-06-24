import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Batch Job", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

st.markdown("### Jeopardy")
#use st.dialog function to pop up with each question & submit

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write("LPA")
    st.button("A1", type="primary", use_container_width=True)
    st.button("A2", type="primary", use_container_width=True)
    st.button("A3", type="primary", use_container_width=True)
    st.button("A4", type="primary", use_container_width=True)
    st.button("A5", type="primary", use_container_width=True)
with col2:
    st.write("Topic 2")
    st.button("B1", type="primary", use_container_width=True)
    st.button("B2", type="primary", use_container_width=True)
    st.button("B3", type="primary", use_container_width=True)
    st.button("B4", type="primary", use_container_width=True)
    st.button("B5", type="primary", use_container_width=True)
with col3:
    st.write("Topic 3")
    st.button("C1", type="primary", use_container_width=True)
    st.button("C2", type="primary", use_container_width=True)
    st.button("C3", type="primary", use_container_width=True)
    st.button("C4", type="primary", use_container_width=True)
    st.button("C5", type="primary", use_container_width=True)
with col4:
    st.write("Topic 4")
    st.button("D1", type="primary", use_container_width=True)
    st.button("D2", type="primary", use_container_width=True)
    st.button("D3", type="primary", use_container_width=True)
    st.button("D4", type="primary", use_container_width=True)
    st.button("D5", type="primary", use_container_width=True)
with col5:
    st.write("Topic 5")
    st.button("E1", type="primary", use_container_width=True)
    st.button("E2", type="primary", use_container_width=True)
    st.button("E3", type="primary", use_container_width=True)
    st.button("E4", type="primary", use_container_width=True)
    st.button("E5", type="primary", use_container_width=True)








import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Batch Job", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

st.markdown("### TASK 6: DEVELOP COUNTERMEASURES")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.write("1")
    st.number_input("1")
    
with col2:
    st.write("2")
    st.number_input("2")

with col3:
    st.write("ROI")
    st.number_input("3")

with col4:
    st.write("4")
    st.number_input("4")

with col5:
    st.write("5")
    st.number_input("5")

with col6:
    st.write("6")

with col7: 
    st.write("Total")
    st.write("11")
    st.write("6")

#ADD THE PART ABOUT SENTENCE STRUCTURE


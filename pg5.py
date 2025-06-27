import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Batch Job", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 5: ROOT CAUSE ANALYSIS")
st.markdown("##### Fishbone Diagram")
st.write("image")

st.markdown("Given the wordbank and the diagram above, enter the corresponding answer.")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    man = st.text_input("Man", key=0)
    
with col2:
    method = st.text_input("Method", key=1)

with col3:
    material = st.text_input("Material", key=2)

with col4:
    machine = st.text_input("Machine", key=3)

with col5:
    environment = st.text_input("Environment", key=4)

with col6:
    management = st.text_input("Management", key=5)





st.markdown("---")  # Horizontal line

st.markdown("### Direct Cause")
st.markdown("Pick the most direct cause.")

st.markdown("---")  # Horizontal line

st.markdown("### 5 Whys")

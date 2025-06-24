import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Batch Job", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

st.markdown("### Fishbone Diagram")
#use st.dialog function to pop up with each question & submit

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write("Material")
    material = st.text_input("Enter answer here", key=0)
    
with col2:
    st.write("Method")
    method = st.text_input("Enter answer here", key=1)

with col3:
    st.write("Management")
    management = st.text_input("Enter answer here", key=2)

with col4:
    st.write("Machine")
    machine = st.text_input("Enter answer here", key=3)

with col5:
    st.write("Environment")
    environment = st.text_input("Enter answer here", key=4)





st.markdown("---")  # Horizontal line

st.markdown("### Direct Cause")


st.markdown("---")  # Horizontal line

st.markdown("### 5 Whys")






st.markdown("---")  # Horizontal line

st.markdown("### Develop Countermeasures")

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

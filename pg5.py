import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Batch Job", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

#initialize session states
if "activity5a" not in st.session_state:
        st.session_state.activity5a = False

if "activity5b" not in st.session_state:
        st.session_state.activity5b = False

if "activity5c" not in st.session_state:
        st.session_state.activity5c = False



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



if "activity5a" not in st.session_state:
    st.session_state.activity5a = False
# Button - submit code
if st.button("Submit Answers", key="5a", type="primary"):

    if True:
        st.session_state.activity5a = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

if st.session_state.activity5a:
        
    st.markdown("---")  # Horizontal line

    st.markdown("### Direct Cause")
    st.markdown("Pick the most direct cause.")
    st.selectbox("label", [man, method, material, machine, environment, management])

    if "activity5b" not in st.session_state:
        st.session_state.activity5b = False
    # Button - submit code
    if st.button("Submit Answers", key="5b", type="primary"):

        if True:
            st.session_state.activity5b = True
            st.success("You got it!")
        else:
            st.error("Your answer is incorrect. Please try again.")

if st.session_state.activity5b:

    st.markdown("---")  # Horizontal line

    st.markdown("### 5 Whys")

    st.markdown("Read this excerpt and use it to complete the activity below.")
    st.text_area("Example Exerpt",
                "This is where the A3 story/scenario will go for the users to read.")
    st.markdown("Order these statements in the correct order.")


    st.selectbox("statement 1", [1,2,3,4,5])
    st.selectbox("statement 2", [1,2,3,4,5])
    st.selectbox("statement 3", [1,2,3,4,5])
    st.selectbox("statement 4", [1,2,3,4,5])
    st.selectbox("statement 5", [1,2,3,4,5])

    if "activity5c" not in st.session_state:
        st.session_state.activity5c = False
    # Button - submit code
    if st.button("Submit Answers", key="5c", type="primary"):

        if True:
            st.session_state.activity5c = True
            st.success("You got it!")
        else:
            st.error("Your answer is incorrect. Please try again.")

if st.session_state.activity5c:
    st.markdown("---")
    st.write("Please note: *insert statement about Root Cause Analysis*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg6.py")
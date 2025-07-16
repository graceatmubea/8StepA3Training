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





if "activity6" not in st.session_state:
    st.session_state.activity6 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if True:
        st.session_state.activity6 = True
        st.success("You got it!")
    else:
        st.error("One or more of your numbers are incorrect. Please try again.")

# Follow up question
if st.session_state.activity6:
    st.markdown("---")
    st.write("One more thing before we move to the next task. Please answer the question below.")
    st.write("What information should NOT be included in the A3 header?")

    answerP6Q1 = "Coach's Date of Birth"
    headerQ1 = st.radio(
        "What information should NOT be included in the A3 header?",
        ["Project Owner's Name", "Coach's Date of Birth",
         "Project Start & End Date", "Project Area/Location"],
        index=None, key="header_Q1"
    )

    if headerQ1 == answerP6Q1:
        st.success("You are correct! Click the button below to move to the next task.")
        if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg2.py")
    elif headerQ1 == None:
        st.markdown("Please select an answer")
    else:
        st.error("Incorrect. Please try again.")


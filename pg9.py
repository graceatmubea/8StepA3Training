import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Standardize", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 9: STANDARDIZE & SHARE")
st.markdown("Quiz Style - 3 multiple choice questions")

answerP9Q1 = "To ensure improvements are sustained over time"
pg9Q1 = st.radio(
    "1. What is the goal of the Standardization step in the A3 process?",
    ["To test different hypotheses",
    "To ensure improvements are sustained over time",
    "To collect scrap data",
    "To assign a new budget"],
    index=None, key="pg9Q1"
)
answerP9Q2 = "Work Instruction"
pg9Q2 = st.radio(
    "2. Which of the following is an example of a standardization document?",
    ["Brainstorming Sheet",
    "A3 Summary Sheet",
    "5 Why's Analysis",
    "Work Instruction"],
    index=None, key="pg9Q2"
)
answerP9Q3 = "The Point of Occurrence (PoO) of the defect"
pg9Q3 = st.radio(
    "3. Why is it important to update the PFMEA after implementing improvements?",
    ["To inform the HR department",
    "To comply with marketing requirements",
    "To reflect updated risks and controls in the process",
    "To reduce training time"],
    index=None, key="pg9Q3"
)

if "activity9" not in st.session_state:
    st.session_state.activity9 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    #boolean to test Q1-Q5 for correctness
    boolX = False
    boolY = False
    boolZ = False 
    
    
    if pg9Q1 == answerP9Q1:
        boolX = True
    else:
         st.error("Question 1 is incorrect.")
    if pg9Q2 == answerP9Q2:
        boolY = True
    else:
         st.error("Question 2 is incorrect.")
    if pg9Q3 == answerP9Q3:
        boolZ = True
    else:
         st.error("Question 3 is incorrect.")

    if boolX and boolY and boolZ:
        st.session_state.activity9 = True
        st.success("You got it!")


# Follow up question
if st.session_state.activity9:
    st.markdown("---")
    st.write("Please note: *insert statement about break down problem*")
    if st.button("COMPLETE MISSION", type="primary"):
            st.switch_page("pgEnd.py")
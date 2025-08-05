import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Breakdown", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 3: BREAKDOWN")
st.markdown("Answer the 5 multiple choice questions below.")


answerP3Q1 = "Pareto Chart"
pg3Q1 = st.radio(
    "Q1. Which tool is most commonly used to prioritize defects during the breakdown phase?",
    ["Fishbone Diagram",
    "Pareto Chart",
    "Control Chart",
    "Flow Chart"],
    index=None, key="pg3Q1"
)
answerP3Q2 = "The point in the process with the highest impact on the issue"
pg3Q2 = st.radio(
    "Q2. What does 'Priority Point' refer to during the Breakdown step?",
    ["The team member leading the step",
    "The final result of the project",
    "The department where the problem started",
    "The point in the process with the highest impact on the issue"],
    index=None, key="pg3Q2"
)

answerP3Q3 = "The Point of Occurrence (PoO) of the defect"
pg3Q3 = st.radio(
    "Q3. What is typically identified after creating a process flow diagram in the breakdown step?",
    ["The budget of the project",
    "The root cause of the problem",
    "The Point of Occurrence (PoO) of the defect",
    "The final countermeasure"],
    index=None, key="pg3Q3"
)
st.image("pg3pic.png")
answerP3Q4 = "Clamp Marks:   **20%**"
pg3Q4 = st.radio(
    "Q4. Verify the project breakdown above. If there is an error, select it below. Assume everything else is correct.",
    ["Welding:   **25%**",
    "Tube Bender #3:   **30%**",
    "Clamp Marks:   **20%**",
    "No errors found"],
    index=None, key="pg3Q4"
)

if "activity3" not in st.session_state:
    st.session_state.activity3 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    #boolean to test Q1-Q5 for correctness
    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    

    if pg3Q1 == answerP3Q1:
        bool1 = True
    else:
         st.error("Question 1 is incorrect.")
    if pg3Q2 == answerP3Q2:
        bool2 = True
    else:
         st.error("Question 2 is incorrect.")
    if pg3Q3 == answerP3Q3:
        bool3 = True
    else:
         st.error("Question 3 is incorrect.")
    if pg3Q4 == answerP3Q4:
        bool4 = True
    else:
         st.error("Question 4 is incorrect.")
         

    if bool1 and bool2 and bool3 and bool4 and bool5:
        st.session_state.activity3 = True
        st.success("You got it!")


# Follow up question
if st.session_state.activity3:
    st.markdown("---")
    st.write(":dart: *It's important that the goal aligns with the identified problem because if it doesn't, the actions taken may not solve the actual problem!*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg4.py")
import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Breakdown", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 3: BREAKDOWN")
st.markdown("Answer the 5 multiple choice questions below.")

answerP3Q1 = "To understand and isolate where the problem occurs"
pg3Q1 = st.radio(
    "Q1. What is the main purpose of the 'Breakdown the Problem' Step in the A3 Process?",
    ["To test different solutions",
    "To define the ideal future state",
    "To understand and isolate where the problem occurs",
    "To assign the team roles"],
    index=None, key="pg3Q1"
)
answerP3Q2 = "Pareto Chart"
pg3Q2 = st.radio(
    "Q2. Which tool is most commonly used to prioritize defects during the breakdown phase?",
    ["Fishbone Diagram",
    "Pareto Chart",
    "Control Chart",
    "Flow Chart"],
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
answerP3Q4 = "The defect with the highest frequency or cost"
pg3Q4 = st.radio(
    "Q4. When reviewing defects, which of the following should be prioritized?",
    ["The defect with the most visibility to leadership",
    "The defect with the lowest cost impact",
    "The defect with the highest frequency or cost",
    "The defect found in the latest shipment"],
    index=None, key="pg3Q4"
)
answerP3Q5 = "The point in the process with the highest impact on the issue"
pg3Q5 = st.radio(
    "Q5. What does 'Priority Point' refer to during the Breakdown step?",
    ["The team member leading the step",
    "The final result of the project",
    "The department where the problem started",
    "The point in the process with the highest impact on the issue"],
    index=None, key="pg3Q5"
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
    bool5 = False
    

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
    if pg3Q5 == answerP3Q5:
        bool5 = True
    else:
         st.error("Question 5 is incorrect.")
         

    if bool1 and bool2 and bool3 and bool4 and bool5:
        st.session_state.activity3 = True
        st.success("You got it!")


# Follow up question
if st.session_state.activity3:
    st.markdown("---")
    st.write(":dart: *It's important that the goal aligns with the identified problem because if it doesn't, the actions taken may not solve the actual problem!*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg4.py")
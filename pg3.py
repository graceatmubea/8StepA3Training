import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Activity 3", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 3: BREAKDOWN")
st.markdown("Quiz Style - 5 multiple choice questions")

answerP3Q1 = st.pills(
    "Q1",
    options=["a1","a2","a3"],
    selection_mode="single"
)
answerP3Q2 = st.pills(
    "Q2",
    options=["b1","b2","b3"],
    selection_mode="single"
)
answerP3Q3 = st.pills(
    "Q3",
    options=["c1","c2","c3"],
    selection_mode="single"
)
answerP3Q4 = st.pills(
    "Q4",
    options=["d1","d2","d3"],
    selection_mode="single",
)
answerP3Q5 = st.pills(
    "Q5",
    options=["e1","e2","e3"],
    selection_mode="single",
)

if "activity3" not in st.session_state:
    st.session_state.activity3 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    #boolean to test Q1-Q5 for correctness
    boolP3 = False
    if True:
         boolP3 = True

    if boolP3:
        st.session_state.activity3 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity3:
    st.markdown("---")
    st.write("Please note: *insert statement about break down problem*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg4.py")
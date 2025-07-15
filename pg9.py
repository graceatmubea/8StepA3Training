import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Activity 3", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 9: STANDARDIZE & SHARE")
st.markdown("Quiz Style - 3 multiple choice questions")

answerP9Q1 = st.pills(
    "Q1",
    options=["a1","a2","a3"],
    selection_mode="single"
)
answerP9Q2 = st.pills(
    "Q2",
    options=["b1","b2","b3"],
    selection_mode="single"
)
answerP9Q3 = st.pills(
    "Q3",
    options=["c1","c2","c3"],
    selection_mode="single"
)

if "activity9" not in st.session_state:
    st.session_state.activity9 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    #boolean to test Q1-Q5 for correctness
    boolP9 = False
    if True:
         boolP9 = True

    if boolP9:
        st.session_state.activity9 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity9:
    st.markdown("---")
    st.write("Please note: *insert statement about break down problem*")
    if st.button("COMPLETE MISSION", type="primary"):
            st.switch_page("pgEnd.py")
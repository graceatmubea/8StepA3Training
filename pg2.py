import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Activity 2", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 2: CURRENT CONDITION")
st.markdown("Using the diagram and information provided below, determine the missing value.")

st.image("pg2pic.jpg", width=600)

answerP2Q1 = st.number_input("Enter your answer below (ANSWER IS 3)", min_value=0.0, step=0.1)

if "activity2" not in st.session_state:
    st.session_state.activity2 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if answerP2Q1 == 3:
        st.session_state.activity2 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity2:
    st.markdown("---")
    st.write("Please note: *insert statement about current condition*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg3.py")
    






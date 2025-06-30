import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Activity 3", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 3: BREAKDOWN")
st.markdown("Quiz Style - 5 multiple choice questions")

if "activity3" not in st.session_state:
    st.session_state.activity3 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if True:
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
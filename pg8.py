import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Monitor Results", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 8: MONITOR RESULTS")

st.markdown("*Picture of Chart 1*")
st.markdown("*Picture of Chart 2*")
st.markdown("*Picture of Chart 3*")

st.markdown("Looking at the 3 different results displayed above, decide whether each project is able to be closed. Why? ")
st.markdown(" Use words from the wordbank provided below in your 1-2 sentence explanation.")


st.markdown(":blue-badge[Baseline] :green-badge[Improvement] :violet-badge[Implementation] :orange-badge[Standard]")

st.text_area("Scenario 1", height=68)
st.text_area("Scenario 2", height=68)
st.text_area("Scenario 3", height=68)

st.markdown("To check your answers, please show them to the training proctor for verification.")

answerP8Q1 = st.number_input("Enter the code to move on to the final task: (answer is 123)", )
if "activity8" not in st.session_state:
    st.session_state.activity8 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if answerP8Q1 == 123:
        st.session_state.activity8 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity8:
    st.markdown("---")
    st.write("Please note: *insert statement about current condition*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg9.py")


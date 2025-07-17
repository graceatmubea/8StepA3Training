import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Monitor Results", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 8: MONITOR RESULTS")

st.markdown("Looking at the 3 different scenarios below, decide whether each project is able to be closed. Why?")
st.markdown("*Use keywords from the wordbank provided below in your 1-2 sentence explanation.*")


st.markdown(":blue-badge[Baseline] :green-badge[Improvement] :violet-badge[Implementation] :orange-badge[Standard]")

tab1, tab2, tab3 = st.tabs(["Scenario 1", "Scenario 2", "Scenario 3"])
with tab1:
    st.image("pg8pic1.png")
    st.text_area("Scenario 1")
with tab2:
    st.image("pg8pic2.png")
    st.text_area("Scenario 2")
with tab3:
    st.image("pg8pic3.png")
    st.text_area("Scenario 3")

st.divider()

st.markdown("To check your answers, please show them to the training proctor for verification.")

answerP8Q1 = st.number_input("Enter the code to move on to the final task: (answer is 123)", value=None, step=0)
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
    st.write("Please note: *insert statement about monitor results*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg9.py")


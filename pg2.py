import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Current Condition", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 2: CURRENT CONDITION")
st.markdown("Using the diagram and information provided below, determine the missing value.")

st.image("pg2pic.jpg", width=1800)

answerP2Q1 = st.number_input("Enter your answer below. (Format 100% as 100)", min_value=0.0, step=0.1)

if "activity2" not in st.session_state:
    st.session_state.activity2 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if answerP2Q1 == 2.5:
        st.session_state.activity2 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity2:
    st.markdown("---")
    st.write(":dart: Measurable data, graphs, or photos of the issue should be included in the current condition to make it useful.")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg3.py")
    






import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Current Condition", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 1: CURRENT CONDITION")
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
    st.write("One more question before we move to the next task. Please answer the question below.")
    st.code("The long-term target or ideal outcome you aim to achieve. It represents the optimal state of the process once all improvements have been successfully implemented. It is ambitious but achievable.", language=None, wrap_lines=True)

    answerP2Q1 = "Ultimate Goal"
    pg2q1 = st.radio(
        "What is the given statement the definition for?",
        ["Standard Goal",
         "Ultimate Goal"],
        index=None, key="pg2q1"
    )

    if pg2q1 == answerP2Q1:
        st.success("You are correct! Click the button below to move to the next task.")
        if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg3.py")
    elif pg2q1 == None:
        st.markdown("Please select an answer")
    else:
        st.error("Incorrect. Please try again.")
    






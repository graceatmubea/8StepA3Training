import streamlit as st


# Set page title
st.set_page_config(page_title="Header", layout="centered")

if st.button(label="Return to Home Page", key=None, help=None, type="secondary", icon=None,
             disabled=False, use_container_width=False):
    st.switch_page("pgTitle.py")

# Title
st.markdown("### TASK 1: HEADER")
st.markdown("*Offline Activity*")
st.write("When you've finished arranging the pieces into their proper sections in front of you, please enter the corresponding code into the boxes below.")

st.markdown("#### Enter the secret code below: (ANSWER IS 123)")

#Enter code
code1 = st.number_input("", min_value=0)

if "activity1" not in st.session_state:
    st.session_state.activity1 = False

# Button - submit code
if st.button("Submit Answers", type="primary"):
    if code1 == 123:
        st.session_state.activity1 = True
        st.success("You got it!")
    else:
        st.error("One or more of your numbers are incorrect. Please try again.")

# Follow up question
if st.session_state.activity1:
    st.markdown("---")
    st.write("One more thing before we move to the next task. Please answer the question below.")
    #st.write("What information should NOT be included in the A3 header?")

    answerP1Q1 = "Tom Muhr"
    headerQ1 = st.radio(
        "What name should be written on the header of the A3?",
        ["T. Muhr", "TomTom",
         "Tom", "Tom Muhr"],
        index=None, key="header_Q1"
    )

    if headerQ1 == answerP1Q1:
        st.success("You are correct! Click the button below to move to the next task.")
        if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg2.py")
    elif headerQ1 == None:
        st.markdown("Please select an answer")
    else:
        st.error("Incorrect. Please try again.")



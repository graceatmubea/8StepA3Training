import streamlit as st


# Set page title
st.set_page_config(page_title="Activity 1", layout="centered")

if st.button(label="Return to Home Page", key=None, help=None, type="secondary", icon=None,
             disabled=False, use_container_width=False):
    st.switch_page("pgTitle.py")

# Title
st.markdown("# TASK 1: HEADER")
st.write("When you've finished arranging the pieces into their proper sections in front of you, please enter the corresponding code into the boxes below.")

st.markdown("#### Enter the secret code below:")

left, middle, right = st.columns([3, 3, 3], vertical_alignment="top")

#Enter code
with left:
    code1 = st.number_input("First number", min_value=0)
with middle:
    code2 = st.number_input("Second number", min_value=0)
with right:
    code3 = st.number_input("Third number", min_value=0)

if "activity1" not in st.session_state:
    st.session_state.activity1 = False

# Button - submit code
if st.button("Submit Answers"):
    if code1 == 1 and code2 == 2 and code3 == 3:
        st.session_state.activity1 = True
        st.success("You got it!")
    else:
        st.error("One or more of your numbers are incorrect. Please try again.")

# Follow up question
if st.session_state.activity1:
    st.markdown("---")
    st.write("One more thing before we move to the next task. Please answer the question below.")
    st.write("What information should NOT be included in the A3 header?")

    answerQ1 = "Coach's Date of Birth"
    headerQ1 = st.radio(
        "What information should NOT be included in the A3 header?",
        ["Project Owner's Name", "Coach's Date of Birth",
         "Project Start & End Date", "Project Area/Location"],
        index=None, key="header_Q1"
    )

    if headerQ1 == answerQ1:
        st.success("You are correct! Click the button below to move to the next task.")
        if st.button("CONTINUE MISSION", type="primary"):
            st.switch_page("pg2.py")
    elif headerQ1 == None:
        st.markdown("Please select an answer")
    else:
        st.error("Incorrect. Please try again.")



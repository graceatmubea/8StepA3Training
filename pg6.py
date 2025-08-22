import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Develop Countermeasures", layout="wide")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


#INITIALIZE
if "activity6b" not in st.session_state:
    st.session_state.activity6b = False

if "activity6a" not in st.session_state:
    st.session_state.activity6a = False

#START PAGE
st.markdown("### TASK 5: DEVELOP COUNTERMEASURES")

st.markdown("Fill out the matrix below. *Tip: Add up the values in every row!*")
#HEADER ROW
col1r1, col2r1, col3r1, col4r1, col5r1, col6r1, col7r1 = st.columns([8,2,2,2,2,2,1], vertical_alignment="bottom")
with col1r1:
    st.write("**Countermeasure**")
with col2r1:
    st.write("**Current Safety Risk**")
with col3r1:
    st.write("**ROI**")
with col4r1:
    st.write("**Easy Implementation**")
with col5r1:
    st.write("**Effectiveness**")
with col6r1:
    st.write("**Quick Implementation**")
with col7r1: 
    st.write("**Total**")

#TABLE
col1r2, col2r2, col3r2, col4r2, col5r2, col6r2, col7r2 = st.columns([8,2,2,2,2,2,1], vertical_alignment="center")
with col1r2:
    st.write("Create and implement a preventative maintenance checklist for Tube Bender")
    st.write("Calibrate and replace bending tools (clamps and gauge) on a fixed schedule")
    st.write("Assign owndership of maintenance tasks to a specific technician")
    st.write("Add visual controls to track PM status (e.g. magnetic tags or board indicators)")
    st.write("Add Tube Bender #2 to SAP PM schedule with automated reminders")
with col2r2:
    st.markdown("2")
    st.markdown("1")
    st.text_input("", value=None, label_visibility="collapsed", key=1)
    st.markdown("0")
    st.markdown("1")
with col3r2:
    st.markdown("3")
    st.markdown("3")
    st.markdown("2")
    st.markdown("2")
    st.markdown("2")
with col4r2:
    st.text_input("", value=None, label_visibility="collapsed", key=3)
    st.markdown("2")
    st.markdown("3")
    st.markdown("3")
    st.markdown("2")
with col5r2:
    st.markdown("3")
    st.markdown("3")
    st.markdown("2")
    st.markdown("2")
    st.text_input("", value=None, label_visibility="collapsed", key=4)
with col6r2:
    st.markdown("3")
    st.markdown("2")
    st.markdown("3")
    st.text_input("", value=None, label_visibility="collapsed", key=5)
    st.markdown("1")
with col7r2: 
    st.markdown("14")
    st.text_input("", value=None, label_visibility="collapsed", key=6)
    st.markdown("11")
    st.markdown("10")
    st.markdown("9")


# Button - submit code
if st.button("Submit Answers", type="primary"):
    if True:
        st.session_state.activity6a = True
        st.success("You got it!")
    else:
        st.error("One or more of your numbers are incorrect. Please try again.")

# Follow up question
if st.session_state.activity6a:
    st.markdown("---")
    st.write("One more thing before we move to the next task. Please answer the question below.")
    #st.write("What information should NOT be included in the A3 header?")

    answerP6Q1 = "Development is for brainstorming possible solutions and implementation chooses one solution and plans it out"
    pg6Q1 = st.radio(
        "What is the difference between 'Develop Countermeasures' and 'Implement Countermeasures'?",
        ["Development is for sketching and implementation is the technical drawing",
         "Development is for brainstorming possible solutions and implementation chooses one solution and plans it out",
         "Development is creating detailed action plans and implementation is the finished product",
         "All of these are correct"],
        index=None, key="pg6Q1"
    )

    if pg6Q1 == answerP6Q1:
        st.success("You are correct! Click the button below to move to the next task.")
        if st.button("PROCEED TO NEXT TASK", type="primary", key="pg6B1"):
            st.session_state.activity6b = True
    elif pg6Q1 == None:
        st.markdown("Please select an answer")
    else:
        st.error("Incorrect. Please try again.")

if st.session_state.activity6b:
    message = ''':warning: STOP! :warning: *There's something important hidden in this room... To keep it hidden from enemy spies, we can only give you a clue*.  
    Use this clue to find the secret intel **essential** for the next task and the code needed to continue.'''
    st.warning(message)
    p5code1 = '''
    TOP SECRET: Classified intel isn't visible to the untrained eye. Locate the secret where two walls meet.
    '''
    st.code(p5code1, language=None)

    pg6Code = st.text_input("Enter the code on the back of the hint and hit enter.", value=None)

    if pg6Code == "08672":
        st.success("*Good work agents. We knew you would find it. Make sure to write down or keep the information you found!*")
        if st.button("PROCEED TO NEXT TASK", type="primary", key="pg6B2"):
            st.switch_page("pg7.py")
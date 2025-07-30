import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Root Cause Analysis", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

#initialize session states
if "activity5a" not in st.session_state:
        st.session_state.activity5a = False

if "activity5b" not in st.session_state:
        st.session_state.activity5b = False

if "activity5c" not in st.session_state:
        st.session_state.activity5c = False


#begin page
st.markdown("### TASK 5: ROOT CAUSE ANALYSIS")

#FISHBONE
st.markdown("Given the statement bank and the diagram below, enter the statement number into the corresponding box.")
st.markdown("##### Fishbone Diagram")

if st.session_state.activity5b:
    st.image("pg5picSOLUTION.png")
else:
    st.image("pg5pic.png")

st.markdown("##### Statement Bank")
p5code1 = '''
Statement 1: Setup steps not followed consistently
Statement 2: Inconsistent tube positioning
Statement 3: Poor lighting around bender station
Statement 4: Calibration tool worn out
Statement 5: Lack of clear ownership
Statement 6: Scratches or dents affect positioning
'''
st.code(p5code1, language=None)


col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    man = st.number_input("Man", value=None, step=0, key=0)    
with col2:
    method = st.number_input("Method", value=None, step=0, key=1)
with col3:
    material = st.number_input("Material", value=None, step=0, key=2)
with col4:
    machine = st.number_input("Machine", value=None, step=0, key=3)
with col5:
    environment = st.number_input("Environment", value=None, step=0, key=4)
with col6:
    management = st.number_input("Management", value=None, step=0, key=5)


if "activity5a" not in st.session_state:
    st.session_state.activity5a = False
# Button - submit code
if st.button("Submit Answers", key="5a", type="primary"):

    if man==2 and method==1 and material==4 and machine==6 and environment==3 and management==5:
        st.session_state.activity5a = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

#DIRECT CAUSE
if st.session_state.activity5a:
        
    st.markdown("---")  # Horizontal line
    st.markdown("### Direct Cause")
    st.markdown(":star: Direct cause, is the *MAIN* cause of variation in a process or product that is most responsible for the problem being investigated. It is the dominant cause among many potential contributors, and targeting it yields the maximum impact on solving the issue.")
    #Ishikawa option (using all 6 causes, select "direct" or "indirect")
    st.markdown("*ISHIKAWA MATRIX*")
    answerP5Q2 = st.selectbox("Given the problem statement in the fishbone diagram above, identify the most direct cause.",
                 ["Setup steps not followed consistently",
                  "Inconsistent tube positioning",
                  "Poor lighting around bender station",
                  "Calibration tool worn out",
                  "Lack of clear ownership",
                  "Scratches or dents affect positioning"], index=None
                )
    
    # Button - submit code
    if st.button("Submit Answers", key="5b", type="primary"):

        if answerP5Q2 == "Calibration tool worn out":
            st.session_state.activity5b = True
            st.success("You got it!")
        else:
            st.error("Your answer is incorrect. Please try again.")

#5 WHYS
if st.session_state.activity5b:

    st.markdown("---")  # Horizontal line

    st.markdown("### 5 Whys")
    st.markdown(":star: Remember: Identifying a single root cause is ideal for clarity and focus, but in some cases, multiple root causes may exist and need to be addressed to fully solve the problem.")

    st.markdown("Based on the problem statement, put the 5 Why statements in the correct order.")
    st.markdown("##### Problem Statement")

    p5code2 = '''
    In the Tube Bender #2 station, parts are being rejected due to
    bend angles that exceed the specification tolerance (±2°).

    Direct Cause: Calibration tool worn out
    '''
    st.code(p5code2, language=None)

    st.markdown("Order these statements in the correct order.")


    why3 = st.selectbox("Because they haven't been inspected or replaced in a long time", [1,2,3,4,5], index=None)
    why2 = st.selectbox("Because the clamps are damaged and the calibration tool is worn out", [1,2,3,4,5], index=None)
    why5 = st.selectbox("Because there is no preventative maintenance plan for Tube Bender #2, including calibration tools and clamps", [1,2,3,4,5], index=None)
    why1 = st.selectbox("Because the bending equipment is not applying the correct force or angle", [1,2,3,4,5], index=None)
    why4 = st.selectbox("Because there's no scheduled preventative maintenance for this equipment", [1,2,3,4,5], index=None)


    # Button - submit code
    if st.button("Submit Answers", key="5c", type="primary"):

        if why1==1 and why2==2 and why3==3 and why4==4 and why5==5:
            st.session_state.activity5c = True
            st.success("You got it!")
        else:
            st.error("One or more of your answer is incorrect. Please try again.")

if st.session_state.activity5c:
    st.markdown("---")
    st.write(":exclamation: A root cause and a symptom are **NOT** the same! A sympton is the visible effect, and the root cause is the underlying reason for the problem.")
    st.image("pg5pic2.png")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg6.py")
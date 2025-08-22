import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Root Cause Analysis", layout="wide")
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
st.markdown("### TASK 4: ROOT CAUSE ANALYSIS")

#FISHBONE
col1, col2, col3 = st.columns([0.3, 0.5, 0.3])
with col2:
    st.markdown("Given the statement bank and the diagram below, enter the statement number into the corresponding box.")
    st.markdown("##### Fishbone Diagram")

    if st.session_state.activity5b:
        st.image("pg5picSOLUTION.png", width=900)
    else:
        st.image("pg5pic.png", width=900)

    st.markdown("##### Statement Bank")
    p5code1 = '''
    Statement 1: No standard procedure for angle setup
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

    if man==2 and method==1 and material==6 and machine==4 and environment==3 and management==5:
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
    left, center, right = st.columns([0.05, 0.85, 0.15], vertical_alignment="top")
    with center:
        st.markdown("")
        st.image("pg5pic2.png", use_container_width=True)
    with right:
        st.markdown("**Evaluation of Root Cause**")
        #st.markdown("")
        ishi1 = st.segmented_control("Man", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=6, label_visibility="hidden")
        ishi2 = st.segmented_control("Method", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=7, label_visibility="hidden")
        ishi3 = st.segmented_control("Material", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=8, label_visibility="hidden")
        ishi4 = st.segmented_control("Machine", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=9, label_visibility="hidden")
        ishi5 = st.segmented_control("Environment", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=10, label_visibility="hidden")
        ishi6 = st.segmented_control("Management", ["Direct", "Indirect"], selection_mode="single",
                                     default=None, key=11, label_visibility="hidden")
        st.markdown(" ")

    with center:
        # Button - submit code
        if st.button("Submit Answers", key="5b", type="primary"):
            bool1 = False
            bool2 = False
            bool3 = False
            bool4 = False
            bool5 = False
            bool6 = False
            

            if ishi1 == "Indirect":
                bool1 = True
            else:
                st.error("Category: Man is incorrect.")
            if ishi2 == "Indirect":
                bool2 = True
            else:
                st.error("Category: Method is incorrect.")
            if ishi3 == "Indirect":
                bool3 = True
            else:
                st.error("Category: Material is incorrect.")
            if ishi4 == "Direct":
                bool4 = True
            else:
                st.error("Category: Machine is incorrect.")
            if ishi5 == "Indirect":
                bool5 = True
            else:
                st.error("Category: Environment is incorrect.")
            if ishi6 == "Indirect":
                bool6 = True
            else:
                st.error("Category: Management is incorrect.")
                

            if bool1 and bool2 and bool3 and bool4 and bool5 and bool6:
                st.session_state.activity5b = True
                st.success("You got it!")
        

#5 WHYS
if st.session_state.activity5b:

    st.markdown("---")  # Horizontal line

    col4, col5, col6 = st.columns([0.3, 0.6, 0.3])
    with col5:
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


        why3 = st.selectbox("Because they haven't been inspected or replaced in a long time", [1,2,3,4,5], index=None, width=700)
        why2 = st.selectbox("Because the clamps are damaged and the calibration tool is worn out", [1,2,3,4,5], index=None, width=700)
        why5 = st.selectbox("Because there is no preventative maintenance plan for Tube Bender #2, including calibration tools and clamps", [1,2,3,4,5], index=None, width=700)
        why1 = st.selectbox("Because the bending equipment is not applying the correct force or angle", [1,2,3,4,5], index=None, width=700)
        why4 = st.selectbox("Because there's no scheduled preventative maintenance for this equipment", [1,2,3,4,5], index=None, width=700)


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
        st.image("pg5pic3.png", width=700)
        if st.button("PROCEED TO NEXT TASK", type="primary"):
                st.switch_page("pg6.py")
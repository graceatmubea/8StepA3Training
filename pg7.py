import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Implement Countermeasures", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")

if "activity7a" not in st.session_state:
    st.session_state.activity7a = False
if "activity7b" not in st.session_state:
    st.session_state.activity7b = False

st.markdown("### TASK 7: IMPLEMENT COUNTERMEASURES")


pg7List = ["address gaps through leader coaching", "ownership execution weekly", "To review", "during FMDS meetings and"]

st.markdown("Use your secret intel and arrange these words into the proper action structure to unlock the next activity. ")
pg7Q1 = st.multiselect("Put these sections in the correct order to write the missing countermeasure.", pg7List, placeholder="")

if st.button("Submit Answers", key="7a", type="primary"):
    if pg7Q1 == ["To review","ownership execution weekly","during FMDS meetings and","address gaps through leader coaching"]:
        st.session_state.activity7a = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")


if st.session_state.activity7a:
    st.divider()
    st.image("pg7pic.png")
    st.markdown("Using the image above, select the countermeasures that were completed within the proper time frame.")
    cm1 = st.checkbox("CM 1")
    cm2 = st.checkbox("CM 2")
    cm3 = st.checkbox("CM 3")
    cm4 = st.checkbox("CM 4")
    cm5 = st.checkbox("CM 5")
    cm6 = st.checkbox("CM 6")

    # Button - submit code
    if st.button("Submit Answers", key="7b", type="primary"):
        if cm6 and cm5 and not cm1 and not cm2 and not cm3 and not cm4:
            st.session_state.activity7b = True
            st.success("You got it!")
        else:
            st.error("Your answer is incorrect. Please try again.")

if st.session_state.activity7b:
    st.markdown("---")
    st.write(":exclamation: Tasks should be completed within **3 months** to be considered 'completed on time'.")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg8.py")
import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Target Setting", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 4: TARGET SETTING")
st.markdown("Fill-in-the-blank activity")

if "activity4" not in st.session_state:
    st.session_state.activity4 = False
# Button - submit code
if st.button("Submit Answers", type="primary"):

    if True:
        st.session_state.activity4 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

# Follow up question
if st.session_state.activity4:
    st.markdown("---")
    st.write("Please note: *insert statement about Target Setting*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg5.py")
import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Implement Countermeasures", layout="centered")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 7: IMPLEMENT COUNTERMEASURES")
st.image("pg7pic.png")

st.markdown("Using the image above, select the countermeasures that were completed within the proper time frame.")
cm1 = st.checkbox("CM 1")
cm2 = st.checkbox("CM 2")
cm3 = st.checkbox("CM 3")
cm4 = st.checkbox("CM 4")
cm5 = st.checkbox("CM 5")
cm6 = st.checkbox("CM 6")

if "activity7" not in st.session_state:
        st.session_state.activity7 = False
    # Button - submit code
if st.button("Submit Answers", key="7", type="primary"):
    if True:
        st.session_state.activity7 = True
        st.success("You got it!")
    else:
        st.error("Your answer is incorrect. Please try again.")

if st.session_state.activity7:
    st.markdown("---")
    st.write("Please note: *insert statement about due date*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg8.py")
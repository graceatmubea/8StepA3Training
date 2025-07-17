import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Target Setting", layout="wide")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 4: TARGET SETTING")
st.markdown("Fill-in-the-blank activity")

p4code1 = '''
Reduce bend angle ______ from 58% to 10% of Bender #2 _____,
at the Bending Operation by June 30, 2025. This ____________
is expected to _______ total scrap in the tube forming line from
4.5% to 3.9%
'''
st.code(p4code1, language=None)

col1, col2, col3, col4, col5 = st.columns([3, 2, 3, 2, 5], vertical_alignment="top")

with col1:
    st.markdown("**Reduce bend angle**")
    st.text_input("improvement", key="b3", label_visibility="collapsed")

with col2:
    answer1 = st.text_input("defects", key="b1", label_visibility="collapsed")
    st.markdown("**is expected to**")

with col3:
    st.markdown("**from 58% to 10% of Bender #2**")
    st.text_input("reduce", key="b4", label_visibility="collapsed")

with col4:
    answer2 = st.text_input("scrap", key="b2", label_visibility="collapsed")
    st.markdown("**total scrap in the**")

with col5:
    st.markdown("**at the Bending Operation by June 30, 2025. This**")
    st.markdown("**tube forming line from 4.5% to 3.9%.**")


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
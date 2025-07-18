import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title="Target Setting", layout="wide")
if st.button("Return to Home Page"):
    st.switch_page("pgTitle.py")


st.markdown("### TASK 4: TARGET SETTING")
st.markdown("#### Fill-in-the-blank activity")
st.markdown("Fill in the blanks below to form the complete target goal statment.")

st.divider()

p4code1 = '''
Reduce bend angle ______ from 58% to 10% of Bender #2 _____,
at the Bending Operation by June 30, 2025. This ____________
is expected to _______ total scrap in the tube forming line from
4.5% to 3.9%
'''
#st.code(p4code1, language=None)

pg4List = ["defects","improvement","reduce","scrap"]

#line1
col1, col2, col3, col4, col5 = st.columns([2, 3, 3, 3, 7], vertical_alignment="top")

with col1:
    st.markdown("**Reduce bend angle**")

with col2:
    answer1 = st.selectbox("defects", options=pg4List, index=None, key="b1", label_visibility="collapsed")

with col3:
    st.markdown("**from 58% to 10% of Bender #2**")

with col4:
    answer2 = st.selectbox("scrap", options=pg4List, index=None, key="b2", label_visibility="collapsed")

with col5:
    st.markdown("**at the Bending Operation by June 30, 2025.**")

#line2
col1r2, col2r2, col3r2, col4r2, col5r2, col6r2 = st.columns([1, 4, 2, 4, 2, 8], vertical_alignment="top")

with col1r2:
    st.markdown("**This**")
with col2r2:
    st.selectbox("improvement", options=pg4List, index=None, key="b3", label_visibility="collapsed")

with col3r2:
    st.markdown("**is expected to**")

with col4r2:
    st.selectbox("reduce", options=pg4List, index=None, key="b4", label_visibility="collapsed")

with col5r2:
    st.markdown("**total scrap in the**")

with col6r2:
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
    st.write(":dart: *Formulate your goals clearly and quantifiably.*")
    if st.button("PROCEED TO NEXT TASK", type="primary"):
            st.switch_page("pg5.py")
import streamlit as st


# Set page title
st.set_page_config(page_title="Activity 1", layout="centered")

if st.button(label="Return to Home Page", key=None, help=None, type="secondary", icon=None,
             disabled=False, use_container_width=False):
    st.switch_page("pgTitle.py")

# Title
st.markdown("## Enter the secret code below:")

left, middle, right = st.columns([3, 3, 3], vertical_alignment="top")

with left:
    code1 = st.number_input("First number", min_value=0)
with middle:
    code2 = st.number_input("Second number", min_value=0)
with right:
    code3 = st.number_input("Third number", min_value=0)
    
if st.button("Submit Answers"):
    if (code1 == 1 and code2 == 2 and code3 == 3):
        st.markdown("You got it!")
        st.markdown("---")  # Horizontal line
    else:
        st.markdown("One or more of your numbers are incorrect. Please try again.")
        st.markdown("---")  # Horizontal line



import streamlit as st


pg = st.navigation([
    st.Page("pgTitle.py", title="Title", icon=":material/favorite:"),
    st.Page("pg1.py", title="1. header"),
    st.Page("pg2.py", title="2. current condition"),
    st.Page("pg3.py", title="3. breakdown"),
    st.Page("pg4.py", title="4. target setting"),
    st.Page("pg5.py", title="5. root cause analysis"),
    st.Page("pg6.py", title="6. develop countermeasures"),
    st.Page("pg7.py", title="7. implement countermeasures"),
    st.Page("pg8.py", title="8. monitor results"),
    st.Page("pg9.py", title="9. standardize & share"),
    st.Page("pgEnd.py", title="Final", icon=":material/favorite:"),
], position='hidden')
pg.run()
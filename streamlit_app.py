import streamlit as st


pg = st.navigation([
    st.Page("pgTitle.py", title="Title", icon=":material/favorite:"),
    st.Page("pg1.py", title="Batch", icon="🔥"),
    st.Page("pg2.py", title="Single", icon="🔥"),
    st.Page("pg3.py", title="Single", icon="🔥")
], position='hidden')
pg.run()
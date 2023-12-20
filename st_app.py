import streamlit as st
st.title("expense tracker")
submitted=st.button("submit")
if submitted:
    st.write("submitted successfully")
    st.success("done")
    st.balloons()
import streamlit as st

st.title("Authentication")

if not st.experimental_user.is_logged_in:
    if st.button("Login"):
        st.login("google")

if st.experimental_user.is_logged_in:
    st.write(f"Logged in as: {st.experimental_user.email}")
    if st.button("Logout"):
        st.logout()

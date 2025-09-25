import streamlit as st
from data.base import about_diabetes

def app():
    st.markdown(about_diabetes)

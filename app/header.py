import streamlit as st
from data.base import head, st_style, footer

def app():
    st.markdown(st_style, unsafe_allow_html=True)
    st.markdown(head, unsafe_allow_html=True)

    st.title("AI-ML Approach for Early Detection of Diabetes Risk")
    st.markdown("""
    **Mini Project (2025–26)**  
    Developed by: *NSS TEAM*  
    Institution: *SJCIT*
    """)

    st.markdown(footer, unsafe_allow_html=True)

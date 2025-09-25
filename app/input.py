import streamlit as st
import pandas as pd

def app():
    st.sidebar.header("📝 Enter Patient Information")

    pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.sidebar.number_input("Glucose", min_value=0, max_value=200, value=100)
    insulin = st.sidebar.number_input("Insulin", min_value=0, max_value=900, value=80)
    bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=30)

    input_dict = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "Insulin": insulin,
        "BMI": bmi,
        "Age": age
    }

    input_df = pd.DataFrame([input_dict])
    return input_df

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load('models/model.pkl')
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# Prediction function
def app(input_data):
    st.header("🔍 Diabetes Risk Prediction")

    expected_columns = ['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']

    if not isinstance(input_data, pd.DataFrame):
        st.error("Input must be a pandas DataFrame.")
        st.stop()

    if not all(col in input_data.columns for col in expected_columns):
        st.error(f"Missing required input columns: {expected_columns}")
        st.stop()

    try:
        # Make prediction
        prediction_proba = model.predict_proba(input_data)[0][1]
        prediction_class = model.predict(input_data)[0]

        # Display result
        st.subheader(f"🎯 Diabetes Risk Probability: {prediction_proba:.2f}")
        if prediction_class == 1:
            st.error("⚠️ High risk of diabetes detected.")
        else:
            st.success("✅ Low risk of diabetes detected.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

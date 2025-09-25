import streamlit as st
from loader import page_icon  # Your icon file (PIL Image object or similar)
from app.header import app as header_app
from app.input import app as input_app
from app.predict import app as predict_app
from app.explainer import app as explainer_app
from app.performance import app as performance_app
from app.perm_importance import app as perm_importance_app
from app.about import app as about_app

# Set Streamlit page config
st.set_page_config(
    page_title="AI-ML Approach for Early Detection of Diabetes Risk",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Render Header Section
header_app()

# Render Input Section and get user inputs as DataFrame
input_data = input_app()

# Run Prediction Section with user input
predict_app(input_data)

# Render Explanation Section (e.g., SHAP) using input data
explainer_app(input_data)

# Show Model Performance Metrics
performance_app()

# Show Permutation Importance
perm_importance_app()

# Show About Section
about_app()

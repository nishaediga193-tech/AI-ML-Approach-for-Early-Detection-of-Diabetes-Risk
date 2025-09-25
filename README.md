# AI-ML-Approach-for-Early-Detection-of-Diabetes-Risk
Mini Project | AI & ML Approach for Early Detection of Diabetes Risk (2025–26)

---

## 📖 Abstract
Diabetes mellitus is one of the most common and serious chronic diseases affecting people worldwide.  
It occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.  
Early prediction of diabetes is important to avoid severe complications.  

This mini project implements an **AI & ML–based approach** to predict the risk of diabetes using the **PIMA Indian Diabetes Dataset**.  
The system applies machine learning algorithms to identify patterns from health parameters like glucose level, BMI, insulin, age, and pregnancies.  
The model is deployed as a **Streamlit web app** that allows users to enter their health details and check their risk level in real-time.

---

## 🎯 Objectives
1. To study and analyze the application of **Artificial Intelligence and Machine Learning** in healthcare.  
2. To predict diabetes at an early stage using medical datasets.  
3. To implement and evaluate different ML algorithms for performance.  
4. To deploy the trained model in a **user-friendly web application**.  
5. To provide explanations of predictions using SHAP values and permutation importance.

---

## ⚙️ Methodology
The project methodology is divided into the following phases:

1. **Data Collection**  
   - Dataset used: *PIMA Indian Diabetes Dataset*.  
   - Includes parameters such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Age, DiabetesPedigreeFunction, and Outcome.

2. **Data Preprocessing**  
   - Handling missing or zero values.  
   - Normalization of continuous variables.  
   - Feature selection for improving model performance.

3. **Model Training**  
   - Applied algorithms such as Random Forest Classifier.  
   - Hyperparameter tuning using **Optuna** optimizer.  
   - Model evaluated using metrics like Accuracy, Precision, Recall, F1-score, and ROC AUC.

4. **Model Deployment**  
   - Trained model stored as `.pkl`.  
   - Deployed on a **Streamlit web application**.  
   - Prediction results explained with SHAP plots and permutation importance.

---

## 📊 Dataset
- **Source:** National Institute of Diabetes and Digestive and Kidney Diseases  
- **Instances (rows):** 768  
- **Attributes (columns):** 9  
- **Target:** Outcome (0 = Non-diabetic, 1 = Diabetic)  

Features include: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome.

---

## 🚀 Features
- Diabetes risk prediction using ML algorithms.  
- Web-based interface built with **Streamlit**.  
- Interactive input for health data.  
- Prediction probability displayed.  
- **SHAP visualizations** for explainability.  
- Performance metrics visualization.  

---

## 🖥️ Installation

### Requirements
- Python 3.10+  
- pip  

### Steps
```bash
# Clone the repository
git clone https://github.com/nishaediga193-tech/AI-ML-Approach-for-Early-Detection-of-Diabetes-Risk.git
cd AI-ML-Approach-for-Early-Detection-of-Diabetes-Risk

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run main.py
```bash
AI-ML-Approach-for-Early-Detection-of-Diabetes-Risk/
├── README.md                 # Documentation
├── main.py                   # Streamlit app
├── loader.py                 # Data loading and preprocessing
├── training.py               # ML model training
├── requirements.txt          # Dependencies
├── LICENSE                   # MIT License
├── datasets/
│   └── diabetes.csv          # Dataset
├── models/
│   └── model.pkl             # Trained model
├── app/
│   ├── predict.py            # Prediction logic
│   ├── explainer.py          # SHAP explanations
│   ├── performance.py        # Performance visualization
│   ├── input.py              # User input form
│   └── about.py              # Project info
Model Performance

Accuracy: ~78%

Precision: ~63%

Recall: ~94%

F1 Score: ~76%

ROC AUC: ~83%

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

👩‍💻 Team Members

Nisha N (USN: 1SJ23CI040)

K G Shrujana (USN: 1SJ23CI027)

Sahana T N (USN: 1SJ23CI050)

Guide: Prof. MRS ASHIKA .S
Institution: SJCIT, VTU

🙏 Acknowledgement

We sincerely thank our guide, department, and institution for their constant support and encouragement throughout the mini project.
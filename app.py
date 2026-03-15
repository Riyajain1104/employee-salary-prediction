import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

st.set_page_config(layout="wide")
# Load trained model
model = joblib.load("best_model.pkl")

# Page configuration
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼")

# Title
st.title("💼 Employee Salary Prediction App")

st.markdown(
"""
This app predicts whether an employee earns **more than 50K or less than 50K**
based on age, educational-num, occupation and work hours.
"""
)

# Sidebar
st.sidebar.header("Enter Employee Details")
age = st.sidebar.slider("Age",18,65,30)
education = st.sidebar.selectbox(
"Education Level",
["Preschool","1st-4th","5th-6th","7th-8th","9th","10th","11th","12th",
"HS-grad","Some-college","Assoc-voc","Assoc-acdm",
"Bachelors","Masters","Prof-school","Doctorate"]
)

occupation = st.sidebar.selectbox(
"Occupation",
["Tech-support","Craft-repair","Other-service","Sales",
"Exec-managerial","Prof-specialty","Handlers-cleaners",
"Machine-op-inspct","Adm-clerical","Farming-fishing",
"Transport-moving","Priv-house-serv","Protective-serv","Armed-Forces"]
)

hours_per_week = st.sidebar.slider("Hours per Week",1,80,40)

# -----------------------------
# Education Mapping
# -----------------------------
education_map = {
"Preschool":1,
"1st-4th":2,
"5th-6th":3,
"7th-8th":4,
"9th":5,
"10th":6,
"11th":7,
"12th":8,
"HS-grad":9,
"Some-college":10,
"Assoc-voc":11,
"Assoc-acdm":12,
"Bachelors":13,
"Masters":14,
"Prof-school":15,
"Doctorate":16
}

education_num = education_map[education]

# -----------------------------
# Occupation Mapping
# -----------------------------
occupation_map = {
"Tech-support":0,
"Craft-repair":1,
"Other-service":2,
"Sales":3,
"Exec-managerial":4,
"Prof-specialty":5,
"Handlers-cleaners":6,
"Machine-op-inspct":7,
"Adm-clerical":8,
"Farming-fishing":9,
"Transport-moving":10,
"Priv-house-serv":11,
"Protective-serv":12,
"Armed-Forces":13
}

occupation_num = occupation_map[occupation]

# -----------------------------
# Input DataFrame
# -----------------------------
input_df = pd.DataFrame({
"age":[age],
"educational-num":[education_num],
"occupation":[occupation_num],
"hours-per-week":[hours_per_week]
})

st.subheader("Input Data")
st.write(input_df)




# -----------------------
# Prediction
# -----------------------

if st.button("Predict Salary"):

    prediction = model.predict(input_df)

    # Get probability
    probability = model.predict_proba(input_df)

    confidence = round(max(probability[0]) * 100, 2)

    result = ">50K" if prediction[0] == 1 else "<=50K"

    st.subheader("🔎 Prediction Result")

    if prediction[0] == 1:
        st.success("💰 The employee is likely to earn **more than 50K**.")
    else:
        st.warning("📉 The employee is likely to earn **50K or less**.")

    st.info(f"📊 Confidence: **{confidence}%**")

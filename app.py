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
based on age, education, occupation, work hours and experience.
"""
)

# Sidebar
st.sidebar.header("Enter Employee Details")


age = st.sidebar.slider("Age", 18, 65, 30)

education = st.sidebar.selectbox(
    "Education Level",
    ["Bachelors","Masters","PhD","HS-grad","Assoc","Some-college"]
)

occupation = st.sidebar.selectbox(
    "Occupation",
    ["Tech-support","Craft-repair","Other-service","Sales",
     "Exec-managerial","Prof-specialty","Handlers-cleaners",
     "Machine-op-inspct","Adm-clerical","Farming-fishing",
     "Transport-moving","Priv-house-serv","Protective-serv",
     "Armed-Forces"]
)

hours_per_week = st.sidebar.slider("Hours per Week", 1, 80, 40)

experience = st.sidebar.slider("Years of Experience", 0, 40, 5)

# -----------------------
# Convert strings to numbers
# -----------------------

education_map = {
    "HS-grad":0,
    "Some-college":1,
    "Assoc":2,
    "Bachelors":3,
    "Masters":4,
    "PhD":5
}

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

education = education_map[education]
occupation = occupation_map[occupation]

# Input dataframe
input_df = pd.DataFrame({
    'age':[age],
    'education':[education],
    'occupation':[occupation],
    'hours-per-week':[hours_per_week],
    'experience':[experience]
})

st.subheader("📊 Input Data")
st.write(input_df)

# -----------------------
# Scaling
# -----------------------


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

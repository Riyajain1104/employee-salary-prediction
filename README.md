# 💼 Employee Salary Prediction App

This project is a **Machine Learning web application** that predicts whether an employee earns **more than 50K or less than 50K** based on certain features such as age, education level, occupation, and working hours.

The application is built using **Python, Scikit-Learn, and Streamlit**, and is deployed online using **Streamlit Cloud**.

---

## 🚀 Live Application

You can access the live app here:

🔗 https://employee-salary-predictor-riya.streamlit.app

---

## 📊 Project Overview

The goal of this project is to build a **classification model** that predicts employee salary category based on input features.

The dataset used is the **Adult Income Dataset**, which is commonly used for machine learning classification tasks.

The model predicts whether a person's income is:

* **>50K (More than 50,000)**
* **≤50K (50,000 or less)**

---

## 🧠 Machine Learning Models Used

The following models were trained and compared:

* Logistic Regression
* Random Forest Classifier
* Gradient Boosting Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)

The best performing model was saved and used for the web application.

---

## 📥 Input Features

The app uses the following features for prediction:

* Age
* Education Level
* Occupation
* Hours per Week

These inputs are provided through an interactive **Streamlit user interface**.

---

## 📈 Output

The application displays:

* Predicted Salary Category
* Model Confidence Score

Example output:

```
Prediction Result:
The employee is likely to earn 50K or less.

Confidence: 75%
```

---

## 🛠️ Technologies Used

* Python
* Scikit-Learn
* Pandas
* NumPy
* Streamlit
* Joblib
* GitHub
* Streamlit Cloud

---

## 📂 Project Structure

```
employee-salary-prediction
│
├── app.py              # Streamlit application
├── best_model.pkl      # Trained ML model
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ▶️ How to Run the Project Locally

1. Clone the repository

```
git clone https://github.com/your-username/employee-salary-prediction.git
```

2. Navigate to the project folder

```
cd employee-salary-prediction
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the Streamlit app

```
streamlit run app.py
```

---

## 📚 Future Improvements

* Add more features like marital status and capital gain
* Improve model performance
* Add data visualization and feature importance graphs

---

## 👩‍💻 Author

**Riya Jain**

Machine Learning Project – Employee Salary Prediction

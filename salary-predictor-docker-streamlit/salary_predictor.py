import joblib
import streamlit as st

salary_prediction_model = joblib.load("salary_predict_model.model")

def salary_predict(exp):
    salary_predict = salary_prediction_model.predict([[ int(exp) ]] )
    st.write(" Your Salary would be : ", salary_predict[0])

st.title("Welcome to Salary Predictor")

exp = st.slider("Select your experience (in years):", 0.0, 20.0, step=0.1) 

if exp:
    st.write(f"Hey I know your experience is {exp} years, plz wait I m helping in predicting your future salary")
    salary_predict(exp)



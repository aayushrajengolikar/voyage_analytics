import streamlit as st
import requests

st.header("Gender Prediction")

API_URL = "https://voyage-analytics-xdw8.onrender.com/predict/gender"

code = st.number_input("Code", value=1)

company = st.text_input("Company", "Google")

name = st.text_input("Name", "Aayush")

age = st.number_input("Age", value=22)

if st.button("Predict Gender"):

        data = {
            "code": code,
            "company": company,
            "name": name,
            "age": age
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            st.success("Prediction Successful")
            st.write(response.json())
        else:
            st.error(response.text)
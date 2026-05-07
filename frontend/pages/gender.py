import streamlit as st
import requests

st.title("👤 Gender Prediction")

code = st.number_input("Code", value=1148)
company = st.text_input("Company", "Umbrella LTDA")
name = st.text_input("Name", "Laurel Rodriguez")
age = st.number_input("Age", value=45)

if st.button("Predict Gender"):
    response = requests.post(
        "http://127.0.0.1:8000/predict/gender",
        json={
            "code": int(code),
            "company": company,
            "name": name,
            "age": int(age)
        }
    )

    st.write(response.json())
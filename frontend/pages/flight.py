import streamlit as st
import requests

st.header("Flight Prediction")

API_URL = "https://voyage-analytics-xdw8.onrender.com/predict/flight"

travelCode = st.number_input("Travel Code", value=1)
userCode = st.number_input("User Code", value=100)

from_city = st.text_input("From", "Hyderabad")
to_city = st.text_input("To", "Delhi")

flightType = st.selectbox(
        "Flight Type",
        ["Economic", "Business"]
    )

time = st.number_input("Flight Time", value=2.5)
distance = st.number_input("Distance", value=1200.0)

agency = st.text_input("Agency", "MakeMyTrip")

date = st.text_input("Date (YYYY-MM-DD)", "2026-05-07")

if st.button("Predict Flight"):

        data = {
            "travelCode": travelCode,
            "userCode": userCode,
            "from_": from_city,
            "to": to_city,
            "flightType": flightType,
            "time": time,
            "distance": distance,
            "agency": agency,
            "date": date
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            st.success("Prediction Successful")
            st.write(response.json())
        else:
            st.error(response.text)

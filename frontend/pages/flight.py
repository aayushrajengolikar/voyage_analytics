import streamlit as st
import requests

st.title("✈️ Flight Price Prediction")

travelCode = st.number_input("Travel Code", value=55700)
userCode = st.number_input("User Code", value=543)
from_ = st.text_input("From", "Recife (PE)")
to = st.text_input("To", "Campo Grande (MS)")
flightType = st.selectbox("Flight Type", ["firstClass", "economic", "premium"])
time = st.number_input("Time", value=1.39)
distance = st.number_input("Distance", value=535.40)
agency = st.text_input("Agency", "Rainbow")
date = st.date_input("Date")

if st.button("Predict Flight Price"):
    response = requests.post(
        "http://127.0.0.1:8000/predict/flight",
        json={
            "travelCode": int(travelCode),
            "userCode": int(userCode),
            "from_": from_,
            "to": to,
            "flightType": flightType,
            "time": float(time),
            "distance": float(distance),
            "agency": agency,
            "date": str(date)   # IMPORTANT FIX
        }
    )

    st.write(response.json())
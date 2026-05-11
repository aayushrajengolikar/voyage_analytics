import streamlit as st
import requests

st.header("Customer Churn Prediction")

API_URL = "https://voyage-analytics-xdw8.onrender.com/predict/churn"

state = st.text_input("State", "OH")
account_length = st.number_input("Account Length", value=120)
area_code = st.number_input("Area Code", value=415)

international_plan = st.selectbox(
        "International Plan",
        ["Yes", "No"]
    )

voice_mail_plan = st.selectbox(
        "Voice Mail Plan",
        ["Yes", "No"]
    )

number_vmail_messages = st.number_input(
        "Number of Voicemail Messages",
        value=25
    )

total_day_minutes = st.number_input("Total Day Minutes", value=200.5)
total_day_calls = st.number_input("Total Day Calls", value=110)
total_day_charge = st.number_input("Total Day Charge", value=34.08)

total_eve_minutes = st.number_input("Total Evening Minutes", value=180.2)
total_eve_calls = st.number_input("Total Evening Calls", value=95)
total_eve_charge = st.number_input("Total Evening Charge", value=15.32)

total_night_minutes = st.number_input("Total Night Minutes", value=220.4)
total_night_calls = st.number_input("Total Night Calls", value=100)
total_night_charge = st.number_input("Total Night Charge", value=9.92)

total_intl_minutes = st.number_input("Total International Minutes", value=10.5)
total_intl_calls = st.number_input("Total International Calls", value=3)
total_intl_charge = st.number_input("Total International Charge", value=2.84)

customer_service_calls = st.number_input(
        "Customer Service Calls",
        value=1
    )

if st.button("Predict Churn"):

    data = {
            "State": state,
            "Account_length": account_length,
            "Area_code": area_code,
            "International_plan": international_plan,
            "Voice_mail_plan": voice_mail_plan,
            "Number_vmail_messages": number_vmail_messages,
            "Total_day_minutes": total_day_minutes,
            "Total_day_calls": total_day_calls,
            "Total_day_charge": total_day_charge,
            "Total_eve_minutes": total_eve_minutes,
            "Total_eve_calls": total_eve_calls,
            "Total_eve_charge": total_eve_charge,
            "Total_night_minutes": total_night_minutes,
            "Total_night_calls": total_night_calls,
            "Total_night_charge": total_night_charge,
            "Total_intl_minutes": total_intl_minutes,
            "Total_intl_calls": total_intl_calls,
            "Total_intl_charge": total_intl_charge,
            "Customer_service_calls": customer_service_calls
        }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
            st.success("Prediction Successful")
            st.write(response.json())
    else:
            st.error(response.text)


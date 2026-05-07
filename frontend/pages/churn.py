import streamlit as st
import requests

st.title("📉 Customer Churn Prediction")

State = st.text_input("State", "UT")
Account_length = st.number_input("Account Length", value=243)
Area_code = st.number_input("Area Code", value=510)

International_plan = st.selectbox("International Plan", ["Yes", "No"])
Voice_mail_plan = st.selectbox("Voice Mail Plan", ["Yes", "No"])

Number_vmail_messages = st.number_input("Voicemail Messages", value=0)

Total_day_minutes = st.number_input("Day Minutes", value=95.5)
Total_day_calls = st.number_input("Day Calls", value=92)
Total_day_charge = st.number_input("Day Charge", value=16.24)

Total_eve_minutes = st.number_input("Evening Minutes", value=163.7)
Total_eve_calls = st.number_input("Evening Calls", value=63)
Total_eve_charge = st.number_input("Evening Charge", value=13.91)

Total_night_minutes = st.number_input("Night Minutes", value=264.2)
Total_night_calls = st.number_input("Night Calls", value=118)
Total_night_charge = st.number_input("Night Charge", value=11.89)

Total_intl_minutes = st.number_input("Intl Minutes", value=6.6)
Total_intl_calls = st.number_input("Intl Calls", value=6)
Total_intl_charge = st.number_input("Intl Charge", value=1.78)

Customer_service_calls = st.number_input("Customer Service Calls", value=2)

if st.button("Predict Churn"):
    response = requests.post(
        "http://127.0.0.1:8000/predict/churn",
        json={
            "State": State,
            "Account_length": int(Account_length),
            "Area_code": int(Area_code),
            "International_plan": International_plan,
            "Voice_mail_plan": Voice_mail_plan,
            "Number_vmail_messages": int(Number_vmail_messages),
            "Total_day_minutes": float(Total_day_minutes),
            "Total_day_calls": int(Total_day_calls),
            "Total_day_charge": float(Total_day_charge),
            "Total_eve_minutes": float(Total_eve_minutes),
            "Total_eve_calls": int(Total_eve_calls),
            "Total_eve_charge": float(Total_eve_charge),
            "Total_night_minutes": float(Total_night_minutes),
            "Total_night_calls": int(Total_night_calls),
            "Total_night_charge": float(Total_night_charge),
            "Total_intl_minutes": float(Total_intl_minutes),
            "Total_intl_calls": int(Total_intl_calls),
            "Total_intl_charge": float(Total_intl_charge),
            "Customer_service_calls": int(Customer_service_calls)
        }
    )

    st.write(response.json())
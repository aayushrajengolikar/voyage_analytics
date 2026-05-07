import streamlit as st
import requests

st.title("🏨 Hotel Recommendation")

index = st.number_input("Enter Row Index (0,1,2...)", value=0)

if st.button("Get Recommendations"):
    response = requests.get(
        f"http://127.0.0.1:8000/recommend/{index}"
    )

    st.write(response.json())
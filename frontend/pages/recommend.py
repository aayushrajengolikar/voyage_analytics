import streamlit as st
import requests

st.header("Recommendation System")


index = st.number_input("Movie/Product Index", value=0)
API_URL = f"https://voyage-analytics-xdw8.onrender.com/recommend/{index}"

if st.button("Get Recommendations"):

    data = {
            "index": index
        }

    response = requests.get(API_URL, json=data)

    if response.status_code == 200:
            st.success("Recommendation Generated")
            st.write(response.json())
    else:
            st.error(response.text)
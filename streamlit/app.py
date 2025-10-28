import streamlit as st
import requests
import json
url="http://127.0.0.1:8000/predict"
st.title("🏦 Insurance Premium Prediction App")
st.markdown("enter your details below:")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("predict premium category"):
    if age and weight and height :
      input_data={
        "age":age,
        "weight":weight,
        "height":height,
         "income_lpa":income_lpa,
         "smoker":True if smoker == "Yes" else False,
         "city":city,
         "occupation":occupation
         }


    response = requests.post(url, json=input_data)
    try:
        # Send POST request to FastAPI backend
        response = requests.post(url, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction Successful!")
            st.json(result)
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Could not connect to the API: {e}")


    
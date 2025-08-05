import streamlit as st
import requests

st.title("Clinical Trials Finder")

condition = st.text_input("Condition", "Parkinson's")
zip_code = st.text_input("Zip Code", "98101")
age = st.number_input("Age", min_value=0, max_value=120, value=65)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
radius = st.slider("Search Radius (miles)", 10, 100, 50)

if st.button("Search Trials"):
    query = f"I am a {age}-year-old {gender.lower()} in {zip_code} with {condition} looking for trials within {radius} miles."
    response = requests.post("http://localhost:8000/query_trials", json={"query": query})
    st.write("### Results")
    st.json(response.json())

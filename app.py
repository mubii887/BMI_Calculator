import streamlit as st
import pandas as pd

st.title("BMI Calculator")

weight = st.slider("Weight in kg", 40, 200, 70)
height = st.slider("Height in cm", 140, 250, 175)

bmi = weight / (height / 100) ** 2

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI is less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI of 30 or greater")
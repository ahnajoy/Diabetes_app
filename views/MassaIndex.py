import streamlit as st
import numpy as np

st.title("Kalkulator Body Mass Index (BMI)")
st.write("Perhitungan ini dilakukan untuk menentukan indeks masa tubuh")

height = st.number_input("Tinggi Badan (m)", min_value=0.1, format="%.2f")
Mass = st.number_input("Massa Tubuh (Kg)", min_value=0.1, format="%.2f")

if st.button("Hitung"):
    BMI = Mass / (height ** 2)

    st.write(f"BMI anda adalah {BMI:.2f}")

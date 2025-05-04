import streamlit as st
import numpy as np
import joblib

LogReg = joblib.load(r"D:\KTI\Diabetes_app\.models\Diabetes_Prediction.pkl")
Scale = joblib.load(r"D:\KTI\Diabetes_app\.models\Scaler_Data.pkl")

encoder_bmi = joblib.load(r"D:\KTI\Diabetes_app\.models\encoder_bmi.pkl")
encoder_insulin = joblib.load(r"D:\KTI\Diabetes_app\.models\encoder_insulin.pkl")
encoder_BP = joblib.load(r"D:\KTI\Diabetes_app\.models\encoder_BP.pkl")

st.title("Prediksi Risiko Penyakit Diabetes Melitus")
st.write("Masukkan data berikut untuk memprediksi kemungkinan penyakit")
st.write("Angka yang telah tertulis pada form merupakan nilai default yang diambil melalui rata-rata setiap variabel data yang dipelajari")

KlasisfikasiBMI = ["Underweight (bmi < 18.5)", "Normal (18.5 <= bmi <= 22.9)", 
                   "Overweight (23 <= bmi <= 24.9)", "Obesity 1 (25 <= bmi <= 29.9)", "Obesity 2 (bmi > 29.9)"]
KlasifikasiInsulin = ["Low (insulin <= 16)", "Normal (16 < insulin <= 166)", "High (insulin > 166)"]
KlasifikasiBP = ['normal (tekanan darah diastole < 80)', 'prehipertensi (80 <= tekanan darah diastole <=89)',
                 'hipertensi tingkat 1 (90 <= tekanan darah diastole <= 99)', "hipertensi tingkat 2 (tekanan darah diastole > 99)"]
KlasifikasiDPF = ['0.429734 (Jika pengguna tidak memiliki kerabat yang terjangkit diabetes)', 
                  '0.5505 (Jika pengguna memiliki kerabat yang terjangkit diabetes)']

Pregnancies = st.number_input("Jumlah Kehamilan", min_value=0)
Glucose = st.number_input("Kadar Glukosa", min_value=0, value=121)
BloodPressure = st.number_input("Tekanan Darah Diastole (mmHg)", min_value=0, value=72)
SkinThickness = st.number_input("Ketebalan Kulit (mm)", min_value=0.0, value=15.0)
Insulin = st.number_input("Kadar Insulin", min_value=0, value=141)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0)
age = st.number_input("Usia", min_value=0)

if age < 20:
    inputage = 20
else:
    inputage = age

diabetes_pedigree = st.selectbox("Diabetes Pedigree Function", options=KlasifikasiDPF)

if diabetes_pedigree == '0.429734 (Jika pengguna tidak memiliki kerabat yang terjangkit diabetes)':
    input_dpf = 0.429734
else:
    input_dpf = 0.5505

klasifikasibmi = st.selectbox("Klasifikasi BMI", options=KlasisfikasiBMI, index=None)
klasifikasiinsulin = st.selectbox("Klasifikasi Insulin", options=KlasifikasiInsulin, index=None)
klasifikasibp = st.selectbox("Klasifikasi Tekanan Darah Diastole", options=KlasifikasiBP, index=None)

if st.button("Prediksi") :
    encoder1 = encoder_bmi.transform([klasifikasibmi])[0]
    encoder2 = encoder_insulin.transform([klasifikasiinsulin])[0]
    encoder4 = encoder_BP.transform([klasifikasibp])[0]

    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi,input_dpf, inputage,
                            encoder1, encoder2, encoder4]])
    
    input_data_scaled = Scale.transform(input_data)
    prediction = LogReg.predict_proba(input_data_scaled)[0][1]  

    st.write(f"Probabilitas terkena penyakit: {prediction*100:.2f}%")
    if prediction >= 0.5:
        st.error("Hasil menunjukkan diatass 50%, risiko tinggi terkena Diabetes")
    else:
        st.success("Hasil menunjukkan dibawah 50%, risiko rendah terkena penyakit Diabetes")
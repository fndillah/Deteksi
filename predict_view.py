import pickle
import streamlit as st

#read model
diabetes_model = pickle.load(open('diabetes_model.sav',"rb"))

st.title('Sistem Pembuat Keputusan Diabetes Menggunakan Decision Tree')
st.sidebar.header('Variable input')

user_input = st.sidebar.text_input("Pregnancies")

# Convert the user input to an integer if it's a valid number
if user_input.isdigit():
    slider_value = int(user_input)
else:
    slider_value = 0  # Default value if the input is not a valid number

pregnancies = st.sidebar.slider('Pregnancies',  min_value=0,  max_value=20,  step=1, value=slider_value)
glucose = st.sidebar.slider('Glucose', min_value=60, max_value=240, step=1)
blood_pressure = st.sidebar.slider('Blood Pressure', min_value=0, max_value=140, step=1)
skin_thickness = st.sidebar.slider('Skin Thickness',  min_value=0,  max_value=100,  step=1)
insulin = st.sidebar.slider('Insulin',  min_value=0,  max_value=1000,  step=1)
bmi = st.sidebar.slider('BMI',  min_value=0.0,  max_value=200.0,  step=0.01)
pedigree = st.sidebar.slider('Diabetes Pedigree Function',  min_value=0.0,  max_value=3.0,  step=0.001)
age = st.sidebar.slider('Age',  min_value=0,  max_value=100,  step=1)

diabetes_diagnose = ''

if st.button('Test Prediksi Diabetes') :
    diabetes_predict = ([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]])

    if (diabetes_predict[0] == 1):
        diabetes_diagnose = 'Terdeteksi Diabetes'
    else :
        diabetes_diagnose = 'Tidak Terdeteksi Diabetes'

st.write(diabetes_diagnose)
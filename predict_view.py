import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('diabetes_model.sav')

# Judul aplikasi
st.title('Sistem Penunjang Keputusan Deteksi Diabetes')

# Input pengguna
st.header('Masukkan Parameter Kesehatan:')
pregnancies = st.number_input('Jumlah Kehamilan', min_value=0, max_value=20, value=0)
glucose = st.number_input('Kadar Glukosa', min_value=0, max_value=240, value=0)
blood_pressure = st.number_input('Tekanan Darah Diastolik (mm Hg)', min_value=0, max_value=140, value=0)
skin_thickness = st.number_input('Ketebalan Lipatan Kulit (mm)', min_value=0, max_value=100, value=0)
insulin = st.number_input('Insulin (mu U/ml)', min_value=0, max_value=1000, value=0)
bmi = st.number_input('Indeks Massa Tubuh (BMI)', min_value=0.0, max_value=200.0, value=0.00)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.00)
age = st.number_input('Usia', min_value=0, max_value=100, value=0)

# Tombol prediksi
if st.button('Prediksi Risiko Diabetes'):
    # Buat dataframe dari input pengguna
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'Blood_pressure': [blood_pressure],
        'Skin_Thickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })
    
    # Prediksi menggunakan model
    prediction = model.predict(input_data)
    
    # Tampilkan hasil prediksi
    if prediction[0] == 1:
        st.error('Berdasarkan data yang Anda masukkan, Anda berisiko terkena diabetes.')
        st.subheader('Rekomendasi:')
        st.write("""
            - **Pantau kadar gula darah Anda secara rutin.**
            - **Perhatikan pola makan Anda dengan mengurangi asupan gula dan karbohidrat olahan.**
            - **Lakukan aktivitas fisik secara teratur, seperti berolahraga minimal 30 menit setiap hari.**
            - **Jaga berat badan ideal Anda untuk mengurangi risiko diabetes.**
            - **Konsultasikan dengan dokter atau ahli gizi untuk mendapatkan rencana diet yang sesuai.**
            - **Hindari merokok dan kurangi konsumsi alkohol.**
        """)
    else:
        st.success('Berdasarkan data yang Anda masukkan, Anda tidak berisiko terkena diabetes.')
        st.subheader('Rekomendasi Umum:')
        st.write("""
            - **Tetap jaga pola makan sehat dan seimbang.**
            - **Lakukan aktivitas fisik secara rutin untuk menjaga kebugaran tubuh.**
            - **Jaga berat badan ideal dan hindari obesitas.**
            - **Pantau kesehatan Anda secara berkala dengan memeriksa kadar gula darah dan tekanan darah.**
            - **Hindari kebiasaan buruk seperti merokok dan konsumsi alkohol berlebihan.**
        """)

# Tidak perlu memanggil st._run() atau fungsi lainnya untuk menjalankan aplikasi

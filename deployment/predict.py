import streamlit as st
import pandas as pd
import joblib


def run():
     
    with open('best_model_pipeline.pkl', 'rb') as file:
        model = joblib.load(file)
        
# Judul Aplikasi
    st.title("Prediksi Konsumsi Energi di Industri Baja")

# Input Data Baru
    st.header("Input Data Baru untuk Prediksi")
    data_baru = {
        'Leading_Current_Reactive_Power_kVarh': st.number_input("Leading Current Reactive Power (kVarh)", value=1.2),
        'Leading_Current_Power_Factor': st.number_input("Leading Current Power Factor", value=95.0),
        'Lagging_Current_Reactive.Power_kVarh': st.number_input("Lagging Current Reactive Power (kVarh)", value=3.4),
        'CO2(tCO2)': st.number_input("CO2 (tCO2)", value=0.1),
        'Lagging_Current_Power_Factor': st.number_input("Lagging Current Power Factor", value=90.0),
        'NSM': st.number_input("NSM (Seconds Since Midnight)", value=3600),
        'WeekStatus': st.selectbox("WeekStatus", ["Weekday", "Weekend"]),
        'Day_of_week': st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
        'Load_Type': st.selectbox("Load Type", ["Light_Load", "Medium_Load", "High_Load", "Maximum_Load"])
    }
    

    # Konversi ke DataFrame
    data_baru_df = pd.DataFrame([data_baru])

    # Menampilkan Data Baru
    st.subheader("Data Baru yang Dimasukkan")
    st.write(data_baru_df)

    # Prediksi Menggunakan Model
    st.header("Hasil Prediksi")
    model_file = 'best_model_pipeline.pkl'  # Pastikan nama file model sesuai
    try:
        # Memuat model
        model = joblib.load(model_file)
        # Prediksi
        prediction = model.predict(data_baru_df)
        st.success(f"Hasil Prediksi Konsumsi Energi: {prediction[0]:.2f} kWh")
    except FileNotFoundError:
        st.error("Model file tidak ditemukan. Pastikan model telah disimpan sebagai 'best_model_pipeline.pkl'.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")

        st.dataframe(data_baru_df, hide_index=True)

# import libraries

import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(layout='wide',
                   page_title='Prediksi Konsumsi Energi di Industri Baja Menggunakan Regresi Linear',)

def run():

    st.title('Prediksi Konsumsi Energi di Industri Baja Menggunakan Regresi Linear')

    # st.markdown()
    #masukan gambar
    st.image('https://cdn.betahita.id/8/1/9/6/8196_840x576.jpeg')

    #membuat latar belakang 
    st.write ('Industri baja memiliki tingkat konsumsi energi yang signifikan dan berkontribusi pada emisi karbon yang tinggi. Ketidakefisienan dalam pengelolaan energi dapat menyebabkan biaya operasional meningkat, yang berpengaruh terhadap profitabilitas perusahaan. Di era digital, pemanfaatan data historis konsumsi energi melalui teknologi machine learning dapat memberikan wawasan penting untuk mengoptimalkan penggunaan energi. Dengan membangun model prediksi berbasis data, perusahaan dapat merencanakan strategi yang lebih efisien dan berkelanjutan.')

    #data loading 
    st.write('Dataset')
    df = pd.read_csv('Steel_industry_data.csv')

    st.dataframe(df, hide_index=True)

    st.write('# Exploratory Data Analysis')

    # Visualisasi Data 

    # Distribusi variabel target 
    st.subheader("Distribusi Usage_kWh")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Usage_kWh'], kde=True, bins=30, color='blue', ax=ax)
    ax.set_title('Distribusi Usage_KWh')
    ax.set_xlabel('Usage_KWh')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    st.markdown('Berdasarkan distribusi penggunaan listrik, sebagian besar pengguna hanya mengonsumsi sedikit listrik. Hal ini menunjukkan bahwa banyak orang sudah cukup efisien dalam penggunaan energi. Namun, ada juga sedikit pengguna yang mengonsumsi listrik dalam jumlah besar. Untuk itu, kebijakan penghematan energi bisa difokuskan pada kelompok dengan penggunaan rendah, sementara bagi pengguna yang konsumsi listriknya tinggi, bisa diberikan perhatian khusus, misalnya dengan tarif lebih tinggi atau program efisiensi energi.')

    #
    # Membuat scatter plot
    st.subheader("Scatter Plot")
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Lagging_Current_Reactive.Power_kVarh'], y=df['Usage_kWh'])
    plt.title('Hubungan Lagging Reactive Power dan Usage_kWh')
    plt.xlabel('Lagging Reactive Power (kVarh)')
    plt.ylabel('Usage (kWh)')
    st.pyplot(fig)
    st.markdown('Ada hubungan positif antara Lagging Reactive Power dan Usage, meskipun sebaran data cukup luas. Peningkatan daya reaktif tertinggal cenderung berasosiasi dengan peningkatan penggunaan energi, tetapi variasi yang besar dalam data menunjukkan kemungkinan adanya faktor-faktor lain yang mempengaruhi penggunaan energi.')

    st.subheader("Plot Jumlah Data Berdasarkan Load_Type")
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='Load_Type', data=df, palette='viridis')
    plt.title('Jumlah Data Berdasarkan Load_Type')
    plt.xlabel('Load_Type')
    plt.ylabel('Jumlah')

    kolom = st.selectbox(label = 'Pilih Kolom', options= df.columns[7:13])
    # Menampilkan plot di Streamlit
    st.pyplot(fig)

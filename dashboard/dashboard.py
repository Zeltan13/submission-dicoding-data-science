import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Bike Sharing Data Analysis Dashboard')
st.write("""
# Dashboard Analisis Persewaan Sepeda
Analisis ini mencakup pengaruh kondisi cuaca (suhu, kelembaban, kecepatan angin) dan pola musiman terhadap jumlah sepeda yang disewa di Washington D.C.
""")

#Memasukan Data
@st.cache
def load_data():
    day_data = pd.read_csv('data/day.csv')
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    return day_data

data = load_data()

#Sidebar
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox('Pilih Musim', ('Semua Musim', 1, 2, 3, 4))

#Filter berdasarkan musim
if season_filter != 'Semua Musim':
    data = data[data['season'] == season_filter]

#Total Penyewaan berdasarkan musim yang dipilih
st.write(f"Menampilkan jumlah persewaan untuk musim: {season_filter}")

#Pengaruh suhu terhadap jumlah persewaan
st.subheader('Pengaruh Suhu terhadap Jumlah Sepeda yang Disewa')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='temp', y='cnt', data=data)
plt.title('Pengaruh Suhu terhadap Jumlah Sepeda yang Disewa')
plt.xlabel('Temperature (Normalized)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

#Pengaruh kelembaban terhadap jumlah persewaan
st.subheader('Pengaruh Kelembaban terhadap Jumlah Sepeda yang Disewa')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='hum', y='cnt', data=data)
plt.title('Pengaruh Kelembaban terhadap Jumlah Sepeda yang Disewa')
plt.xlabel('Humidity (Normalized)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

#Pengaruh kecepatan angin terhadap jumlah persewaan
st.subheader('Pengaruh Kecepatan Angin terhadap Jumlah Sepeda yang Disewa')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='windspeed', y='cnt', data=data)
plt.title('Pengaruh Kecepatan Angin terhadap Jumlah Sepeda yang Disewa')
plt.xlabel('Windspeed (Normalized)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

#jumlah sepeda yang disewa berdasarkan musim
st.subheader('Jumlah Sepeda yang Disewa Berdasarkan Musim')
plt.figure(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=data, estimator=sum)
plt.title('Jumlah Sepeda yang Disewa Berdasarkan Musim')
plt.xlabel('Season (1:Spring, 2:Summer, 3:Fall, 4:Winter)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

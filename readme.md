# Dashboard Analisis Data Bike Sharing

## Gambaran Proyek
Proyek ini adalah sebuah dashboard yang dibangun menggunakan **Streamlit** untuk menganalisis **Bike Sharing Dataset**. Dashboard ini memvisualisasikan pengaruh kondisi cuaca seperti suhu, kelembaban, dan kecepatan angin, serta pola musiman terhadap jumlah sepeda yang disewa di Washington D.C.

## Fitur
- **Analisis Cuaca**: Mengeksplorasi bagaimana suhu, kelembaban, dan kecepatan angin mempengaruhi jumlah penyewaan sepeda.
- **Analisis Musiman**: Melihat tren penyewaan sepeda berdasarkan musim (Musim Semi, Panas, Gugur, Dingin).
- **Filter Interaktif**: Filter data berdasarkan musim menggunakan sidebar.

## Struktur Proyek
- **dashboard.py**: Skrip Python utama yang membuat dashboard Streamlit.
- **data/day.csv**: Data harian untuk penyewaan sepeda, termasuk informasi cuaca dan jumlah penyewaan.
- **data/hour.csv**: Data per jam untuk penyewaan sepeda, termasuk informasi cuaca dan jumlah penyewaan.
- **Proyek_Analisis_Data.ipynb**: Notebook Jupyter yang berisi eksplorasi data (EDA) untuk proyek ini.
- **requirements.txt**: Daftar paket yang dibutuhkan untuk menjalankan proyek.

## Dataset
Dataset yang digunakan dalam proyek ini berasal dari **Bike Sharing Dataset**, yang mencakup informasi harian dan per jam tentang penyewaan sepeda, data cuaca, dan variabel terkait lainnya.

## Menjalankan app Streamlit (Pada local)
Pada terminal tuliskan:
```
streamlit run dashboard.py
```
Pastikan semua **requirements** sudah di install
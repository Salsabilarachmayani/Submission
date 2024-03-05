import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
day_df = pd.read_csv("bike_sharing.csv")
hour_df = pd.read_csv("bike_hour.csv")

#streamlit dashboard
st.title("Bike Sharing Analysis")

st.subheader("Data Visualisation")

#visualisation 1
st.header('Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda')
dt = day_df.groupby(['weathersit', 'yr'])['cnt'].mean().unstack()
st.write('Bar Chart:')
fig, ax = plt.subplots()
dt_plot = dt.plot(kind='bar', width=0.8, ax=ax)
ax.set_xlabel('Cuaca')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
ax.set_title('Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda Harian')
ax.set_xticklabels(dt.index, rotation=45)
ax.legend(title='Tahun')
st.pyplot(fig)

#explain the bar 1
st.markdown("Dari grafik diatas dapat disimpulkan bahwa saat cuaca sedang cerah (clear) jumlah sewa sepeda lebih banyak dibandingkan dengan cuaca lainnya. Hal ini dapat disebabkan karena cuaca cerah sangat pas untuk bersepeda oleh karena itu ketika cuaca sedang hujan atau bersalju jumlah sewa sepeda menurun.")

#visualisation 2
st.header('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
data = day_df.groupby(['season', 'yr'])['cnt'].mean().unstack()
st.write('Bar Chart:')
fig, ax = plt.subplots()
data_plot = data.plot(kind='bar', width=0.8, ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
ax.set_title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
ax.set_xticklabels(data.index, rotation=45)
ax.legend(title='Tahun')
st.pyplot(fig)

#explain the bar 2
st.markdown("Dari grafik diatas dapat disimpulkan bahwa musim mempengaruhi jumlah sewa sepeda harian. Musim gugur memiliki jumlah sewa sepeda yang paling banyak dibandingkan dengan jumlah sewa sepeda di musim lainnya. Hal ini dapat disebabkan karena ketika musim gugur suhu udaranya tidak terlalu dingin juga tidak terlalu panas serta tidak ada halangan seperti salju.")
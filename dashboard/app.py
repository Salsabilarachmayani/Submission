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

st.header('Jumlah Sewa Sepeda Harian Berdasarkan Jam')
st.write('Line Chart:')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt", hue="yr", data=hour_df, ax=ax)
ax.set_title("Jumlah Sewa Sepeda Harian Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")
ax.legend(title='Tahun')

# Display the plot in Streamlit
st.pyplot(fig)

st.header('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
data = day_df.groupby(['season', 'yr'])['cnt'].mean().unstack()
# Plot the bar chart
st.write('Bar Chart:')
fig, ax = plt.subplots()
data_plot = data.plot(kind='bar', width=0.8, ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
ax.set_title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
ax.set_xticklabels(data.index, rotation=45)
ax.legend(title='Tahun')

# Display the plot in Streamlit
st.pyplot(fig)
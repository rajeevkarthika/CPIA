# Import packages
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from functions import plot_radar 

# Load the dataframe
df = pd.read_csv('Datasets/cpia_africa.csv')

# Title
st.title('Country Performace')

# Sidebar: Option to select a country
countries = df['Country or Area'].unique()
country = st.selectbox("Select Country", countries)

# Data for the selected country
df_selected_country = df[(df['Country or Area']==country)]

# List of unique years in the filtered dataframe
years = sorted(df_selected_country['Year'].unique())

# Display the data for the selected country
st.subheader(f'Data for {country}')
st.write(df_selected_country)

# Section: Trends in CPIA rating over the years
st.subheader(f'Performance of {country} over the years')

# Line plot
fig1, ax = plt.subplots()
df_selected_country.plot(ax=ax, x='Year', y=['Economic Management', 'Structural Policies', 'Policies for Social Inclusion and Equity', 'Public Sector Management and Institutions', 'Overall CPIA'], kind='line')  
#ax.set_title("CPIA ratings over the years")
ax.set_ylabel("CPIA Rating")
ax.set_xticks(years)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xticklabels(years, rotation=90)

# Display the plot
st.pyplot(fig1)

# Section: Performance of the selected country for a given year
st.subheader(f'Performace of {country} for a given year')

# Option to select an year
year = st.slider("Select Year", min_value=years[0], max_value=years[-1], value=years[0])

# Data for selected year
df_filtered = df[(df['Country or Area']==country) & (df['Year']==year)]

# Radar plot using the function plot_radar 
if not df_filtered.empty:
    fig = plot_radar(df_filtered, country, year)
    st.plotly_chart(fig)
else:
    st.write('No data available. Please check the input DataFrame')
# Import Packages
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from functions import plot_choropleth

# Load the dataframe
df = pd.read_csv('Datasets/cpia_africa.csv')

# Section: Overview of CPIA rating across African countries for a given year
st.subheader(f'An overview of overall CPIA rating acorss Africa')

# Option to select an year
years = sorted(df['Year'].unique())
year = st.selectbox("Select Year", years)

# Choropleth plot using the function plot_choropleth
fig = plot_choropleth(df, year)

# Display the plot
st.plotly_chart(fig)

# Section: CPIA ratings by country
st.subheader('CPIA Rating Composition')

# Stacked bar plot
fig1, ax = plt.subplots(figsize=(20, 20))
df[df['Year']==year].sort_values(by='Economic Management', ascending=False).plot.barh(x='Country or Area', y=['Economic Management', 'Structural Policies', 'Policies for Social Inclusion and Equity', 'Public Sector Management and Institutions'], stacked=True, ax=ax)
ax.legend(loc='upper right')
ax.set_title(f'CPIA Rating Composition for the Year {year}')

# Display the plot
st.pyplot(fig1)
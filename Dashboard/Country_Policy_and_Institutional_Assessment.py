# Import packages
import streamlit as st
import pandas as pd

# Title
st.title('CPIA Insights: Policy and Institutional Analysis of African Countries (2005–2023)')

# Content
st.markdown("### What is CPIA?")
st.write("""Country Policy and Institutional Assessment (CPIA) measures the extent to which a country’s policy and institutional framework supports 
sustainable growth and poverty reduction, and consequently, the effective use of development assistance.""")
st.write("""The CPIA rates countries against a set of 16 criteria grouped in four clusters, namely **Economic Management**, 
**Structural Policies**, **Policies for Social Inclusion/Equity**, **Public Sector Management and Institutions**.
For each criterion, countries are rated on a scale of **1 (low) to 6 (high)**. 
A 1 rating corresponds to a very weak performance, and a 6 rating to a very strong performance.""")


st.markdown("### Dataset")

st.write("""The data is retrieved from the [UNdata](http://data.un.org/Explorer.aspx?d=UNODC) database, 
which sources its information from the [World Development Indicators](https://databank.worldbank.org/source/world-development-indicators)
 (WDI) published by the World Bank.""")
st.write("""The dataset contains information on 36 African countries, covering the period from 2005 to 2023.
""")

# Load the dataframe
df = pd.read_csv('Datasets/cpia_africa.csv')

# Display the data
st.write(df)


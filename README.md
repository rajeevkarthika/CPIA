# CPIA Insights: Policy and Institutional Analysis of African Countries (2005–2023)

This data analysis project assesses the policy and institutional performance of African countries using the **World Bank’s Country Policy and Institutional Assessment (CPIA)** ratings. The CPIA evaluates the extent to which a country’s policy and institutional framework fosters sustainable economic growth and poverty reduction, as well as its capacity to effectively utilise development assistance.

### Objectives

The analysis explores:

- The relationship across the CPIA cluster scores.

- Regional variations and changes in cluster scores over time.

- Identification of top-performing and low-performing countries.

- Trends in CPIA scores from 2005 to 2023.

- Application of K-Means cluster analysis to identify countries with similar CPIA cluster ratings.

### Project Structure

This project consists of:

- Jupyter Notebook: Contains data cleaning, analysis, and visualisations.

- Data Visualisation Dashboard: An interactive dashboard for exploring CPIA trends and country performance.

### Technologies Used

This analysis is based in Python and utilises the following libraries:

- NumPy and pandas for data manipulation and analysis

- matplotlib, Seaborn, and Plotly for data visualisation

- scikit-learn for K-Means cluster analysis

- Streamlit for building an interactive dashboard

### Dataset

The data is retrieved from the [UNdata](http://data.un.org/Explorer.aspx?d=UNODC) database, which sources its information from the [World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) (WDI) published by the World Bank. The final dataset is saved as [cpia_africa.csv](CPIA/Datasets/cpia_africa.csv) in the directory CPIA/Datasets/. 

### Data Visualisation Dashboard

The visualisation dashboard is created with streamlit. 

**Environment Setup**

Create a Python virtual environment (for example `venv`) with the following command:

```bash
python -m venv venv
```

then activate the environment, and install all the required packages:

```bash
source venv/bin/activate
python -m pip install -r requirements.txt
```
The dashboard can be run by the following command:

```bash
streamlit run Dashboard/Country_Policy_and_Institutional_Assessment.py
```

### Note

This is a data-driven project intended for educational purposes, inspired by the [CPIA portal](https://cpia.afdb.org/?page=results&subpage=profile&indicator_id=A-E_&country_id=BJ&year=2018) by the African Development Bank Group.

# Import packages
import plotly
import numpy as np
import plotly.graph_objects as go

# Define a function to plot a radar plot
def plot_radar(df, country, year):
    """
    Generates a radar plot of CPIA ratings for a specific country and year.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing columns for country names, CPIA rating, and years.
    country : str
        The name of the country for which to generate the radar plot.
    year : int
        The year corresponding to the CPIA ratings.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        A radar plot visualising CPIA ratings across different clusters for the specified country and year.
    """
    ratings=['Economic Management', 'Structural Policies', 'Policies for Social Inclusion and Equity', 'Public Sector Management and Institutions', 'Overall CPIA']
    r=df[ratings].values.flatten()
    np.append(r, r[0])
    theta=ratings
    theta.append(theta[0])

    fig = go.Figure(data=go.Scatterpolar(
        r=r,
        theta=theta,
        fill='toself',
    ))
    fig.update_layout(
    title= dict(
        text = f"Performance of {country} in {year}",
        x = 0.5,
        y = 0.95,
        xanchor='center',
        yanchor='top',
    ),
    polar=dict(
        radialaxis=dict(
            visible=True,
            tickangle=0,         
            tickfont=dict(size=12, color="blue"),  
            range=[0, 5],         
            tickvals=[1,2,3,4,5],   
            ticktext=["1", "2", "3", "4", "5"],  
            gridcolor="lightgrey",
        )
    )
)
    return fig

# Define a function to plot a choropleth map
def plot_choropleth(df, year):
    """
    Generates a choropleth map of Overall CPIA rating for a specific year.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing columns for country names, CPIA rating, and years.
    year : int
        The year corresponding to the CPIA ratings.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        A choropleth map visualising Overall CPIA ratings across African countries for the specified year.
    """
    df = df[df['Year']==year]

    fig = go.Figure(data=go.Choropleth(
        locations=df['Country or Area'], 
        z = df['Overall CPIA'].astype(float), 
        locationmode = 'country names', 
        colorscale = 'Cividis',
        colorbar_title = "Rating",
    ))

    fig.update_layout(
        width=1200,  
        height=800,
        title_text = f'Overall CPIA Rating for the year {year}',
        geo_scope='africa', 
    )

    return fig 
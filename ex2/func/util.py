import plotly.express as px
import pandas as pd
import os

def clean_data(df):
    """ 
    Function for rounding the values for GDP to get rid of decimal points.

    """
    df['GDP'] = df['GDP'].round()

    return df

def load_data(countries, folder_name):
    """
    Function for loading the data from a number of csv files, returning a pandas dataframe.
    
    """

    dfs = []

    for country in countries:
        
        file_name = f"{country}.csv"
        file_path = os.path.join('.', folder_name, file_name)
        
        df = pd.read_csv(file_path)
        df.columns = ['Date', 'GDP']
        df['Country'] = country
        
        dfs.append(df)

    combined_df = pd.concat(dfs)

    combined_df['Date'] = pd.to_datetime(combined_df['Date'])

    return combined_df

def plot_data(df, countries):
    """
    Function for creating a line plot that compares the GDP of the different countries over time.
    
    """
    filtered_df = df[df["Country"].isin(countries)]
    fig = px.line(
        filtered_df,
        x="Date",
        y="GDP",
        color="Country",
        title="2000-2022 GDP Data ",
        labels={"GDP": "GDP (in current USD)", "Date": "Year"},
        line_shape="linear",
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Nominal GDP, Index, Jan 2000 = 100",
        legend_title="Country",
        template="plotly_white"
    )

    fig.show()

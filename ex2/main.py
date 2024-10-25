# from source.load_data import load_data
# from source.plot_data import plot_data
# from source.clean_data import clean_data
from func.util import *

if __name__ == "__main__":
    # List of countries to analyze
    countries = ['BR', 'CN', 'DE', 'JP', 'CH', 'UK', 'US']

    # Load the data (assuming you have the URL or file)
    gdp_data = load_data(countries, "data")

    # Clean the data
    gdp_data_cleaned = clean_data(gdp_data)

    # Plot the data
    plot_data(gdp_data_cleaned, countries)

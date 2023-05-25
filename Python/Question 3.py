"""
Write a program, which would download the data from the provided link, and then read the data and convert
that into properly structured data and return it in Excel format.
"""
import pandas as pd
import requests


def download_and_convert_to_excel(url, filename):
    response = requests.get(url)  # request to url
    data = response.json()  # converting to json data
    df_data = pd.DataFrame(data['pokemon'])  # creating new dataframe by passing data
    df_data.to_excel(filename, index=False, sheet_name='Pokemon data')  # converting data frame to excel
    print(f"Data saved to {filename}")


# Example usage
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
filename = "pokemon_data.xlsx"
download_and_convert_to_excel(url, filename)

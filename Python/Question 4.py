"""
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
"""

import pandas as pd
import requests


def download_and_convert_to_csv(url, filename):
    response = requests.get(url)  # request to url
    data = response.json()  # converting to json data
    data_df = pd.DataFrame(data)  # creating new dataframe by passing data
    data_df.to_csv(filename, index=False)  # converting data frame to csv file
    print(f"Data saved to {filename}")


# Example
url = "https://data.nasa.gov/resource/y77d-th95.json"
filename = "data.csv"
download_and_convert_to_csv(url, filename)

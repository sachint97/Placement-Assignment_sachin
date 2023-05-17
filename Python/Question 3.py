import pandas as pd
import requests

def download_and_convert_to_excel(url, filename):
    response = requests.get(url)
    data = response.json()
    df_data = pd.DataFrame(data)
    df_data.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
url = "https://gist.githubusercontent.com/gcollazo/884a489a50aec7b53765405f40c6fbd1/raw/49d1568c34090587ac82e80612a9c350108b62c5/sample.json"
filename = "sample_data.xlsx"
download_and_convert_to_excel(url, filename)

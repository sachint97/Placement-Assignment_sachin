"""Write a program to download the data from the given API link and then extract the following data with
proper formatting"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Function to remove HTML tags from summary
def remove_html_tags(summary):
    soup = BeautifulSoup(summary, "html.parser")
    return soup.get_text()

# Download data from API
def download_data(url):
    response = requests.get(url)
    data = response.json()
    attributes = []
    episodes = data["_embedded"]["episodes"]

    for episode in episodes:
        # Data attributes
        episode_id = episode["id"]
        url = episode["url"]
        name = episode["name"]
        season = episode["season"]
        number = episode["number"]
        episode_type = episode["type"]
        airdate = episode["airdate"]
        airtime = datetime.strptime(episode["airtime"], "%H:%M").strftime("%I:%M %p")
        runtime = episode["runtime"]
        average_rating = episode["rating"]["average"]
        summary = remove_html_tags(episode['summary'])
        medium_image = episode["image"]["medium"]
        original_image = episode["image"]["original"]

        # Creating data attribute
        attribute_dict = {
            "id": episode_id,
            "url": url,
            "name": name,
            "season": season,
            "number": number,
            "type": episode_type,
            "airdate": airdate,
            "airtime": airtime,
            "runtime": runtime,
            "average_rating": average_rating,
            "summary": summary,
            "medium_image": medium_image,
            "original_image": original_image
        }

        # Appending attribute
        attributes.append(attribute_dict)

    return attributes


api_url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
data = download_data(api_url)
for episode in data:
    print(episode)


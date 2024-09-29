import json
import requests
import folium
import os
from dotenv import load_dotenv
from geopy import distance
from flask import Flask

app=Flask(__name__)


def coffee_map():
    with open("index.html") as file:
        return file.read()

def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def get_distance(dist):
    return dist["distance"]


def main():
    load_dotenv()
    apikey=os.getenv('apikey')
    with open("coffee.json", "r", encoding="CP1251") as my_file:
        content = my_file.read()
    file_content = json.loads(content)
    human_location = input('Где вы находитесь?')
    coods = fetch_coordinates(apikey, human_location)

    informative_list = []
    for cafe in file_content:
        name = cafe['Name']
        latitude = cafe['Latitude_WGS84']
        longitude = cafe['Longitude_WGS84']
        length = distance.distance(coods, (latitude, longitude)).km

        item = {
            "title": name,
            "distance": length,
            "latitude": latitude,
            "longitude": longitude
        }
        informative_list.append(item)

    sorted_informative_list = sorted(informative_list, key=get_distance)
    nearest_cafe = sorted_informative_list[:6]

    mini_map = folium.Map(location=coods)
    for cafe in nearest_cafe:
        folium.Marker(
            location=[cafe['latitude'], cafe['longitude']],
            tooltip="кофейня",
            popup=f"{cafe['title']}: {cafe['distance']:.2f}км",
            icon=folium.Icon(color="green")
        ).add_to(mini_map)
    mini_map.save("index.html")

    app.add_url_rule('/','coffee_here',coffee_map)
    app.run('0.0.0.0')


if __name__ == '__main__':
    main()

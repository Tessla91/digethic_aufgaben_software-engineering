import requests

def get_city_coordinates [city]:
    api_url = "https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=10&language=en&format=json" + city

    response = requests.get(api_url)

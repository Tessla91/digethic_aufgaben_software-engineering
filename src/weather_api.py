import requests

def get_city_coordinates(city):
    api_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city
    response = requests.get(api_url).json()
    return response
def get_weather_forecast(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(api_url).json()
    return response

def get_weather_history(latitude, longitude, start_date, end_date):
    api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(api_url).json()
    return response

city = "Berlin"
city_coordinates = get_city_coordinates(city)
latitude = city_coordinates ["results"][0]["latitude"]
longitude = city_coordinates ["results"][0]["longitude"]
print (city_coordinates ["results"][0])

print (
    "The coordination of",
    city,
    "are: longitude:",
    longitude,
    "latidude:",
    latitude,
)

weather_forecast = get_weather_forecast(latitude, longitude)

time = weather_forecast["daily"]["time"]
temperature_2m_min = weather_forecast ["daily"]["temperature_2m_min"]
temperature_2m_max = weather_forecast ["daily"]["temperature_2m_max"]
print (time)
print(temperature_2m_max)

for i in range(len(time)):
    print(
        "The weather forecast for",
        city,
        "on",
        time[i],
        "is a minimum temperature of",
        temperature_2m_min[i],
        "and a maximum temperature of",
        temperature_2m_max[i],
    )
weather_date = "2019-03-08"
weather_history = get_weather_history(
    latitude=latitude,
    longitude=longitude,
    start_date=weather_date,
    end_date=weather_date,
)

historic_time = weather_history["daily"]["time"]
historic_temperature_2m_min = weather_history["daily"]["temperature_2m_min"]
historic_temperature_2m_max = weather_history["daily"]["temperature_2m_max"]

for i in range(len(historic_time)):
    print(
        "The weather in",
        city,
        "on",
        historic_time[i],
        "was a minimum temperature of",
        temperature_2m_min[i],
        "and a maximum temperature of",
        temperature_2m_max[i],
    )

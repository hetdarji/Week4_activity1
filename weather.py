import os
import requests

api_key = os.getenv("WEATHER_API_KEY")
city = "Toronto"

if not api_key:
    print("No API key found in environment.")
    exit(1)

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    print(f"Weather in {city}: {NewYork}")
    print(f"Temperature: {temp}°C")
except Exception as e:
    print("Error fetching weather data:", e)

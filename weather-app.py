import urllib.request
import urllib.parse
import json

print("🌤️ Python Weather App")

city = input("Enter your city: ")

# Find the city's coordinates
search_url = (
    "https://geocoding-api.open-meteo.com/v1/search?"
    + urllib.parse.urlencode({
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })
)

try:
    with urllib.request.urlopen(search_url) as response:
        location_data = json.loads(response.read().decode())

    if "results" not in location_data:
        print("❌ City not found.")
    else:
        location = location_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        # Get current weather
        weather_url = (
            "https://api.open-meteo.com/v1/forecast?"
            + urllib.parse.urlencode({
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m,weather_code"
            })
        )

        with urllib.request.urlopen(weather_url) as response:
            weather_data = json.loads(response.read().decode())

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]

        print()
        print(f"📍 Location: {city_name}, {country}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💨 Wind Speed: {wind_speed} km/h")
        print(f"🌤️ Weather Code: {weather_code}")

except Exception:
    print("❌ Something went wrong. Please check your internet connection.")

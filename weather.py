import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_for_city(city: str, api_key: str) -> dict:
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  # Fahrenheit
    }
    resp = requests.get(API_URL, params=params, timeout=10)
    resp.raise_for_status()
    j = resp.json()
    return {
        "temp_f": j.get("main", {}).get("temp"),
        "humidity": j.get("main", {}).get("humidity"),
        "conditions": ", ".join([w.get("description", "") for w in j.get("weather", [])]),
        "raw": j
    }

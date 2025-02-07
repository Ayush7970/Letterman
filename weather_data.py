import requests
import os

# Load API key from environment variable (recommended for security)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "77a31bded1435148afa53c21536992d4")  

CITY = "Chicago"  # Change this to your target location

def get_weather_forecast():
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}"
        response = requests.get(url)

        # Check if API request was successful
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            return None
        
        data = response.json()

        # Extract 7-day weather data
        forecast = []
        for entry in data["list"]:  # The API returns data for every 3 hours
            forecast.append({
                "date": entry["dt_txt"],
                "temperature": round(entry["main"]["temp"] - 273.15, 2),  # Convert Kelvin to Celsius
                "humidity": entry["main"]["humidity"],
                "wind_speed": entry["wind"]["speed"]
            })

        return forecast[:7]  # Take only the first 7 entries (7 days)

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        return None

if __name__ == "__main__":
    forecast = get_weather_forecast()
    if forecast:
        print(forecast)
    else:
        print("⚠️ Failed to fetch weather forecast.")

import requests

def get_weather(city_name):
    API_KEY = "6b016e4e34006b313974a667adf7136c"  # Replace with your valid API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description'].title()
            temperature = f"{data['main']['temp']}\u00b0C"
            humidity = f"{data['main']['humidity']}%"
            return weather_desc, temperature, humidity
        else:
            print("Weather API error:", data.get("message", "Unknown error"))
            return "Unavailable", "Unavailable", "Unavailable"
    except Exception as e:
        print("Exception while fetching weather:", str(e))
        return "Unavailable", "Unavailable", "Unavailable"
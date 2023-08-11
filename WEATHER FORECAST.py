import requests


def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data


def display_weather(weather_data):
    if weather_data["cod"] == 200:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found. Please check the input.")


def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather_data(api_key, location)
    display_weather(weather_data)


if __name__ == "__main__":
    main()

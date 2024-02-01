import requests



city = input("Enter a city : ")

def get_weather(coordinates):
    # The base URL for the Open-Meteo API
    api_url = "https://api.open-meteo.com/v1/forecast"

   

    # Parameters for the API request
    params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "hourly": "temperature_2m"
    }

    # Making the API request
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        # Extracting the weather data
        data = response.json()
        return data
    else:
        return "Failed to retrieve weather data."

def get_coordinates(city):
    # The base URL for the Open-Meteo Geocoding API
    geocoding_api_url = "https://geocoding-api.open-meteo.com/v1/search"

    # Parameters for the API request
    params = {
        "name": city,
        "count": 1,  # We only need the top result
        "language": "en",
        "format": "json"
    }

    # Making the API request for geocoding
    response = requests.get(geocoding_api_url, params=params)
    
    if response.status_code == 200:
        # Extracting the latitude and longitude
        data = response.json()
        if data["results"]:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]
            return latitude, longitude
        else:
            return "No coordinates found for the specified city."
    else:
        return "Failed to retrieve coordinates."



# Fetching coordinates for city
coordinates = get_coordinates(city)

weather_data = get_weather(coordinates)

# Extracting the current weather data from the response
if isinstance(weather_data, dict) and 'hourly' in weather_data:
    current_weather_data = weather_data['hourly']
    # Assuming the last entry in the data is the most current
    current_time = current_weather_data['time'][-1]
    current_temperature = current_weather_data['temperature_2m'][-1]

    current_weather_info = f"Current weather in {city} : {current_temperature}°C at {current_time}"
else:
    current_weather_info = "Unable to retrieve current weather data."

print(current_weather_info)


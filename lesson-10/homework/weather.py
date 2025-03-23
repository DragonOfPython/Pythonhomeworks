import requests

def get_weather_data(lat, lon, api_key):
    # Construct the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    print(f"Requesting URL: {url}")  # Debugging line to check the request URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        # Print the weather information
        print(f"Weather at coordinates ({lat}, {lon}):")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        # Print error message if the request was unsuccessful
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        print(f"Response: {response.text}")  # Print the response text for more information

if __name__ == "__main__":
    # Coordinates for Tashkent
    latitude = 41.311081
    longitude = 69.240562
    api_key = "4b08097bd2eff092140655719c83d17e"  # Your OpenWeatherMap API key
    get_weather_data(latitude, longitude, api_key)
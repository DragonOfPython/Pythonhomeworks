from bs4 import BeautifulSoup

# Load the HTML file
with open('weather.html', 'r') as file:
    html_content = file.read()

# Parse the HTML file
soup = BeautifulSoup(html_content, 'html.parser')

# Extract weather forecast details
weather_forecast = []
table = soup.find('table')
rows = table.find_all('tr')[1:]  # Skip the header row
for row in rows:
    day, temperature, condition = [cell.get_text() for cell in row.find_all('td')]
    weather_forecast.append({'day': day, 'temperature': temperature, 'condition': condition})

# Display Weather Data
for forecast in weather_forecast:
    print(f"Day: {forecast['day']}, Temperature: {forecast['temperature']}, Condition: {forecast['condition']}")

# Find Specific Data
highest_temp_day = max(weather_forecast, key=lambda x: int(x['temperature'][:-1]))['day']
print(f"Day with the highest temperature: {highest_temp_day}")

sunny_days = [forecast['day'] for forecast in weather_forecast if forecast['condition'] == 'Sunny']
print(f"Days with 'Sunny' condition: {', '.join(sunny_days)}")

# Calculate Average Temperature
temperatures = [int(forecast['temperature'][:-1]) for forecast in weather_forecast]
average_temperature = sum(temperatures) / len(temperatures)
print(f"Average Temperature for the week: {average_temperature}°C")
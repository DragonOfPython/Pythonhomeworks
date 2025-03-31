import pandas as pd

# Grouped Aggregations on Titanic Dataset
titanic_df = pd.read_csv('titanic.csv')

# Group passengers by Pclass and calculate average age, total fare, and count of passengers
grouped_titanic = titanic_df.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'sum', 'PassengerId': 'count'}).reset_index()
grouped_titanic.columns = ['Pclass', 'Average Age', 'Total Fare', 'Passenger Count']
print("Grouped Aggregations on Titanic Dataset:")
print(grouped_titanic)

# Multi-level Grouping on Movie Data
movie_df = pd.read_csv('movie.csv')

# Group movies by color and director_name and calculate total num_critic_for_reviews and average duration for each group
grouped_movie = movie_df.groupby(['color', 'director_name']).agg({'num_critic_for_reviews': 'sum', 'duration': 'mean'}).reset_index()
print("\nMulti-level Grouping on Movie Data:")
print(grouped_movie)

# Nested Grouping on Flights Data
flights_df = pd.read_csv('flights.csv')

# Convert the 'Year' and 'Month' columns to datetime format
flights_df['Year_Month'] = pd.to_datetime(flights_df['Year'].astype(str) + '-' + flights_df['Month'].astype(str), format='%Y-%m')

# Group flights by Year and Month and calculate total number of flights, average arrival delay, and maximum departure delay
nested_grouped_flights = flights_df.groupby(['Year', 'Month']).agg({'FlightNumber': 'count', 'ArrDelay': 'mean', 'DepDelay': 'max'}).reset_index()
nested_grouped_flights.columns = ['Year', 'Month', 'Total Flights', 'Avg Arrival Delay', 'Max Departure Delay']
print("\nNested Grouping on Flights Data:")
print(nested_grouped_flights)
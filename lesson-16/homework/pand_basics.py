import sqlite3
import pandas as pd

# Part 1: Reading Files

# 1. Read the customers table from chinook.db
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print('Customers Table from chinook.db:')
print(customers_df.head(10))

# 2. Load the JSON file iris.json
iris_df = pd.read_json('iris.json')
print('\nShape of iris dataset:')
print(iris_df.shape)
print('Columns of iris dataset:')
print(iris_df.columns)

# 3. Load the Excel file titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print('\nFirst 5 rows of titanic dataset:')
print(titanic_df.head())

# 4. Read the Parquet file flights.parquet
flights_df = pd.read_parquet('flights.parquet')
print('\nSummary of flights dataset:')
print(flights_df.info())

# 5. Load the CSV file movie.csv
movie_df = pd.read_csv('movie.csv')
print('\nRandom sample of 10 rows from movie dataset:')
print(movie_df.sample(10))

# Part 2: Exploring DataFrames

# 1. Using the DataFrame from iris.json
iris_df.columns = iris_df.columns.str.lower()
selected_columns = iris_df[['sepal_length', 'sepal_width']]
print('\nSelected columns from iris dataset:')
print(selected_columns.head())

# 2. From the titanic.xlsx DataFrame
above_30 = titanic_df[titanic_df['Age'] > 30]
gender_counts = titanic_df['Sex'].value_counts()
print('\nPassengers above 30 years old:')
print(above_30.head())
print('\nCounts of male and female passengers:')
print(gender_counts)

# 3. From the Flights parquet file
selected_columns = flights_df[['origin', 'dest', 'carrier']]
unique_destinations = flights_df['dest'].nunique()
print('\nSelected columns from flights dataset:')
print(selected_columns.head())
print('\nNumber of unique destinations:')
print(unique_destinations)

# 4. From the movie.csv file
long_movies = movie_df[movie_df['duration'] > 120]
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print('\nMovies with duration > 120 minutes:')
print(long_movies.head())
print('\nSorted movies by director_facebook_likes:')
print(sorted_movies.head())

# Part 3: Challenges and Explorations

# 1. From iris.json
numerical_stats = iris_df.describe()
print('\nStatistics for numerical columns in iris dataset:')
print(numerical_stats)

# 2. From titanic.xlsx
min_age = titanic_df['Age'].min()
max_age = titanic_df['Age'].max()
total_age = titanic_df['Age'].sum()
print('\nMinimum age of passengers:', min_age)
print('Maximum age of passengers:', max_age)
print('Total sum of passenger ages:', total_age)

# 3. From movie.csv
top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top5_longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'director_name']]
print('\nDirector with the highest total director_facebook_likes:', top_director)
print('\nTop 5 longest movies and their directors:')
print(top5_longest_movies)

# 4. From Flights parquet file
missing_values = flights_df.isnull().sum()
flights_df['some_numerical_column'] = flights_df['some_numerical_column'].fillna(flights_df['some_numerical_column'].mean())
print('\nMissing values in flights dataset:')
print(missing_values)
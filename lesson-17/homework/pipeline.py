import pandas as pd

# Pipeline on Titanic Dataset
titanic_df = pd.read_csv('titanic.csv')

# Create a pipeline to filter passengers who survived, fill missing Age values with the mean, and create Fare_Per_Age column
def titanic_pipeline(data):
    data = data[data['Survived'] == 1]
    data['Age'].fillna(data['Age'].mean(), inplace=True)
    data['Fare_Per_Age'] = data['Fare'] / data['Age']
    return data

titanic_df_processed = titanic_df.pipe(titanic_pipeline)
print("Titanic Dataset after processing:")
print(titanic_df_processed[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head(10))

# Pipeline on Flights Data
flights_df = pd.read_csv('flights.csv')

# Create a pipeline to filter flights with departure delay > 30 minutes and calculate Delay_Per_Hour
def flights_pipeline(data):
    data = data[data['DepDelay'] > 30]
    data['Delay_Per_Hour'] = data['DepDelay'] / data['CRSDepTime']
    return data

flights_df_processed = flights_df.pipe(flights_pipeline)
print("\nFlights Dataset after processing:")
print(flights_df_processed[['FlightNumber', 'DepDelay', 'CRSDepTime', 'Delay_Per_Hour']].head(10))
import pandas as pd

# Apply a Custom Function on Titanic Dataset
titanic_df = pd.read_csv('titanic.csv')

# Write a function to classify passengers as Child (age < 18) or Adult
def classify_age_group(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

# Use apply to create a new column, Age_Group, with these values
titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age_group)
print("Titanic Dataset with Age_Group column:")
print(titanic_df[['Age', 'Age_Group']].head(10))

# Normalize Employee Salaries
employee_df = pd.read_csv('employee.csv')

# Normalize the salaries within each department
employee_df['Normalized_Salary'] = employee_df.groupby('Department')['Salary'].transform(lambda x: (x - x.mean()) / x.std())
print("\nEmployee Dataset with Normalized Salaries:")
print(employee_df[['EmployeeID', 'Department', 'Salary', 'Normalized_Salary']].head(10))

# Custom Function on Movies
movie_df = pd.read_csv('movie.csv')

# Write a function that classifies movies based on duration
def classify_movie_length(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

# Apply the function to classify movies in the movie dataset
movie_df['Length_Classification'] = movie_df['duration'].apply(classify_movie_length)
print("\nMovie Dataset with Length_Classification column:")
print(movie_df[['movie_title', 'duration', 'Length_Classification']].head(10))
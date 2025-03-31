import sqlite3
import pandas as pd

# Inner Join on Chinook Database
conn = sqlite3.connect('chinook.db')
query = '''
SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) as TotalInvoices
FROM customers
INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
GROUP BY customers.CustomerId
'''
invoices_per_customer = pd.read_sql_query(query, conn)
print("Total number of invoices for each customer:")
print(invoices_per_customer)

# Outer Join on Movie Data
movie_df = pd.read_csv('movie.csv')
df1 = movie_df[['director_name', 'color']]
df2 = movie_df[['director_name', 'num_critic_for_reviews']]

# Perform a left join on director_name
left_join_df = pd.merge(df1, df2, on='director_name', how='left')
print("\nLeft join result:")
print(left_join_df)

# Perform a full outer join on director_name
outer_join_df = pd.merge(df1, df2, on='director_name', how='outer')
print("\nFull outer join result:")
print(outer_join_df)

# Count the number of rows in the resulting DataFrames for each join type
print("\nNumber of rows in the left join result:", len(left_join_df))
print("Number of rows in the full outer join result:", len(outer_join_df))
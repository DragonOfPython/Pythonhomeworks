import sqlite3

# Database Creation
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Define table schema
c.execute('''CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)''')

# Insert Data
books = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]

c.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', books)

# Update Data
c.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

# Query Data
c.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
dystopian_books = c.fetchall()
print(dystopian_books)

# Delete Data
c.execute("DELETE FROM Books WHERE Year_Published < 1950")

# Bonus Task
c.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
c.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
c.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
c.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

# Advanced Query
c.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
books_sorted_by_year = c.fetchall()
print(books_sorted_by_year)

conn.commit()
conn.close()
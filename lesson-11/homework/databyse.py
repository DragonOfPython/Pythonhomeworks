import sqlite3

# Database Creation
conn = sqlite3.connect('roster.db')
c = conn.cursor()

# Define table schema
c.execute('''CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)''')

# Insert Data
characters = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

c.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', characters)

# Update Data
c.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# Query Data
c.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajoran_characters = c.fetchall()
print(bajoran_characters)

# Delete Data
c.execute("DELETE FROM Roster WHERE Age > 100")

# Bonus Task
c.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
c.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
c.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
c.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

# Advanced Query
c.execute("SELECT * FROM Roster ORDER BY Age DESC")
sorted_characters = c.fetchall()
print(sorted_characters)

conn.commit()
conn.close()
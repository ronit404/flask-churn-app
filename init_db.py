import sqlite3

# Connect to the database. This command creates the 'database.db' file.
connection = sqlite3.connect('database.db')

# Create a cursor object, which allows us to execute SQL commands
cursor = connection.cursor()

# Define the SQL command to create our 'users' table
# This table will have three columns: an auto-incrementing id, a username, and a password.
# The username must be UNIQUE.
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
"""

# Execute the SQL command
cursor.execute(create_table_query)

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()

print("Database 'database.db' and 'users' table created successfully.")
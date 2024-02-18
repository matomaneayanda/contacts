import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Create a cursor to execute queries
cursor = conn.cursor()

# Open and read the SQL file
with open('your_sql_file.sql', 'r') as file:
    sql_queries = file.read()

# Split the SQL file content into individual queries
queries = sql_queries.split(';')

# Iterate over the queries and execute them
for query in queries:
    try:
        if query.strip() != '':
            cursor.execute(query)
            conn.commit()
            print("Query executed successfully!")
    except Exception as e:
        print("Error executing query:", str(e))

# Close the cursor and the database connection
cursor.close()
conn.close()
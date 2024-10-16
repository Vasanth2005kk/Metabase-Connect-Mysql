import mysql.connector
from mysql.connector import Error
import csv


# Database connection 
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'metabase_db'
}


movie_records = []

# Read the CSV file
with open('Datas and Query/movielens.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        movie_records.append(row)
        

movie_data=[]

for i in movie_records:
    movie_data_values = []
    for j in i.values():
        movie_data_values.append(j)
    movie_data.append(tuple(movie_data_values))



def update_movielens_datas(data):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            # SQL Update query

            update_query = """
            INSERT INTO Movielens
            (rownames, movieId, title, year, genres, userId, rating, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            
            # Execute the insert query for each row of data
            cursor.executemany(update_query, data)

            # Commit the transaction
            connection.commit()
            print(f"{cursor.rowcount} records inserted successfully.")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
     update_movielens_datas(movie_data)


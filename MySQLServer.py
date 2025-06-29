import mysql.connector
from mysql.connector import Error

try:
    # Step 1: Connect to MySQL Server (without selecting any database yet)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1604"  # Replace with your correct password
    )

    if mydb.is_connected():
        print("Connected to MySQL Server successfully!")

        # Step 2: Create a cursor
        cursor = mydb.cursor()

        # Step 3: Try creating the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

        except Error as e:
            print(f"Error while creating database: {e}")

        # Step 4: Close cursor
        cursor.close()

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Step 5: Close connection
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")

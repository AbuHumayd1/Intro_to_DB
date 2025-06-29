import mysql.connector

try:
    # Step 1: Connect to MySQL Server (without specifying a database)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1604"  # <-- Replace with your password
    )

    if mydb.is_connected():
        print("Connected to MySQL Server successfully!")

        # Step 2: Create a cursor
        cursor = mydb.cursor()

        # Step 3: Create the database (won't fail if it already exists)
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

        except mysql.connector.Error as e:
            print(f"Error while creating database: {e}")

        # Step 4: Close cursor
        cursor.close()

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Step 5: Close connection if it was opened
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")

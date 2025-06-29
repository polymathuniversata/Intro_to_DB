import mysql.connector

def create_database():
    """Create the alx_book_store database if it doesn't exist."""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            password="your_password"   # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        # Close cursor and connection properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()

import streamlit as st
import mysql.connector
import pandas as pd

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='VinitNotFound',
        password='jayjalaram',
        database='IPLManagement'
    )

# Function to insert data into Venues table
def insert_venue_data(venue_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL insert statement
        cursor.execute("INSERT INTO Venues (StadiumName, Capacity, Address, City, HomeTeamId) VALUES (%s, %s, %s, %s, %s)", venue_data)

        # Commit changes
        connection.commit()
        st.success("Venue data inserted successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to insert venue data: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch all records from the Venues table
def fetch_all_venues():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Venues")
        venues_data = cursor.fetchall()
        return venues_data
    except mysql.connector.Error as error:
        st.error(f"Failed to fetch venues data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch column names for the Venues table
def fetch_column_names_venues():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL query to fetch column names
        cursor.execute("SHOW COLUMNS FROM Venues")

        # Fetch all rows
        columns_data = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns_data]
        return column_names

    except mysql.connector.Error as error:
        print(f"Failed to fetch column names for Venues table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_venue_by_id(venue_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM venues WHERE VenueID = %s", (venue_id,))

        connection.commit()


    except mysql.connector.Error as error:
        print(f"Failed to delete venue: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
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

# Function to insert data into Points table
def insert_points_data(points_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL insert statement
        cursor.execute("INSERT INTO Points (Position, TeamId, TotalMatches, Wins, Loss, Result, NetRunRate) VALUES (%s, %s, %s, %s, %s, %s, %s)", points_data)

        # Commit changes
        connection.commit()
        st.success("Points data inserted successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to insert points data: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch all records from the Points table
def fetch_all_points():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM points")
        points_data = cursor.fetchall()
        return points_data
    except mysql.connector.Error as error:
        st.error(f"Failed to fetch venues data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch column names for the Points table
def fetch_column_names_points():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL query to fetch column names
        cursor.execute("SHOW COLUMNS FROM Points")

        # Fetch all rows
        columns_data = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns_data]
        return column_names

    except mysql.connector.Error as error:
        print(f"Failed to fetch column names for Points table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_points_by_id(points_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM venues WHERE PlayerID = %s", (points_id,))

        connection.commit()


    except mysql.connector.Error as error:
        print(f"Failed to delete points: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


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

# Function to insert data into Teams table
def insert_team_data(team_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL insert statement
        cursor.execute("INSERT INTO Teams (TeamName, Owner, Coach, Venue, Captain, Points, Wins, Lost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", team_data)

        # Commit changes
        connection.commit()
        st.success("Team data inserted successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to insert team data: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch all records from the Teams table
def fetch_all_teams():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Teams")
        teams_data = cursor.fetchall()
        return teams_data
    except mysql.connector.Error as error:
        st.error(f"Failed to fetch teams data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# Function to fetch column names for the Teams table
def fetch_column_names_teams():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL query to fetch column names
        cursor.execute("SHOW COLUMNS FROM Teams")

        # Fetch all rows
        columns_data = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns_data]
        return column_names

    except mysql.connector.Error as error:
        print(f"Failed to fetch column names for Teams table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_team_by_id(team_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM teams WHERE teamID = %s", (team_id,))

        connection.commit()


    except mysql.connector.Error as error:
        print(f"Failed to delete venue: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
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

# Function to insert data into Matches table
def insert_match_data(match_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL insert statement
        cursor.execute("INSERT INTO Matches (Status, Team1Id, Team1RunsMade, Team1OversPlayed, Team2Id, Team2RunsMade, Team2OversPlayed, Venue, Date, Time, Winner, ManOfTheMatch) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", match_data)

        # Commit changes
        connection.commit()
        st.success("Match data inserted successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to insert match data: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_match_by_id(match_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Matches WHERE MatchID = %s", (match_id,))

        connection.commit()


    except mysql.connector.Error as error:
        print(f"Failed to delete match: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Function to fetch column names for the Matches table
def fetch_column_names_matches():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL query to fetch column names
        cursor.execute("SHOW COLUMNS FROM Matches")

        # Fetch all rows
        columns_data = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns_data]
        return column_names

    except mysql.connector.Error as error:
        print(f"Failed to fetch column names for Matches table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch all records from the Matches table
def fetch_all_matches():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM matches")
        matches_data = cursor.fetchall()
        return matches_data
    except mysql.connector.Error as error:
        st.error(f"Failed to fetch venues data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


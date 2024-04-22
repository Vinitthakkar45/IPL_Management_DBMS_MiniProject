import streamlit as st
import mysql.connector
import pandas as pd

from teams import (
    fetch_all_teams,
    fetch_column_names_teams,
    insert_team_data,
    delete_team_by_id
)

from venues import (
    fetch_all_venues,
    fetch_column_names_venues,
    insert_venue_data,
    delete_venue_by_id
)

from players import (
    fetch_all_players,
    fetch_column_names_players,
    insert_player_data,
    delete_player_by_id
)

from matches import (
    fetch_all_matches,
    fetch_column_names_matches,
    insert_match_data,
    delete_match_by_id
)

from points import (
    fetch_all_points,
    fetch_column_names_points,
    insert_points_data,
    delete_points_by_id
)


# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='VinitNotFound',
        password='jayjalaram',
        database='IPLManagement'
    )




def main():
    st.title("IPL Management System")

    menu = ["Home", "Add Team Data", "Add Venue Data", "Add Player Data", "Add Match Data", "Add Points Data","About Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the IPL Management System!")
        st.markdown("---")
        st.write("Here, you can manage and analyze data related to the Indian Premier League (IPL).")
        st.write("Use the sidebar menu to navigate through different sections.")
        st.markdown("---")
        st.write("Get started by adding or viewing data on the following:")
        st.markdown("- **Teams**")
        st.markdown("- **Venues**")
        st.markdown("- **Players**")
        st.markdown("- **Matches**")
        st.markdown("- **Points**")

    elif choice == "Add Team Data":
        st.subheader("Add Team Data")
        # Add code to insert team data here
        # Input fields for team data
        team_name = st.text_input("Team Name", key="team_name_input")
        owner = st.text_input("Owner", key="owner_input")
        coach = st.text_input("Coach", key="coach_input")
        venue = st.number_input("Venue ID", min_value=1, key="venue_input")
        captain = st.number_input("Captain ID", min_value=1, key="captain_input")
        points = st.number_input("Points", min_value=0, key="points_input")
        wins = st.number_input("Wins", min_value=0, key="wins_input")
        lost = st.number_input("Lost", min_value=0, key="lost_input")

        # Button to insert team data
        if st.button("Insert Team Data"):
            team_data = (team_name, owner, coach, venue, captain, points, wins, lost)
            insert_team_data(team_data)

        # Delete team button
        st.subheader("Delete Team")
        team_id_to_delete = st.number_input("Enter Team ID to delete:", min_value=1)
        if st.button("Delete Team"):
            delete_team_by_id(team_id_to_delete)

        # Display all teams data in a table
        st.subheader("Existing Teams Data")
        teams_data = fetch_all_teams()
        if teams_data:
            column_names = fetch_column_names_teams()
            teams_df = pd.DataFrame(teams_data, columns=column_names)
            st.table(teams_df)
        else:
            st.write("No teams data available.")

    elif choice == "Add Venue Data":
        st.subheader("Add Venue Data")
        # Add code to insert venue data here
        # Input fields for venue data
        stadium_name = st.text_input("Stadium Name", key="stadium_name_input")
        capacity = st.number_input("Capacity", min_value=1, key="capacity_input")
        address = st.text_input("Address", key="address_input")
        city = st.text_input("City", key="city_input")
        home_team_id = st.number_input("Home Team ID", min_value=1, key="home_team_input")

    # Button to insert venue data
        if st.button("Insert Venue Data"):
            venue_data = (stadium_name, capacity, address, city, home_team_id)
            insert_venue_data(venue_data)

    # Delete venue button
        st.subheader("Delete Venue")
        venue_id_to_delete = st.number_input("Enter Venue ID to delete:", min_value=1)
        if st.button("Delete Venue"):
            delete_team_by_id(venue_id_to_delete)

    # Display all Venues data in a table
        st.subheader("Existing Venues Data")
        venues_data = fetch_all_venues()
        if venues_data:
            column_names = fetch_column_names_venues()
            venues_df = pd.DataFrame(venues_data, columns=column_names)
            st.table(venues_df)
        else:
            st.write("No venues data available.")


    elif choice == "Add Player Data":
        st.subheader("Add Player Data")
        # Add code to insert player data here
        # Input fields for player data
        player_name = st.text_input("Player Name", key="player_name_input")
        age = st.number_input("Age", min_value=0, key="age_input")
        team_id = st.number_input("Team ID", min_value=1, key="team_id_input")
        ipl_debut = st.date_input("IPL Debut", key="ipl_debut_input")
        specialization = st.text_input("Specialization", key="specialization_input")
        matches_played = st.number_input("Matches Played", min_value=0, key="matches_played_input")
        playing_style = st.text_input("Playing Style", key="playing_style_input")
        nationality = st.text_input("Nationality", key="nationality_input")

        # Button to insert player data
        if st.button("Insert Player Data"):
            # Validate input
            if not player_name or not specialization or not playing_style or not nationality:
                st.error("Please fill in all required fields")
            else:
                player_data = (player_name, age, team_id, ipl_debut, specialization, matches_played, playing_style, nationality)
                insert_player_data(player_data)

        # Delete player button
        st.subheader("Delete Player")
        player_id_to_delete = st.number_input("Enter Player ID to delete:", min_value=1)
        if st.button("Delete Player"):
            delete_player_by_id(venue_id_to_delete)
        
        # Display all players data in a table
        st.subheader("Existing Players Data")
        players_data = fetch_all_players()
        if players_data:
            column_names = fetch_column_names_players()
            players_df = pd.DataFrame(players_data, columns=column_names)
            st.table(players_df)
        else:
            st.write("No players data available.")


    elif choice == "Add Match Data":
        st.subheader("Add Match Data")
        # Add code to insert match data here
        # Input fields for match data
        status = st.selectbox("Status", ["Upcoming", "Past"], key="status_input")
        team1_id = st.number_input("Team 1 ID", min_value=1, key="team1_id_input")
        team1_runs_made = st.number_input("Team 1 Runs Made", min_value=0, key="team1_runs_made_input")
        team1_overs_played = st.number_input("Team 1 Overs Played", min_value=0, key="team1_overs_played_input")
        team2_id = st.number_input("Team 2 ID", min_value=1, key="team2_id_input")
        team2_runs_made = st.number_input("Team 2 Runs Made", min_value=0, key="team2_runs_made_input")
        team2_overs_played = st.number_input("Team 2 Overs Played", min_value=0, key="team2_overs_played_input")
        venue_match = st.number_input("Venue ID", min_value=1, key="venue_match_input")
        match_date = st.date_input("Match Date", key="match_date_input")
        match_time = st.time_input("Match Time", key="match_time_input")
        winner = st.number_input("Winner Team ID", min_value=1, key="winner_input")
        man_of_the_match = st.number_input("Man of the Match Player ID", min_value=1, key="man_of_the_match_input")
        if st.button("Insert Match Data"):
            match_data = (status, team1_id, team1_runs_made, team1_overs_played, team2_id, team2_runs_made, team2_overs_played, venue_match, match_date, match_time, winner, man_of_the_match)
            insert_match_data(match_data)

         # Delete match button
        st.subheader("Delete Match")
        match_id_to_delete = st.number_input("Enter Match ID to delete:", min_value=1)
        if st.button("Delete Match"):
            delete_match_by_id(match_id_to_delete)

        # Display all matches data in a table
        st.subheader("Existing Matches Data")
        matches_data = fetch_all_matches()
        if matches_data:
            column_names = fetch_column_names_matches()
            matches_df = pd.DataFrame(matches_data, columns=column_names)
            st.table(matches_df)
        else:
            st.write("No matches data available.")
        
   
    elif choice == "Add Points Data":
        st.subheader("Add Points Data")
        # Add code to insert points data here
        # Input fields for points data
        position = st.number_input("Position", min_value=1, key="position_input")
        team_id_points = st.number_input("Team ID", min_value=1, key="team_id_points_input")
        total_matches = st.number_input("Total Matches", min_value=0, key="total_matches_input")
        wins_points = st.number_input("Wins", min_value=0, key="wins_points_input")
        loss = st.number_input("Loss", min_value=0, key="loss_input")
        result = st.text_input("Result", key="result_input")
        net_run_rate = st.number_input("Net Run Rate", key="net_run_rate_input")
        if st.button("Insert Points Data"):
            points_data = (position, team_id_points, total_matches, wins_points, loss, result, net_run_rate)
            insert_points_data(points_data)

        # Delete player button
        st.subheader("Delete Point")
        point_id_to_delete = st.number_input("Enter Point ID to delete:", min_value=1)
        if st.button("Delete Player"):
            delete_points_by_id(point_id_to_delete)

        # Display all points data in a table
        st.subheader("Existing Points Data")
        points_data = fetch_all_points()
        if points_data:
            column_names = fetch_column_names_points()
            points_df = pd.DataFrame(points_data, columns=column_names)
            st.table(points_df)
        else:
            st.write("No points data available.")

    elif choice == "About Us":
        st.subheader("About Us")
        st.write("Welcome to our IPL Management System!")
        st.write("We are passionate developers dedicated to bringing you the best experience in managing IPL data.")
        
        st.write("Meet the Team:")
        st.markdown("- **Vinit Thakkar**")
        st.image("C:\Semester 4\DBMS\Project\IPL Management\Vinit.jpg", caption="Vinit", width=400)
        st.markdown("- **Vrutansh**")




    
if __name__ == "__main__":
    main()

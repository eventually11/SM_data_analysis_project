# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:08:14 2024

@author: Administrator
"""

from open_street_map_API import OpenStreetMapAPI
import sqlite3
import os

def save_to_sqlite(df, db_name, table_name):
    """
    Saves the DataFrame to an SQLite database.

    Parameters
    ----------
    df : DataFrame
        The Pandas DataFrame containing the place details.
    db_name : str
        The name of the SQLite database file.
    table_name : str
        The name of the table to store the data.
    """
    # Get the current script directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Combine the directory with the database name
    db_path = os.path.join(current_directory, db_name)

    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
        
        
if __name__ == "__main__":
    query = 'restaurant'  # Search keyword
    latitude = -12.4634  # Latitude of Darwin
    longitude = 130.8456  # Longitude of Darwin
    radius = 1  # Search radius in degrees 

    osm_api = OpenStreetMapAPI()
    places = osm_api.get_places(query, latitude, longitude, radius)

    if places:
        print("Restaurants found:")
        df_restaurants = osm_api.convert_to_dataframe(places)
        print(df_restaurants)
        save_to_sqlite(df_restaurants, 'places.db', 'restaurants')
        print("Data saved to SQLite database 'places.db' in the table 'restaurants'.")
    else:
        print("Failed to retrieve restaurants")

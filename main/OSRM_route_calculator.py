# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:32:29 2024

@author: Administrator
"""

import requests

class OSRMRouteCalculator:
    def __init__(self, start_lat, start_lng, end_lat, end_lng):
        self.start_lat = start_lat
        self.start_lng = start_lng
        self.end_lat = end_lat
        self.end_lng = end_lng
        self.url = f"http://router.project-osrm.org/route/v1/driving/{start_lng},{start_lat};{end_lng},{end_lat}?overview=false"

    def get_route_info(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            route = data['routes'][0]
            distance = route['distance'] / 1000  # Convert to kilometers
            duration = route['duration'] / 60    # Convert to minutes
            return distance, duration
        else:
            return None, None

if __name__ == "__main__":
    # Set start and end coordinates
    start_lat, start_lng = 39.9087, 116.3975
    end_lat, end_lng = 39.9163, 116.3971

    # Create an instance of the calculator
    calculator = OSRMRouteCalculator(start_lat, start_lng, end_lat, end_lng)
    
    # Get route information
    distance, duration = calculator.get_route_info()
    
    if distance is not None and duration is not None:
        print(f"Distance: {distance:.2f} km")
        print(f"Duration: {duration:.2f} minutes")
    else:
        print("Request failed")

# Title: ISS Tracking Website
# File: Open Notify API File
# Date: July 2023
# Author: Nick Mast
#
# This file accesses the 'Open Notify' API and the 'Where is the ISS AT?' API to get all of our statistics listed on the site.
import requests

# This class contains the methods to get ISS data from the Open Notify API
class notify:
    # This method gets the latitude and longitude of the ISS and returns them in float form
    def get_position():
        # Use the requests package to access the API
        response = requests.get('http://api.open-notify.org/iss-now.json')
        # Get latitude and longitude and store them into their respectable variables
        latitude = response.json()['iss_position']['latitude']
        longitude = response.json()['iss_position']['longitude']
        # Return the variables
        return float(latitude), float(longitude)
    # This method gets a list of the astronauts currently on the ISS and returns them
    def astronauts():
        # Use the requests package to access the API
        response = requests.get('http://api.open-notify.org/astros.json')
        # Filter out the astronauts names from the JSON response
        temp = response.json()['people']
        # Create list to store the astronauts
        people = []
        # Loop to add all the astronauts to the list
        for i in temp:
            people.append(i['name'])
            # Return the list
        return people
    
# This class contains the methods to get ISS data from the Where is the ISS AT? API
class wtISSat:
    # This method gets the altitude and velocity and returns them
    def get_info():
        # Use the requests package to access the API
        response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
        # Get altitude and velocity and store them into their respectable variables
        altitude = response.json()['altitude']
        velocity = response.json()['velocity']
        # Return the variables
        return altitude, velocity
    

# Title: ISS Tracking Website
# File: Google Map File
# Date: July 2023
# Author: Nick Mast
#
# This file gets the image we use on the map for the ISS and creates the actual map you see on the screen.  The map is stored in the static folder.
# To create the map this file uses the openNotify.py file and the gmplot API.
import gmplot
import openNotify

# Method to plot the position of the iss on a google map
def getPos():
    # Call our get_position method in our openNotify file to get the latitude and longitude from the open Notify API
    latitude, longitude = openNotify.notify.get_position()
    # Create the instance of our Google Map Plotter using our latitude, longitude, and zoom level
    gmap = gmplot.GoogleMapPlotter(latitude, longitude, 4)

    # Get the image we are going to use to represent the ISS on our map
    iss_image = 'https://openclipart.org/download/211230/iss-silhouette.svg'
    # Create the bounds for our image
    bounds = {'north':latitude + 2, 'south': (latitude - 2), 'east': longitude + 2, 'west': (longitude - 2)}

    # Draw the image on our map within the bounds
    gmap.ground_overlay(iss_image, bounds)
    # Create our map in an html file and store it in the templates folder
    gmap.draw('static/map.html')
    # return our latitude and longitude
    return latitude, longitude
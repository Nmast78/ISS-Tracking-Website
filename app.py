# Title: ISS Tracking Website
# File: Main App File
# Date: July 2023
# Author: Nick Mast
#
# This is an website where users can track the International Space Station.  Users can view statistics like latitude, longitude, velocity, and more.
# The user can also see a list of all the astronauts currently on the ISS and interact with the google map on the right side of the page.

from flask import Flask, render_template
import map, openNotify

# Create the flask app
app = Flask(__name__)

# The application page
@app.route("/")
def hello_world():
    # Get latitude and longitude from our map.py file
    latitude, longitude = map.getPos()
    # Get a list of all astronauts on the ISS from our openNotity.py file
    people = openNotify.notify.astronauts()
    # Get altitude and velocity from our openNotify.py file
    altitude, velocity = openNotify.wtISSat.get_info()
    # Render our home.html file with all of the parameters we created above
    return render_template('home.html', latitude=latitude, longitude=longitude, people=people, altitude=altitude, velocity=velocity)

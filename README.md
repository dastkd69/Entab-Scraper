# Entab-Scraper
This is a script that automates the process of opening your browser, opening entab (in this case donboscocampuscare.in) and logging in. 

Please note that this script uses pyAutoGUI and therefore renders your device uselesss for as long as the script is running (wont take long, infact after getting past the login screen u can probably resume other activities, DONT CLOSE THE BROWSER THOUGH!)

# Usage
1) Clone this repository/ download the zip.
2) Unzip it and open command prompy/ terminal in the folder.
3) Enter python3 -m pip install -r requirements.txt (Python installation required, preferably python 3)
4) Enter python3 entabScript.py

# RoadMap
Following features will be added:
1) Automatically scrape through homework section and assignments and dump them to a file which can be viewed later as entab loses its data after 5 days.
2) Automatically create multiple files for an organised list of tasks

# Plan-On (Might not be added)
1) Not waiting for the browser to open , login and do the styuff (turn it into a background process).
2) Automatically update submission deadlines on Google Calendar
3) You tell me! :)

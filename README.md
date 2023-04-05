# Uski
Spotify to youtube playlist migrator

Prerequisites: Spotipy, PyQt5, Google Auth Libraries
Download all of the files within the repo
Create a project within Google Cloud Console (must be for Desktop Application), enable the YouTube Data v3 API and create credentials for a Client.
Download client_secret.json and place into the right file path (as indicated in the program). Copy the Client ID and Client Secret and replace the lines 40-41.
Add your email to the 'testing users' category of the project


How to run:

1) Open python files within an IDE such as VScode
2) Run the uski_gui.py file
3) GUI will open, enter the required information
4) Enter a playlist you want to replicate within YouTube, press the Enter Button (a text file will be made with the playlist id)
5) Click the 'Create Playlist' Button
6) The program will prompt the user to sign in
7) User signs in with email from 'testing users' page on console 
8) The window will say - authorization flow granted
9) After waiting 1 - 2 minutes, the playlist will be created on the users YT 

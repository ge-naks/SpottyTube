from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5 import QtCore
import sys
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle('Uski')

        # Setting the icon
        self.setWindowIcon(QIcon('C:/College/Year 2022-2023/cs projects/Uski/icon/uski_icon.png'))

        # Setting the color
        self.setStyleSheet("background-color: #333333")

        # Create a label
        label = QLabel('Uski - Spotify to YouTube Playlist Migrator')

        # Setting the font
        label.setFont(QFont('Arial', 10, QFont.Bold))
        label.setStyleSheet("color: rgb(255, 255, 255);")

        # Align the label to the top center of the window
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Create a layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Create a line edit widget for the user to enter a Spotify link
        self.spotify_link_edit = QLineEdit()
        layout.addWidget(self.spotify_link_edit)

        # Create a button that prints the text in the line edit to the console
        button = QPushButton('Enter', self)
        button.setToolTip('Click to get the Spotify link')
        button.setFont(QFont('Arial', 10, QFont.Bold))
        button.setStyleSheet("color: rgb(255, 255, 255);")
        button.clicked.connect(self.get_spotify_link)
        layout.addWidget(button)

        # Set the main layout for the window
        self.setLayout(layout)

        # set the size and position of the window (left, top, width, height)
        # first two params are x,y coords of top left of box
        self.setGeometry(500, 100, 800, 600)

        # adding a button :)
        button = QPushButton('Test Button', self)
        button.setToolTip('This is an example button')
        button.setFont(QFont('Arial', 10, QFont.Bold))
        button.setStyleSheet("color: rgb(255, 255, 255);")
        # parameters x and y coordinataes
        button.move(320,450)
        button.resize(150, 50)

        # importing a picture
        newLabel = QLabel(self)
        pixmap = QPixmap('C:/College/Year 2022-2023/cs projects/Uski/icon/uski_icon_window.png')
        newLabel.setPixmap(pixmap)

        # moving the image around the background
        newLabel.move(260,50)

        # resizing the image
        newLabel.resize(pixmap.width(), pixmap.height()) # 545 x 300

        # scaling the image
        scaled_pixmap = pixmap.scaled(272, 140, QtCore.Qt.KeepAspectRatio) # aspect ratio is kept and image can be shrunk or increased
        newLabel.setPixmap(scaled_pixmap)

        create_playlist_button = QPushButton('Create Playlist', self)
        create_playlist_button.setGeometry(100, 220, 200, 30)
        create_playlist_button.clicked.connect(self.create_playlist)

    gui_playlist_id = None

    @pyqtSlot()
    def get_spotify_link(self):
        global gui_playlist_id
        # Get the text in the Spotify link edit and print it to the console
        spotify_link = self.spotify_link_edit.text()
        # Gets the playlist ID from the link and storing it into playlist_id
        gui_playlist_id = spotify_link.split('/')[-1].split('?')[0]
        print(f'Playlist ID: {gui_playlist_id}')

        with open('playlist_id.txt', 'w') as f:
            if gui_playlist_id is not None:
                f.write(gui_playlist_id)

    def create_playlist(self):
        # Run the main.py file using the subprocess module
        subprocess.run(["python", "main.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
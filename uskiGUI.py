from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5 import QtCore
import sys

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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
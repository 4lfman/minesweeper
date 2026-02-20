import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

def start_game():
    print("Let the games begin!")

class Window(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        width = 400
        height = width
        self.setFixedSize(width,height)

        self.setWindowTitle("Minesweeper!")

        self.label = QLabel("Welcome to Minesweeper!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.button = QPushButton("Start game")
        self.button.clicked.connect(start_game)
        self.button.setFixedHeight(50)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.main_widget.setLayout(layout)

        #window.show()
        #width = 400
        #window = QWidget()
        #window.setWindowTitle("Minesweeper!")
        #window.setFixedWidth(width)
        #window.setFixedHeight(width)

        #label = QLabel("Welcome to Minesweeper!")
        #label.setAlignment(QtCore.Qt.AlignCenter)

        #button = QPushButton("Start game")
        #button.clicked.connect(start_game)
        #button.setFixedHeight(50)

        #layout = QVBoxLayout()
        #layout.addWidget(label)
        #layout.addWidget(button)

        #window.setLayout(layout)

        #window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())

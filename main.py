import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

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

class Minesweeper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.setWindowTitle("The game has begun!")

        self.UiComponents()
        
        width = 400
        height = width
        self.setFixedSize(width,height)

        self.show()

    def UiComponents(self):
        self.turn = 0
        
        # Square map side length
        self.gridSize = 6
        
        # Add pressable buttons
        mapGrid = QGridLayout()
        self.buttonList = []
        for i in range(self.gridSize):
            innerList = []
            for j in range(self.gridSize):
                tmpBtn = QPushButton()
                innerList.append(tmpBtn)
                mapGrid.addWidget(tmpBtn, i, j)

            self.buttonList.append(innerList)
       
        self.main_widget.setLayout(mapGrid) 

        # Add functionality to the buttons
        x = 90
        y = 90
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                #self.buttonList[i][j].setGeometry(x*i + 20,
                #                                  y*j + 20,
                #                                  80, 80)
                self.buttonList[i][j].clicked.connect(self.actionCalled)
                self.buttonList[i][j].setFont(QFont(QFont("Times", 25)))

        # Button to reset the game to the starting position
        resetButton = QPushButton()
        resetButton.clicked.connect(self.resetGame)
        resetButton.setText("Reset Game")
        mapGrid.addWidget(resetButton, self.gridSize, 0, 1, self.gridSize)

    # Called when a field is pressed
    def actionCalled(self):
        self.turn += 1

        button = self.sender()

        button.setEnabled(False)
        button.setText("X")

    def resetGame(self):
        self.turn = 0

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttonList[i][j].setText("")
                self.buttonList[i][j].setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Minesweeper()
    #window = Window()
    window.show()
    sys.exit(app.exec_())

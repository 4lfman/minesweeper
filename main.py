import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

import math
import numpy as np

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
        # Square map side length
        self.gridSize = 6

        self.turn = 0
        self.nbrMines = 5
        self.mines = self.selectMineLocations(self. gridSize, self.nbrMines)
        
        # Add pressable buttons
        mapGrid = QGridLayout()
        self.buttonList = []
        for i in range(self.gridSize):
            innerList = []
            for j in range(self.gridSize):
                tmpBtn = QPushButton()
                tmpBtn.x = i
                tmpBtn.y = j
                innerList.append(tmpBtn)
                mapGrid.addWidget(tmpBtn, i, j)

            self.buttonList.append(innerList)
       
        self.main_widget.setLayout(mapGrid) 

        # Add functionality to the buttons
        x = 90
        y = 90
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttonList[i][j].clicked.connect(self.actionCalled)
                self.buttonList[i][j].setFont(QFont(QFont("Times", 20)))

        # Button to reset the game to the starting position
        resetButton = QPushButton()
        resetButton.clicked.connect(self.resetGame)
        resetButton.setText("Reset Game")
        mapGrid.addWidget(resetButton, self.gridSize, math.ceil(self.gridSize/2), 3, math.floor(self.gridSize/2))

        # Turnlabel
        self.turnLabel = QLabel("Turn: 0")
        mapGrid.addWidget(self.turnLabel, self.gridSize, 0, 3, math.floor(self.gridSize/2))

    # Called when a field is pressed
    def actionCalled(self):
        self.turn += 1
        self.turnLabel.setText(f"Turn: {self.turn}")

        button = self.sender()
        button.setEnabled(False)

        if (button.x,button.y) in self.mines:
            self.mineClicked(button)
        else:
            button.setText(f'{self.adjacentMines(button)}')
            self.winCheck()



    def resetGame(self):
        self.setWindowTitle("The game has begun!")
        self.turn = 0
        self.turnLabel.setText(f"Turn: {self.turn}")

        self.mines = self.selectMineLocations(self.gridSize, self.nbrMines)

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttonList[i][j].setText("")
                self.buttonList[i][j].setEnabled(True)
                
    def mineClicked(self, button):
        button.setText("Boom")
        self.setWindowTitle("You lost! Reset the game to try again")

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttonList[i][j].setEnabled(False)

    def adjacentMines(self, button):
        c = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for direction in directions:
            if((button.x+direction[0], button.y+direction[1]) in self.mines):
                c+=1
        return c

    def selectMineLocations(self, gridSize, nbrMines):
        mines = []
        
        while len(mines)<nbrMines:
            newMine = (np.random.randint(0, gridSize), np.random.randint(0,gridSize)) 
            if newMine not in mines:
                mines.append(newMine)

        return mines

    def winCheck(self):
        if self.turn != self.gridSize**2 - self.nbrMines:
            return

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttonList[i][j].setEnabled(False)

        self.setWindowTitle("You won! Press reset to play again")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Minesweeper()
    window.show()
    sys.exit(app.exec_())

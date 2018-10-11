import readchar
from os import system


class Setup():
    def __init__(self, puzzle):
        self.selectedColumn = 0
        self.selectedRow = 0
        self.puzzle = puzzle

    def runSetup(self):
        while True:
            system('clear')

            self.puzzle.print({'column': self.selectedColumn,
                               'row': self.selectedRow})
            print("Enter the known values for the puzzle. Use arrow keys to move, type number 0-9 to set. Press Q when finished.")

            key = readchar.readkey()

            if key == "q" or key == "Q":
                return
            elif key == readchar.key.UP:
                self.move("UP")
            elif key == readchar.key.DOWN:
                self.move("DOWN")
            elif key == readchar.key.RIGHT:
                self.move("RIGHT")
            elif key == readchar.key.LEFT:
                self.move("LEFT")
            else:
                try:
                    value = int(key)
                    self.puzzle.setValue(
                        self.selectedColumn, self.selectedRow, value)
                except ValueError:
                    print("I didn't understand that, try again")

    def move(self, direction):
        if direction == "UP":
            if self.selectedRow > 0:
                self.selectedRow -= 1
        elif direction == "RIGHT":
            if self.selectedColumn < 8:
                self.selectedColumn += 1
        elif direction == "DOWN":
            if self.selectedRow < 8:
                self.selectedRow += 1
        elif direction == "LEFT":
            if self.selectedColumn > 0:
                self.selectedColumn -= 1

def newPuzzle():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


class Sudoku:
    puzzle = newPuzzle()
    posX = 0
    posY = 0

    def setValue(self, value):
        if value < 0 or value > 9:
            return False

        self.puzzle[self.posX][self.posY] = value

    def move(self, direction):
        if direction == "UP":
            if self.posX < 8:
                self.posX += 1
        elif direction == "RIGHT":
            if self.posY < 8:
                self.posY += 1
        elif direction == "DOWN":
            if self.posX > 0:
                self.posX -= 1
        elif direction == "LEFT":
            if self.posY > 0:
                self.posY -= 1

    def print(self):
        print(self.posX, self.posY, "Current value:",
              self.puzzle[self.posX][self.posY])

def newPuzzle():
  puzzle = []

  for i in range(9):
    puzzle.append([])
    for _ in range(9):
      puzzle[i].append({"value": None, "options": [1,2,3,4,5,6,7,8,9]})
  
  return puzzle

def easyPuzzle():
  return [
        [{"value": 2, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 5, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 5, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 9, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 9, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 7, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 9, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 5, "options": [1,2,3,4,5,6,7,8,9]}]
    ]

def mediumPuzzle():
    return [
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 9, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 7, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 5, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 3, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 1, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 6, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 7, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 4, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 9, "options": [1,2,3,4,5,6,7,8,9]}],
        [{"value": 9, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 8, "options": [1,2,3,4,5,6,7,8,9]}, {"value": 2, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}, {"value": None, "options": [1,2,3,4,5,6,7,8,9]}]
    ]


class Sudoku:
    def __init__(self):
      # self.puzzle = newPuzzle()
      # self.puzzle = easyPuzzle()
      self.puzzle = mediumPuzzle()
      self.selectedColumn = 0
      self.selectedRow = 0

    def setValue(self, value):
        if value < 0 or value > 9:
            return False

        self.puzzle[self.selectedColumn][self.selectedRow]['value'] = value
        return value

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

    def print(self, printOptions):
        output = "====================================================================\n" if printOptions else "=========================================\n"

        for row in range(9):
            for column in range(9):
                output += "||" if column % 3 == 0 else "|"
                output += "=" if column == self.selectedColumn and row == self.selectedRow else " "
                output += f"{self.puzzle[column][row]['value']}" if self.puzzle[column][row]['value'] != None else " "
                output += f"({len(self.puzzle[column][row]['options'])})" if printOptions else ""
                output += "=" if column == self.selectedColumn and row == self.selectedRow else " "

            output += "||\n"

            if row % 3 == 2:
                output += "====================================================================\n" if printOptions else "=========================================\n"
            else:
                output += "--------------------------------------------------------------------\n" if printOptions else "-----------------------------------------\n"

        print(output)

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

    def setValue(self, column, row, value):
        if value < 0 or value > 9:
            return False

        self.puzzle[column][row]['value'] = value
        return value

    def print(self, highlight = None):
        output = "=========================================\n"

        for row in range(9):
            for column in range(9):
                output += "||" if column % 3 == 0 else "|"
                output += "=" if highlight != None and column == highlight['column'] and row == highlight['row'] else " "
                output += f"{self.puzzle[column][row]['value']}" if self.puzzle[column][row]['value'] != None else " "
                output += ""
                output += "=" if highlight != None and column == highlight['column'] and row == highlight['row'] else " "

            output += "||\n"

            if row % 3 == 2:
                output += "=========================================\n"
            else:
                output += "-----------------------------------------\n"

        print(output)

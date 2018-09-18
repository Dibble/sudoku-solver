import math


class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        i = 1
        isSolved = False

        while isSolved != True and i < 1000:
            self.updateOptions()
            print(f"iteration {i}")

            i += 1
            isSolved = self.isSolved()

        return isSolved, i - 1

    def isSolved(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j]['value'] == None:
                    return False

        return True

    def updateOptions(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j]['value'] != None:
                    continue

                rowValues = self.__getRowValues__(j)
                columnValues = self.__getColumnValues__(i)
                squareValues = self.__getSquareValues__(i, j)

                rowAndColumnValues = rowValues + \
                    list(set(columnValues) - set(rowValues))
                allValues = rowAndColumnValues + \
                    list(set(squareValues) - set(rowAndColumnValues))

                self.__removeOptions__(i, j, allValues)

                if len(self.puzzle[i][j]['options']) == 1:
                    self.puzzle[i][j]['value'] = self.puzzle[i][j]['options'][0]
                    print(f"Solved [{i}][{j}]: {self.puzzle[i][j]['value']}")

    def __getRowValues__(self, row):
        rowValues = []
        for col in range(9):
            if self.puzzle[col][row]['value'] != None:
                rowValues.append(self.puzzle[col][row]['value'])
        return rowValues

    def __getColumnValues__(self, col):
        columnValues = []
        for row in range(9):
            if self.puzzle[col][row]['value'] != None:
                columnValues.append(self.puzzle[col][row]['value'])
        return columnValues

    def __removeOptions__(self, col, row, options):
        for val in options:
            try:
                self.puzzle[col][row]['options'].remove(val)
            except ValueError:
                continue

    def __getSquareValues__(self, col, row):
        squareValues = []
        squareX = math.floor(col / 3)
        squareY = math.floor(row / 3)

        for i in range(3):
            for j in range(3):
                x = squareX * 3 + i
                y = squareY * 3 + j

                if self.puzzle[x][y]['value'] != None:
                    squareValues.append(self.puzzle[x][y]['value'])

        return squareValues

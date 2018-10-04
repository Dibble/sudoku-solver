import math


class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        i = 1
        isSolved = False

        while isSolved != True and i < 1000:
            self.updateOptions()
            # self.findUniqueOptions()
            self.fillSingles()

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
        for column in range(9):
            for row in range(9):
                if self.puzzle[column][row]['value'] != None:
                    continue

                rowValues = self.__getRowValues__(row)
                columnValues = self.__getColumnValues__(column)
                squareValues = self.__getSquareValues__(column, row)

                rowAndColumnValues = rowValues + \
                    list(set(columnValues) - set(rowValues))
                allValues = rowAndColumnValues + \
                    list(set(squareValues) - set(rowAndColumnValues))

                self.__removeOptions__(column, row, allValues)

                if len(self.puzzle[column][row]['options']) == 1:
                    self.puzzle[column][row]['value'] = self.puzzle[column][row]['options'][0]
                    print(
                        f"Update Options solved [{column}][{row}]: {self.puzzle[column][row]['value']}")

    def findUniqueOptions(self):
        for column in range(9):
            for row in range(9):
                if self.puzzle[column][row]['value'] != None:
                    continue

                rowOptions = self.__getRowOptions__(row)
                for rowOption in range(9):
                    if rowOptions[rowOption] == 1:
                        self.puzzle[column][row]['value'] = rowOption + 1
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle[column][row]['value']}")
                        break

                columnOptions = self.__getColumnOptions__(column)
                for columnOption in range(9):
                    if columnOptions[columnOption] == 1:
                        self.puzzle[column][row]['value'] = columnOption + 1
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle[column][row]['value']}")
                        break

                squareOptions = self.__getSquareOptions__(column, row)
                for squareOption in range(9):
                    if squareOptions[squareOption] == 1:
                        self.puzzle[column][row]['value'] = squareOption + 1
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle[column][row]['value']}")
                        break

    def fillSingles(self):
        for row in range(9):
            rowSum = 0
            emptyCells = 0
            emptyColumn = None
            for col in range(9):
                if self.puzzle[col][row]['value'] != None:
                    rowSum += self.puzzle[col][row]['value']
                else:
                    emptyCells += 1
                    emptyColumn = col

            if emptyCells == 1:
                self.puzzle[emptyColumn][row]['value'] = 45 - rowSum
                print(
                    f"Fill Single Row solved [{emptyColumn}][{row}]: {self.puzzle[emptyColumn][row]['value']}")

        for col in range(9):
            columnSum = 0
            emptyCells = 0
            emptyRow = None
            for row in range(9):
                if self.puzzle[col][row]['value'] != None:
                    columnSum += self.puzzle[col][row]['value']
                else:
                    emptyCells += 1
                    emptyRow = row

            if emptyCells == 1:
                self.puzzle[col][emptyRow]['value'] = 45 - columnSum
                print(
                    f"Fill Single Col solved [{col}][{emptyRow}]: {self.puzzle[col][emptyRow]['value']}")

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

    def __getRowOptions__(self, row):
        rowOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for col in range(9):
            for option in range(len(self.puzzle[col][row]['options'])):
                rowOptions[option - 1] += 1
        return rowOptions

    def __getColumnOptions__(self, col):
        columnOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in range(9):
            for option in range(len(self.puzzle[col][row]['options'])):
                columnOptions[option - 1] += 1
        return columnOptions

    def __getSquareOptions__(self, col, row):
        squareOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squareX = math.floor(col / 3)
        squareY = math.floor(row / 3)

        for i in range(3):
            for j in range(3):
                x = squareX * 3 + i
                y = squareY * 3 + j

                for option in range(len(self.puzzle[x][y]['options'])):
                    squareOptions[option - 1] += 1

        return squareOptions

    def __removeOptions__(self, col, row, options):
        for val in options:
            try:
                self.puzzle[col][row]['options'].remove(val)
            except ValueError:
                continue

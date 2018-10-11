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
                if not self.puzzle.hasValue(i, j):
                    return False

        return True

    def updateOptions(self):
        for column in range(9):
            for row in range(9):
                if self.puzzle.hasValue(column, row):
                    continue

                rowValues = self.__getRowValues__(row)
                columnValues = self.__getColumnValues__(column)
                squareValues = self.__getSquareValues__(column, row)

                rowAndColumnValues = rowValues + \
                    list(set(columnValues) - set(rowValues))
                allValues = rowAndColumnValues + \
                    list(set(squareValues) - set(rowAndColumnValues))

                self.__removeOptions__(column, row, allValues)

                if self.puzzle.numberOfOptions(column, row) == 1:
                    self.puzzle.setValue(
                        column, row, self.puzzle.getOptions(column, row)[0])
                    print(
                        f"Update Options solved [{column}][{row}]: {self.puzzle.getValue(column, row)}")

    def findUniqueOptions(self):
        for column in range(9):
            for row in range(9):
                if self.puzzle.hasValue(column, row):
                    continue

                rowOptions = self.__getRowOptions__(row)
                for rowOption in range(9):
                    if rowOptions[rowOption] == 1:
                        self.puzzle.setValue(column, row, rowOption + 1)
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle.getValue(column, row)}")
                        break

                columnOptions = self.__getColumnOptions__(column)
                for columnOption in range(9):
                    if columnOptions[columnOption] == 1:
                        self.puzzle.setValue(column, row, columnOption + 1)
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle.getValue(column, row)}")
                        break

                squareOptions = self.__getSquareOptions__(column, row)
                for squareOption in range(9):
                    if squareOptions[squareOption] == 1:
                        self.puzzle.setValue(column, row, squareOption + 1)
                        print(
                            f"Find Unique Options solved [{column}][{row}]: {self.puzzle.getValue(column, row)}")
                        break

    def fillSingles(self):
        for row in range(9):
            rowSum = 0
            emptyCells = 0
            emptyColumn = None
            for column in range(9):
                if self.puzzle.hasValue(column, row):
                    rowSum += self.puzzle.getValue(column, row)
                else:
                    emptyCells += 1
                    emptyColumn = column

            if emptyCells == 1:
                self.puzzle.setValue(emptyColumn, row, 45 - rowSum)
                print(
                    f"Fill Single Row solved [{emptyColumn}][{row}]: {self.puzzle.getValue(emptyColumn, row)}")

        for column in range(9):
            columnSum = 0
            emptyCells = 0
            emptyRow = None
            for row in range(9):
                if self.puzzle.hasValue(column, row):
                    columnSum += self.puzzle.getValue(column, row)
                else:
                    emptyCells += 1
                    emptyRow = row

            if emptyCells == 1:
                self.puzzle.setValue(column, emptyRow, 45 - columnSum)
                print(
                    f"Fill Single Col solved [{column}][{emptyRow}]: {self.puzzle.getValue(column, emptyRow)}")

    def __getRowValues__(self, row):
        rowValues = []
        for column in range(9):
            if self.puzzle.hasValue(column, row):
                rowValues.append(self.puzzle.getValue(column, row))
        return rowValues

    def __getColumnValues__(self, column):
        columnValues = []
        for row in range(9):
            if self.puzzle.hasValue(column, row):
                columnValues.append(self.puzzle.getValue(column, row))
        return columnValues

    def __getSquareValues__(self, column, row):
        squareValues = []
        squareX = math.floor(column / 3)
        squareY = math.floor(row / 3)

        for i in range(3):
            for j in range(3):
                x = squareX * 3 + i
                y = squareY * 3 + j

                if self.puzzle.hasValue(x, y):
                    squareValues.append(self.puzzle.getValue(x, y))

        return squareValues

    def __getRowOptions__(self, row):
        rowOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for column in range(9):
            for option in range(self.puzzle.numberOfOptions(column, row)):
                rowOptions[option - 1] += 1
        return rowOptions

    def __getColumnOptions__(self, column):
        columnOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in range(9):
            for option in range(self.puzzle.numberOfOptions(column, row)):
                columnOptions[option - 1] += 1
        return columnOptions

    def __getSquareOptions__(self, column, row):
        squareOptions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squareX = math.floor(column / 3)
        squareY = math.floor(row / 3)

        for i in range(3):
            for j in range(3):
                x = squareX * 3 + i
                y = squareY * 3 + j

                for option in range(self.puzzle.numberOfOptions(x, y)):
                    squareOptions[option - 1] += 1

        return squareOptions

    def __removeOptions__(self, column, row, options):
        for val in options:
            try:
                self.puzzle.getOptions(column, row).remove(val)
            except ValueError:
                continue

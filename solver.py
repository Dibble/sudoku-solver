class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        i = 1
        isSolved = False

        while isSolved != True and i < 100:
            self.updateOptions()
            print(f"iteration {i}")
            i += 1

            isSolved = self.isSolved()

        return isSolved

    def isSolved(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j]['value'] == 0:
                    return False

        return True

    def updateOptions(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j]['value'] != 0:
                    continue

                rowValues = self.__getRowValues__(j)
                columnValues = self.__getColumnValues__(i)

                self.__removeOptions__(
                    i, j, rowValues + list(set(columnValues) - set(rowValues)))

                if len(self.puzzle[i][j]['options']) == 1:
                    self.puzzle[i][j]['value'] = self.puzzle[i][j]['options'][0]

    def __getRowValues__(self, row):
        rowValues = []
        for col in range(9):
            if self.puzzle[col][row]['value'] != 0:
                rowValues.append(self.puzzle[col][row]['value'])
        return rowValues

    def __getColumnValues__(self, col):
        columnValues = []
        for row in range(9):
            if self.puzzle[col][row]['value'] != 0:
                columnValues.append(self.puzzle[col][row]['value'])
        return columnValues

    def __removeOptions__(self, col, row, options):
        for val in options:
            try:
                self.puzzle[col][row]['options'].remove(val)
            except ValueError:
                continue

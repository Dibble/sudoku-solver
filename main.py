from sudoku import Sudoku
import setup


def start():
    puzzle = Sudoku()
    setup.runSetup(puzzle)


if __name__ == "__main__":
    start()

from sudoku import Sudoku
import setup
from solver import Solver


def start():
    puzzle = Sudoku()
    setup.runSetup(puzzle)

    print("Setup done, solving...")
    puzzleSolver = Solver(puzzle.puzzle)
    solved = puzzleSolver.solve()
    puzzle.print()
    print("Solved:", solved)


if __name__ == "__main__":
    start()

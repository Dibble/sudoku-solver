from sudoku import Sudoku
import setup
from solver import Solver


def start():
    puzzle = Sudoku()
    setup.runSetup(puzzle)

    print("Setup done, solving...")
    puzzleSolver = Solver(puzzle.puzzle)
    solved, iterations = puzzleSolver.solve()
    puzzle.print(False)
    print("Solved:", solved, iterations, "iterations")


if __name__ == "__main__":
    start()

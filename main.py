from sudoku import Sudoku
from setup import Setup
from solver import Solver


def start():
    puzzle = Sudoku()
    setup = Setup(puzzle)
    setup.runSetup()

    print("Setup done, solving...")
    puzzleSolver = Solver(puzzle)
    solved, iterations = puzzleSolver.solve()
    puzzle.print()
    print("Solved:", solved, iterations, "iterations")


if __name__ == "__main__":
    start()

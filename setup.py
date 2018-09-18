import readchar
from os import system


def runSetup(puzzle):
    while True:
        system('clear')

        puzzle.print(False)
        print("Enter the known values for the puzzle. Use arrow keys to move, type number 0-9 to set. Press Q when finished.")

        key = readchar.readkey()

        if key == "q" or key == "Q":
            return
        elif key == readchar.key.UP:
            puzzle.move("UP")
        elif key == readchar.key.DOWN:
            puzzle.move("DOWN")
        elif key == readchar.key.RIGHT:
            puzzle.move("RIGHT")
        elif key == readchar.key.LEFT:
            puzzle.move("LEFT")
        else:
            try:
                value = int(key)
                puzzle.setValue(value)
            except ValueError:
                print("I didn't understand that, try again")

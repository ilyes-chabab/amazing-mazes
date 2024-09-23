from maze_generator_ilyes import (
    MazeGenerator,
    size,
    Printmaze,
    name_file,
    main_backtracking_generator,
)
import random
import sys
sys.setrecursionlimit(20000)

CHAR_WALL = "#"
CHAR_WAY = "."
CHAR_VISITED = "*"
CHAR_PATH = "o"

maze_for_solver = main_backtracking_generator()
solver_stack = []
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def baseOfTheMaze():
    maze_for_solver[0][0] = CHAR_PATH
    maze_for_solver[1][0] = CHAR_PATH
    maze_for_solver[size - 2][size - 1] = CHAR_PATH
    maze_for_solver[size - 1][size - 1] = CHAR_PATH


baseOfTheMaze()


def validCaseSolver(x, y):
    if 0 <= x < size and 0 <= y < size and maze_for_solver[x][y] == CHAR_WAY:
        return True
    return False


def mazeSolver(x, y):
    if x == size - 2 and y == size - 2:
        return True
    else:

        maze_for_solver[x][y] = CHAR_PATH

        random.shuffle(MOVES)

        for dx, dy in MOVES:
            new_x = x + dx
            new_y = y + dy

            if validCaseSolver(new_x, new_y):
                if mazeSolver(new_x, new_y):
                    maze_for_solver[new_x][new_y] = CHAR_PATH
                    return True
                else:
                    maze_for_solver[new_x][new_y] = CHAR_VISITED


def MakeFile(name):
    with open(f"{name}.txt", "a") as file:

        sys.stdout = file
        print(" ")
        print("resolution en backtracking : ")
        Printmaze(maze_for_solver)

        sys.stdout = sys.__stdout__


def main_backtracking_solver():
    mazeSolver(1, 1)
    MakeFile(name_file)


if __name__ == "__main__":

    main_backtracking_solver()

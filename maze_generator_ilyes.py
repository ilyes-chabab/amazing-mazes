import random
import sys

sys.setrecursionlimit(20000)  


size = int(input("Quelle taille de labyrinthe voullez-vous ? : "))
name_file = str(input("Quel nom de fichier voullez-vous ? : "))

if size % 2 != 1:
    size += 1

size = 2 * size + 1
maze = []
MOVES = [(-2, 0), (2, 0), (0, -2), (0, 2)]
generator_stack = []


def BaseOfTheMaze(size, maze):
    maze = [["#" for i in range(size)] for i in range(size)]

    maze[0][0] = "."
    maze[1][0] = "."
    maze[size - 2][size - 1] = "."
    maze[size - 1][size - 1] = "."

    for i in range(1, size - 1):
        for j in range(size):
            if i % 2 != 0 and j % 2 != 0:
                maze[i][j] = "."

    return maze


maze = BaseOfTheMaze(size, maze)


def IsCaseValidForGenerator(x, y):
    if (
        0 <= x < size
        and 0 <= y < size
        and maze[x][y] == "."
        and (x, y) not in generator_stack
    ):
        return True
    return False


def MazeGenerator(x, y):
    maze[x][y] = "."

    random.shuffle(MOVES)

    for MoveX, MoveY in MOVES:
        NewX = x + MoveX
        NewY = y + MoveY

        if IsCaseValidForGenerator(NewX, NewY):
            generator_stack.append((NewX, NewY))
            maze[x + MoveX // 2][y + MoveY // 2] = "."
            MazeGenerator(NewX, NewY)

    return maze


def Printmaze(maze):
    n = 0
    for i in maze:
        print("".join(maze[n]))
        n += 1


def MakeFile(name):
    with open(f"{name}.txt", "w") as file:

        sys.stdout = file
        print(f"Labyrinthe en backtracking de taille {(size-1 )/2}: ")
        Printmaze(maze)

        sys.stdout = sys.__stdout__


def main_backtracking_generator():
    MazeGenerator(1, 1)
    MakeFile(name_file)
    return maze


if __name__ == "__main__":
    main_backtracking_generator()

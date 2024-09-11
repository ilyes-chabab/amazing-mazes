import sys

maze = [
    [".", ".", "#", "#", "#", "#", "#"],
    ["#", ".", "#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", ".", ".", "."],
]

file_name = input("Quel nom de fichier voulez-vous ? : ")
start = (0, 0)
size_of_maze = 7
end = (size_of_maze - 1, size_of_maze - 1)


def MazeSolver(maze, x, y):

    if x < 0 or x > len(maze) or y < 0 or y > len(maze):
        return False

    if maze[x][y] == "#" or maze[x][y] == "*" or maze[x][y] == "o":
        return False

    if x == len(maze) - 1 and y == len(maze) - 1:
        maze[x][y] = "o"
        return True

    maze[x][y] = "o"

    if (
        MazeSolver(maze, x, y + 1)
        or MazeSolver(maze, x + 1, y)
        or MazeSolver(maze, x, y - 1)
        or MazeSolver(maze, x - 1, y)
    ):
        return True

    maze[x][y] = "*"
    return False


def Printmaze(maze):
    for case in maze:
        print("".join(case))


MazeSolver(maze, 0, 0)
Printmaze(maze)


with open(f"{file_name}.txt", "w") as file:
    sys.stdout = file

    Printmaze(maze)

    sys.stdout = sys.__stdout__

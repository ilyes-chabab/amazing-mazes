from maze_generator_ilyes import MazeGenerator , size , Printmaze
import random

CHAR_WALL = "#"
CHAR_WAY = "."
CHAR_VISITED = "*"
CHAR_PATH = "o"
maze_for_solver = MazeGenerator(1,1)

solver_stack=[]
MOVES = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def baseOfTheMaze():
    maze_for_solver[0][0] = CHAR_PATH
    maze_for_solver[1][0] = CHAR_PATH
    maze_for_solver[size-2][size-1] = CHAR_PATH
    maze_for_solver[size-1][size-1] = CHAR_PATH

baseOfTheMaze()

def validCaseSolver(x,y):
    if 0 <= x < size and 0 <= y < size and maze_for_solver[x][y] == CHAR_WAY:
        return True
    return False
    

def mazeSolver(x,y):
    if x and y == size - 1 and size - 1 :
        return True
    else:
    
        maze_for_solver[x][y] = CHAR_VISITED

        random.shuffle(MOVES)

        for dx , dy in MOVES:
            new_x = x + dx
            new_y = y + dy

            if validCaseSolver(x + dx , y + dy) and maze_for_solver[(x + new_x) // 2][(y + new_y) // 2] == CHAR_WAY :
                maze_for_solver[(x + new_x) // 2][(y + new_y) // 2] = CHAR_VISITED
                if mazeSolver(new_x,new_y):
                    maze_for_solver[x][y] = CHAR_PATH


if __name__ == "__main__":
    
    Printmaze(maze_for_solver)
    mazeSolver(1,1)
    print("_________________________")
    Printmaze(maze_for_solver)
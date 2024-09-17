from maze_generator_ilyes import MazeGenerator , size , Printmaze
import random

maze_for_solver = MazeGenerator(1,1)
solver_stack=[]

solver_movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def IsCaseValidForSolver(x,y):
    if 0 <= x < size and 0 <= y < size and maze_for_solver[x][y] == "." and (x,y) not in solver_stack:
        return True
    
def MazeSolver(x,y):
    maze_for_solver[x][y] = "o"

    random.shuffle(solver_movement)

    for dx , dy in solver_movement:
        Newx = x + dx
        Newy= y + dy
        if IsCaseValidForSolver(Newx,Newy):
            maze_for_solver[x + dx ][y + dy ] = "o"
            MazeSolver(x+dx,x+dy)

if __name__ == "__main__":
    MazeSolver(0,0)
    Printmaze(maze_for_solver)
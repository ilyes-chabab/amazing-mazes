import random

def BaseOfTheMaze(size , maze):
    maze = [["#" for i in range(size)] for i in range(size)]

    maze[0][0] = "."
    maze[1][0] = "."
    maze[size-2][size-1] = "."
    maze[size-1][size-1] = "."

    for i in range(1,size-1):
        for j in range (size):
            if i % 2 != 0 and j % 2!=0 :
                maze[i][j] = "."
    
    return maze

def IsCaseValidForGenerator(x,y):
    if 0 <= x < size and 0 <= y < size and maze[x][y] == "." and (x,y) not in generator_stack:
        return True

def IsCaseValidForSolver(x,y):
    if 0 <= x < size and 0 <= y < size and maze[x][y] == "." and (x,y) not in solver_stack:
        return True

def MazeGenerator(x,y):
    maze[x][y]="."

    random.shuffle(generator_movement)

    for MoveX , MoveY in generator_movement:
        NewX = x + MoveX 
        NewY = y + MoveY

        if IsCaseValidForGenerator(NewX,NewY):
            generator_stack.append((NewX,NewY))
            maze[x + MoveX //2][y + MoveY //2] = "."
            MazeGenerator(NewX,NewY)

def Printmaze(maze):
    n=0
    for i in maze:
        print("".join(maze[n]))
        n+=1

if __name__ == "__main__":
    # size = int(input("Quelle taille de labyrinthe voullez-vous ? : "))
    # if size % 2 !=1:
    #     size +=1    
    size = 3
    size = 2* size +1
    maze=[]
    generator_movement = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    solver_movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    generator_stack=[]
    solver_stack=[]
    maze = BaseOfTheMaze(size,maze)
    print("base sur laquelle le générateur va s'appuyer ")
    Printmaze(maze)
    print("génération du labyrinthe")
    MazeGenerator(1,1)
    Printmaze(maze)

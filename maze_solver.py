import sys

labyrinthe = [
    ['.', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '.', '.']
]

file_name= input("Quel nom de fichier voulez-vous ? : ")
start = (0,0)
size_of_labyrinthe = 7
end = (size_of_labyrinthe -1,size_of_labyrinthe -1)
    
def MazeSolver(labyrinthe,x,y):
    
    if x < 0 or x > len(labyrinthe) or y < 0 or y > len(labyrinthe):
        return False
    
    if labyrinthe[x][y] == '#' or labyrinthe[x][y] == '*' or labyrinthe[x][y] == 'o':
        return False
    
    if x == len(labyrinthe) - 1 and y == len(labyrinthe) - 1:
        labyrinthe[x][y] = 'o'
        return True
    
    labyrinthe[x][y] = 'o'

    if (MazeSolver(labyrinthe, x, y + 1) or  
        MazeSolver(labyrinthe, x + 1, y) or  
        MazeSolver(labyrinthe, x, y - 1) or  
        MazeSolver(labyrinthe, x - 1, y)):   
        return True

    labyrinthe[x][y] = '*'
    return False

    

def PrintLabyrinthe(labyrinthe):
    for case in labyrinthe:
        print("".join(case))
 

MazeSolver(labyrinthe,0,0) 
PrintLabyrinthe(labyrinthe) 


with open(f"{file_name}.txt","w") as file:
    sys.stdout = file
    
    PrintLabyrinthe(labyrinthe) 

    sys.stdout = sys.__stdout__

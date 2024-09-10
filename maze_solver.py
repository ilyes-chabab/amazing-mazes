
labyrinthe = [
    ['S', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#'],
    ['#', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', 'E']
]

list_of_walls = []
start = (0,0)
end = (6,6)

up , down , left , right = -1,1,-1,1

def IsWayValid(labyrinthe,position):
    if labyrinthe[position[0]][position[1]] == "#":
        return False
    else:
        return True

def IsFinish(labyrinthe,position):
    if labyrinthe[position[0]][position[1]] == "E":
        return True

def MazeSolver(labyrinthe,current_position):
    # while not IsFinish(labyrinthe,current_position):
    current_position[0] += down
    print(current_position)

    

def PrintLabyrinthe(labyrinthe):
    for lists in labyrinthe:
        print(lists)
 
PrintLabyrinthe(labyrinthe) 
# MazeSolver(labyrinthe,start)  
next = start[0] + up
print(next)



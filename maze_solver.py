
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
        print("finish")
        return True

def MazeSolver(labyrinthe,current_position):
    print(current_position)
    while not IsFinish(labyrinthe,current_position):
        line_position  , column_position = current_position
        if IsWayValid(labyrinthe,current_position):
            line_position +=1
        else:
            line_position -=1
            column_position +=1
        current_position = (line_position,column_position)
        print(current_position)

    

def PrintLabyrinthe(labyrinthe):
    for lists in labyrinthe:
        print(lists)
 
PrintLabyrinthe(labyrinthe) 
MazeSolver(labyrinthe,start)  



import random

def base_of_the_maze(size , maze):
    maze = [["#" for i in range(size)] for i in range(size)]


    for i in range(1,size-1):
        for j in range (size):
            if i % 2 != 0 and j % 2!=0 :
                maze[i][j] = CHAR_WAY
    
    return maze

def make_sets(maze):
    for i in range(1,size-1):
        for j in range (1,size-1):
            if maze[i][j] == CHAR_WAY:
                cell_list.append([(i,j)])   
            elif maze[i][j] == CHAR_WALL:
                wall_list.append([(i,j)]) 

def valid_cell(x,y,maze):
    if 0 <= x < len(maze) and 0 <= y < len(maze) :
        return True
    
def kruskal_generator(maze):

    random.shuffle(cell_list)

    iter_cell = 0

    print(cell_list)
    for cell in cell_list:
        x,y  = cell_list[iter_cell][0][0] , cell_list[iter_cell][0][1]
        print((x,y))
        iter_cell +=1
        for dx,dy in MOVES:
            neighbor_cell = (x+dx, y+dy)
            print("neighbor", neighbor_cell)
            if valid_cell(x + dx , y+dy, maze):
                print("neigbor != cell_list",neighbor_cell , cell_list[0][0])
                if neighbor_cell != cell_list[0][0]:
                    ite = 0
                    for cell in cell_list:
                        print("cell", cell)
                        if neighbor_cell == cell[0]:
                            print("neighbor == cell[0] in cell_list : ",neighbor_cell , cell[0])
                            new_cell = cell_list.pop(ite)
                            print("new_cell", new_cell)
                            for new in new_cell:
                                print("new in new_cell",new)
                                cell_list[0].append(new)
                            print(cell_list)
                        else:
                            ite +=1
    # n=0
    # for i in cell_list:
    #     n+=1
    
    # if n >  5:
    #     kruskal_generator(maze)
                
def print_maze(maze):
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
    MOVES = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    CHAR_WALL = "#"
    CHAR_WAY = "."
    wall_list=[]
    cell_list=[]
    
    maze = base_of_the_maze(size,maze)

    print("base sur laquelle le générateur va s'appuyer ")
    print_maze(maze)
    make_sets(maze)
    kruskal_generator(maze)
    maze[0][0] = "."
    maze[1][0] = "."
    maze[size-2][size-1] = "."
    maze[size-1][size-1] = "."

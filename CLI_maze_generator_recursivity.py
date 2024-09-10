def maze_size():
    size = input("How big does the maze need to be ? (one number only) : ")
    size = int(size)
    size *= size
    return size

def choose_file_name():
    file = input("Enter the name for the file : ")
    return file

def create_maze_file():
    file = open(choose_file_name, "w") 
    file.write("Voici le texte de mon fichier") 
    file.close()



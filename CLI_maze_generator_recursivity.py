def maze_size():
    size = input("How big does the maze need to be ? (one number only) : ")
    size = int(size)
    return size


def choose_file_name():
    file = input("Enter the name for the file (.txt at the end) : ")
    return file


def create_maze():
    l = []
    a = 2 * maze_size() + 1
    for i in range(a):
        row = "#" * a
        l.append(row)
    return l


def create_maze_file():
    maze = create_maze()
    with open(choose_file_name(), "w") as file:
        for line in maze:
            file.write(line + "\n")
        

create_maze_file()

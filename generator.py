import random

def input_maze_size():
    size = input("How big does the maze need to be ? (one number only) : ")
    return int(size)

def real_maze_size(size):
    return 2 * size + 1


def choose_file_name():
    file = input("Enter the name for the file (.txt at the end) : ")
    return file # Return the file name choosen by the user


def create_maze(size):
    l = []
    new_size = real_maze_size(size)
    for i in range(new_size):
        row = ["#"] * new_size # Creating our lines for the maze
        l.append(row) # adding the lines to our maze
    return l # return the maze


def create_maze_file(maze):
    with open(choose_file_name(), "w") as file:
        for line in maze:
            file.write("".join(line) + "\n") # Writing the maze in a file without [] or ""

def generate_random_positions(size):
    random_positions = []
    real_size = real_maze_size(size)
    for i in range(2):
        i = random.randint(1,real_size - 2)
        random_positions.append(i)
    return random_positions

    # return [random.randint(1,real_size), random.randint(1,real_size)]

def generate_random_directions():
    d = random.randint(1,4)
    return d

def recursive_backtrack():
    direction = generate_random_directions()
    numbers = generate_random_positions(size)
    maze = create_maze(size)
    if direction == 1:
        maze[numbers[0]][numbers[1]] = maze[numbers[0]][numbers[1] + 1]
        print ("up")
    elif direction == 2:
        maze[numbers[0]][numbers[1]] = maze[numbers[0] + 1][numbers[1]]
        print ("right")
    elif direction == 3:
        maze[numbers[0]][numbers[1]] = maze[numbers[0]][numbers[1] - 1]
        print ("down")
    elif direction == 4:
        maze[numbers[0]][numbers[1]] = maze[numbers[0] - 1][numbers[1]]
        print ("left")


def main():
    size = input_maze_size()
    recursive_backtrack(size)
    

if __name__ == "__main__":
    main()

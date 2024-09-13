import random

def maze_size():
    size = input("How big does the maze need to be ? (one number only) : ")
    size = int(size) # Transform the str in a int to return it properly
    return size

def real_maze_size():
    size = 2 * maze_size() + 1 
    return size # returning the "real size" of the maze to generate between the good random.randint


def choose_file_name():
    file = input("Enter the name for the file (.txt at the end) : ")
    return file


def create_maze():
    l = []
    new_size = 2 * maze_size() + 1
    for i in range(new_size):
        row = ["#"] * new_size
        l.append(row)
    return l


def create_maze_file(maze):
    with open(choose_file_name(), "w") as file:
        for line in maze:
            file.write("".join(line) + "\n")

def generate_random_numbers():
    random_numbers = []
    size = real_maze_size()
    for i in range(2):
        i = random.randint(1,size)
        random_numbers.append(i)
    return random_numbers

def generate_random_directions():
    d = random.randint(1,4)
    return d

def recursive_backtrack():
    direction = generate_random_directions()
    numbers = generate_random_numbers()
    maze = create_maze()
    if direction == 1:
        maze[numbers[0]][numbers[1]] = maze[numbers[0]][numbers[1] + 1]
    elif direction == 2:
        maze[numbers[0]][numbers[1]] = maze[numbers[0] + 1][numbers[1]]
    elif direction == 3:
        maze[numbers[0]][numbers[1]] = maze[numbers[0]][numbers[1] - 1]
    elif direction == 4:
        maze[numbers[0]][numbers[1]] = maze[numbers[0] - 1][numbers[1]]

def main():
    maze = create_maze()
    create_maze_file(maze)
    


if __name__ == "__main__":
    # main()
    recursive_backtrack()

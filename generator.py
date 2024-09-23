import random

def input_maze_size():
    size = input("How big does the maze need to be? (one number only) : ")
    return int(size)

def real_maze_size(size):
    return 2 * size + 1

def choose_file_name():
    file = input("Enter the name for the file (.txt at the end) : ")
    return file

def create_maze(size):
    new_size = real_maze_size(size)
    l = [["#"] * new_size for _ in range(new_size)]
    return l

def create_maze_file(maze):
    with open(choose_file_name(), "w") as file:
        for line in maze:
            file.write("".join(line) + "\n")

def random_directions():
    directions = [1, 2, 3, 4]  # 1: up, 2: right, 3: down, 4: left
    random.shuffle(directions)  # Shuffle direction for each call
    return directions

def recursive_backtrack(maze, x, y, size):
    maze[x][y] = " "  # Mark the current cell as empty

    for direction in random_directions():
        if direction == 1:
            nx, ny = x - 2, y
        elif direction == 2:
            nx, ny = x, y + 2
        elif direction == 3:
            nx, ny = x + 2, y
        elif direction == 4:
            nx, ny = x, y - 2

        # Check if the new positions is in the maze
        if 1 <= nx < real_maze_size(size) - 1 and 1 <= ny < real_maze_size(size) - 1:
            if maze[nx][ny] == "#":  # If the cell was not visited
                # Take out the wall between cell
                maze[(x + nx) // 2][(y + ny) // 2] = " "
                # Calling the function recursivingly to keep diging
                recursive_backtrack(maze, nx, ny, size)

def generate_maze(size):
    maze = create_maze(size)
    start_x, start_y = 1, 1  # Starting point
    recursive_backtrack(maze, start_x, start_y, size)
    return maze

def main():
    size = input_maze_size()
    maze = generate_maze(size)
    create_maze_file(maze)

if __name__ == "__main__":
    main()

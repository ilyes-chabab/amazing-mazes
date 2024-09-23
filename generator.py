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
    directions = [1, 2, 3, 4]  # 1: haut, 2: droite, 3: bas, 4: gauche
    random.shuffle(directions)  # Mélanger les directions pour chaque appel
    return directions

def recursive_backtrack(maze, x, y, size):
    maze[x][y] = " "  # Marque la cellule actuelle comme un chemin (espace vide)

    for direction in random_directions():
        if direction == 1:  # Haut
            nx, ny = x - 2, y
        elif direction == 2:  # Droite
            nx, ny = x, y + 2
        elif direction == 3:  # Bas
            nx, ny = x + 2, y
        elif direction == 4:  # Gauche
            nx, ny = x, y - 2

        # Vérifier si la nouvelle position est dans les limites du labyrinthe
        if 1 <= nx < real_maze_size(size) - 1 and 1 <= ny < real_maze_size(size) - 1:
            if maze[nx][ny] == "#":  # Si la cellule n'a pas encore été visitée
                # Enlever le mur entre les cellules (mettre un espace)
                maze[(x + nx) // 2][(y + ny) // 2] = " "
                # Appel récursif pour continuer à creuser à partir de la nouvelle cellule
                recursive_backtrack(maze, nx, ny, size)

def generate_maze(size):
    maze = create_maze(size)
    start_x, start_y = 1, 1  # Point de départ
    recursive_backtrack(maze, start_x, start_y, size)
    return maze

def main():
    size = input_maze_size()
    maze = generate_maze(size)
    create_maze_file(maze)

if __name__ == "__main__":
    main()

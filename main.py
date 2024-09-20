import maze_generator_ilyes
import maze_solver_ilyes

if __name__ == "__main__":

    mode = int(input("Quel programme voulez vous executer ? generateur de labyrtinthe en backtracking(1) , resolveur de labyrinthe en backtracking(2) "))

    if mode == 1:
        maze_generator_ilyes.main_backtracking_generator()
    elif mode == 2:
        maze_solver_ilyes.main_backtracking_solver()
    else:
        print("Veuillez entrer un chiffre valide. ")
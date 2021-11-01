from Puzzle import Puzzle
from Solve import Solve

if __name__ == "__main__":
    _puzzle = Puzzle()

    # EXECUÇÃO DA DISTANCIA MANHATTAN
    solve = Solve(puzzle=_puzzle, heuristic="out_position")
    solution, moviments = solve.a_star()

    if solution != None:
        print(f"\nSolucao: ({moviments}) Movimentos")
        for sol in solution:
            for i in sol:
                print(i)
            print("\n")
    else:
        print("Não foi possivel resolver")
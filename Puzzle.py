import random
from Escolha import escolha, manual

class Puzzle:
    possible_moviments = ("L", "U", "R", "D")
    initial_state = None

    goal_state = \
                [
                    [1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 0]
                ]

    def __init__(self) -> None:
        randomize = escolha()

        if randomize:
            self.initial_state = manual()
        else:
            initial_state = [ i for i in range(0, 8) ]
            random.shuffle(initial_state)

        self.initial_state = \
                    [
                        [initial_state[0], initial_state[1], initial_state[2]],
                        [initial_state[3], initial_state[4], initial_state[5]],
                        [initial_state[6], initial_state[7], initial_state[8]],
                    ]

    def get_initial_state(self) -> list:
        return self.initial_state

    def get_goal_state(self) -> list:
        return self.goal_state

    def valid_moviment(self, moviment: str = "U") -> int:
        for i in range(len(self.initial_state)):
            for j in range(len(self.initial_state)):
                if self.initial_state[i][j] == 0:
                    if i == 0:
                        if moviment == "U": return 99, 99
                        elif j == 0 and moviment == "L": return 99, 99
                        elif j == 2 and moviment == "R": return 99, 99
                        else: return i, j
                    if i == 1:
                        if j == 0 and moviment == "L": return 99, 99
                        elif j == 2 and moviment == "R": return 99, 99
                        else: return i, j
                    if i == 2:
                        if moviment == "D": return 99, 99
                        elif j == 0 and moviment == "L": return 99, 99
                        elif j == 2 and moviment == "R": return 99, 99
                        else: return i, j

    def possible_moviments(self, current_state:list = []) -> dict:
        moviment_indexes = {}

        for moviment in self.possible_moviments:
            i, j = self.valid_moviment(moviment)
            if i != 99: moviment_indexes[moviment] = (i, j)
        
        return moviment_indexes

    def swap(self, moviment:str = "U", i:int = 0, j:int = 0) -> bool:
        if moviment == "U":
            temp = self.initial_state[i - 1][j]
            self.initial_state[i - 1][j] = self.initial_state[i][j]
            self.initial_state[i][j] = temp
        elif moviment == "D":
            temp = self.initial_state[i + 1][j]
            self.initial_state[i + 1][j] = self.initial_state[i][j]
            self.initial_state[i][j] = temp
        elif moviment == "L":
            temp = self.initial_state[i][j - 1]
            self.initial_state[i][j - 1] = self.initial_state[i][j]
            self.initial_state[i][j] = temp
        elif moviment == "R":
            temp = self.initial_state[i][j + 1]
            self.initial_state[i][j + 1] = self.initial_state[i][j]
            self.initial_state[i][j] = temp

            return True

    def reached_final_goal(self) -> bool:
        return True if self.initial_state == self.goal_state else False

    def is_solvable(self,current_state) -> bool:
        inv_count = 0
        dale = []

        for lista in current_state:
            for element in lista:
                dale.append(element)

        for i in range(len(dale)):
            for j in range(i+1, len(dale)):
                if dale[i] > 0 and dale[j] > 0 and dale[i] > dale[j]:
                    inv_count += 1 
        
        if inv_count%2 != 0:
            print("não é solucionavel")
            return False
        
        print("é solucionavel")
        return True
        
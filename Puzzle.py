from copy import Error
import random
from Escolha import escolha, manual

class Puzzle:
    initial_state = []
    randomize = False

    def __init__(self, escolha_ra=True) -> None:
        if escolha_ra:
            self.randomize = escolha()

        if self.randomize:
            self.initial_state = manual()
        else:
            # self.initial_state = [ i for i in range(0, 9) ]
            # random.shuffle(self.initial_state)

            self.initial_state = [8, 1, 2, 6, 7, 0, 5, 4, 3]

        print(self.initial_state)
        self.initial_state = \
                    [
                        [self.initial_state[0], self.initial_state[1], self.initial_state[2]],
                        [self.initial_state[3], self.initial_state[4], self.initial_state[5]],
                        [self.initial_state[6], self.initial_state[7], self.initial_state[8]],
                    ]

        
        self.goal_state = \
                    [
                        [1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 0]
                    ]

    def get_initial_state(self) -> list:
        return self.initial_state

    def set_initial_state(self, state):
        self.initial_state = state

    def get_goal_state(self) -> list:
        return self.goal_state

    def valid_moviment(self, moviment: str = "U", current_state: list = []) -> int:
        try:
            len_cur = len(current_state)
        except Error:
            print("Error: Error")
            print("Current State: ", current_state)
            return 99, 99

        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] == 0:
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

        possible_moviments = ("L", "U", "R", "D")

        for moviment in possible_moviments:
            i, j = self.valid_moviment(moviment=moviment, current_state=current_state)
            if i != 99: moviment_indexes[moviment] = (i, j)
        
        return moviment_indexes

    def swap(self, moviment:str = "U", i:int = 0, j:int = 0, curr_state:list = []) -> list:
        if moviment == "U":
            temp = curr_state[i - 1][j]
            curr_state[i - 1][j] = curr_state[i][j]
            curr_state[i][j] = temp
        elif moviment == "D":
            temp = curr_state[i + 1][j]
            curr_state[i + 1][j] = curr_state[i][j]
            curr_state[i][j] = temp
        elif moviment == "L":
            temp = curr_state[i][j - 1]
            curr_state[i][j - 1] = curr_state[i][j]
            curr_state[i][j] = temp
        elif moviment == "R":
            temp = curr_state[i][j + 1]
            curr_state[i][j + 1] = curr_state[i][j]
            curr_state[i][j] = temp

        return curr_state

    def reached_final_goal(self, curr_state) -> bool:
        return True if curr_state == self.goal_state else False

    def is_solvable(self,current_state) -> bool:
        inv_count = 0
        dale = []

        for lista in current_state:
            for element in lista:
                dale.append(element)

        for i in range(len(dale)-1):
            for j in range(i+1, len(dale)):
                if dale[i] > 0 and dale[j] > 0 and dale[i] > dale[j]:
                    inv_count += 1 
        
        if inv_count%2 != 0:
            print(inv_count)
            print("não é solucionavel")
            return False
        
        print("é solucionavel")
        print(inv_count)
        return True
        
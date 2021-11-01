from math import sqrt
import copy
from os import write

class Solve:
    def __init__(self, puzzle, heuristic="manhattan") -> None:
        self.__puzzle = puzzle
        self.__initial_state = puzzle.get_initial_state()
        self.__goal_state = puzzle.get_goal_state()
        self.__g_iterator = -1

        self.__heuristic = heuristic

    def find_element(self, element, goal_state):
        for i in range(len(goal_state)):
            for j in range(len(goal_state[i])):
                if element == goal_state[i][j]:
                    return i, j

    def manhattan(self, initial_state, goal_state) -> None:
        sum_man = 0

        for i in range(len(initial_state)):
            for j in range(len(initial_state[i])):
                indice_i, indice_j = self.find_element(element=initial_state[i][j], goal_state=goal_state)
                sum_man += abs(i - indice_i) + abs(j - indice_j)

        return sum_man

    def euclides(self, initial_state, goal_state) -> None:
        sum_eu = 0

        for i in range(len(initial_state)):
            for j in range(len(initial_state[i])):
                indice_i, indice_j = self.find_element(element=initial_state[i][j], goal_state=goal_state)
                sum_eu += sqrt((i - indice_i)**2 + abs(j - indice_j)**2)

        return sum_eu
    
    def out_position(self, initial_state: list = [], goal_state: list = []) -> None:
        sum_out = 0

        for i in range(len(goal_state)):
            for j in range(len(goal_state[i])):
                if initial_state[i][j] != goal_state[i][j]:
                    sum_out += 1

        return sum_out

    def func_g(self):
        self.__g_iterator += 1

        return self.__g_iterator
    
    def choice_func(self, cur_state):
        if self.__heuristic == "out_position":
            return self.out_position(initial_state=cur_state, goal_state=self.__goal_state)
        elif self.__heuristic == "manhattan":
            return self.manhattan(initial_state=cur_state, goal_state=self.__goal_state)
        else:
            return self.euclides(initial_state=cur_state, goal_state=self.__goal_state)

    def a_star(self):
        if not self.__puzzle.is_solvable(current_state=self.__initial_state):
            return None, None

        # Estados abertos atualmente
        open_states = []

        # Estados já explorados
        closed_states = []

        # Estados escolhidor para percorrer
        choiced_states = []

        g = self.func_g()
        h = self.choice_func(cur_state=self.__initial_state)
        resol_f = g + h

        closed_states.append(self.__initial_state)

        f = open("./state.txt", "w")

        print(f"\nMovimento: {g}")
        print(f"Estado: {self.__initial_state}")
        print(f"F: {g} + {h} = {resol_f}")

        f.write(f"Movimento: {g}\n")
        f.write(f"Estado: {self.__initial_state}\n")
        f.write(f"F: {resol_f}\n")

        while self.__puzzle.reached_final_goal(curr_state=self.__initial_state) != True:
            print("\n=====================================================")
            choiced_states.append(self.__initial_state)

            current_state = copy.deepcopy(self.__initial_state)
            possible_moviment_dict = self.__puzzle.possible_moviments(current_state=current_state)
            
            g = self.func_g()
            for moviment in possible_moviment_dict:
                current_state_copy = copy.deepcopy(current_state)

                current_state_swapped = self.__puzzle.swap(
                                                moviment=moviment, 
                                                i=possible_moviment_dict[moviment][0],
                                                j=possible_moviment_dict[moviment][1],
                                                curr_state=current_state_copy
                                            )

                h = self.choice_func(cur_state=current_state_swapped)
                open_states.append({
                        "State":current_state_swapped,
                        "G": g,
                        "H": h
                    })

            open_states.sort(key=self.func_f)

            for i in open_states:
                h = self.choice_func(cur_state=i['State'])
                resol_f = g + h

                print(f"Movimento: {g}")
                print(f"Possiveis: {i['State']}")
                print(f"F: {g} + {h} = {resol_f}\n")

            for i in range(len(open_states)):
                if not open_states[i]["State"] in closed_states:
                    closed_states.append(open_states[i]["State"])
                    choiced_states.append(open_states[i]["State"])
                    
                    self.__initial_state = open_states[i]["State"]

                    # PRINT MOVIMENT
                    h = self.choice_func(cur_state=self.__initial_state)
                    resol_f = g + h

                    print(f"Movimento: {g}")
                    print(f"Estado: {self.__initial_state}")
                    print(f"F: {g} + {h} = {resol_f}")
                    
                    # WRITE MOVIMENT
                    f.write(f"Movimento: {g}\n")
                    f.write(f"Estado: {self.__initial_state}\n")
                    f.write(f"F: {resol_f}\n")

                    f.write(f"Possible Moviment: \n")
                    for j in open_states:
                        f.write(f"{j}\n")

                    f.write("\n")
    
                    # CLEAR LIST
                    open_states.clear()
                    break
                
                if i == len(open_states)-1:
                    print("\nNenhum movimento pode ser feito")

                    print("Closed States:")
                    for i in closed_states:
                        print(i)

                    print("Open States: ")
                    for i in open_states:
                        print(i)

                    return None, None

        f.close()
        return choiced_states, g + 1

    def func_f(curr_state, a):
        return a["G"] + a["H"]
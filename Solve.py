from math import sqrt

class Solve:
    def __init__(self, puzzle) -> None:
        self.__puzzle = puzzle
        self.__initial_state = puzzle.get_initial_state()
        self.__goal_state = puzzle.get_goal_state()

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

        for i in range(len(initial_state)):
            for j in range(len(initial_state[i])):
                if initial_state[i][j] != goal_state[i][j] :
                    sum_out += 1

        return sum_out

    def func_g(self):
        pass
    
    def choice_func(self):
        pass

    def a_star(self):
        if not self.__puzzle.is_solvable(current_state=self.__initial_state):
            return None

        open_states = []
        closed_states = []

        g = self.func_g()
        h = self.choice_func()

        closed_states.append({
            "Moviment": None, 
            "State": self.__initial_state, 
            "F": self.func_f(g, h)
        })

        while self.__puzzle.reached_final_goal():
            possible_moviment_dict = self.__puzzle.possible_moviments(current_state=current_state)

    def func_f(g,h):
       return (g + h)  
        


# initial
# [        
#     0 : [1, 2, 3],
#     1 : [0, 8, 7],[1,2]
#     2 : [4, 5, 6]
# ]

# abs( (1 - 2) + (2 - 0) )

# goal
# [        
#     0 : [1, 2, 3],
#     1 : [4, 5, 6],[2,0]
#     2 : [7, 8, 0]
# ]

# initial
# [        
#     0 : [1, 2, 3],
#     1 : [6, 8, 7],[1,2]
#     2 : [4, 5, 0]
# ]
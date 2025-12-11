import re
import numpy as np
import copy
import math
import shapely

import itertools
import networkx as nx
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(1500)

from collections import deque
from scipy.optimize import linprog
import pulp




def get_new_lights(button: list, original_lights: str):
    original_lights = list(original_lights)
    new_light = copy.deepcopy(original_lights)
    for b in button:
        if original_lights[b] == ".":
            new_light[b] = "#"
        else:
            new_light[b] = "."
    return "".join(new_light)

def extend_graph(G, start_node, buttons):
    for button in buttons:
        new_node = get_new_lights(button, start_node)
        button_str=",".join([str(i) for i in button])
        should_extend = False
        if new_node not in G.nodes:
            G.add_node(new_node)
            should_extend = True
        if (start_node, new_node, button_str) not in [(n1,n2,b) for n1, n2, b in G.edges(data="button")]:
            G.add_edge(start_node, new_node, button=button_str)
            # should_extend = True
        if should_extend:
            extend_graph(G, start_node=new_node, buttons=buttons)

def answer_1(input: list):
    answer = 0
    for index, line in enumerate(input):
        print("Processing line", index)
        goal = ""
        buttons = []
        joltage = []
        for chunk in line.split(" "):
            if chunk.strip()[0] == "[":
                goal = chunk.replace("[", "").replace("]", "")
            elif chunk.strip()[0] == "(":
                button = [int(b) for b in chunk.replace("(", "").replace(")", "").split(",")]
                buttons.append(button)
            elif chunk.strip()[0] == "{":
                jolt = [int(j) for j in chunk.replace("{", "").replace("}", "").split(",")]
                joltage.append(jolt)
        initial_lights = ["."] * len(goal)
        initial_lights = "".join(initial_lights)
        G = nx.DiGraph()
        
        node = copy.deepcopy(initial_lights)
        G.add_node(node)
        extend_graph(G, node, buttons)
        # edge_labels = nx.get_edge_attributes(G,'button')
        # pos = nx.spring_layout(G, scale=10)
        # nx.draw(G, pos=pos, with_labels=True)
        # nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
        # plt.show()
        path = nx.shortest_path(G, source=initial_lights, target=goal)
        answer += len(path) -1
    print("Answer 1", answer)



def convert_counts_to_counters(counts, buttons, goal_length):
    converted_counters = [0] * goal_length
    for button_index, count in enumerate(counts):
        button = buttons[button_index]
        for c in button:
            converted_counters[c] += count
    return converted_counters

# def answer_2(input: list):
    # answer = 0  
    # answer = 0
    # for index, line in enumerate(input):
    #     print("Processing line", index, line)
    #     lights = ""
    #     buttons = []
    #     joltage = []
    #     for chunk in line.split(" "):
    #         if chunk.strip()[0] == "[":
    #             lights = chunk.replace("[", "").replace("]", "")
    #         elif chunk.strip()[0] == "(":
    #             button = [int(b) for b in chunk.replace("(", "").replace(")", "").split(",")]
    #             buttons.append(button)
    #         elif chunk.strip()[0] == "{":
    #             joltage = [int(j) for j in chunk.replace("{", "").replace("}", "").split(",")]
       
    #     # goal = int("".join([str(i) for i in joltage]))
    #     goal = joltage
        
        # sorted_buttons = sorted(
        #     copy.deepcopy(buttons), 
        #     key=lambda x: len(x),
        #     reverse=True
        # )
        
#         possible_counter_configs = []
#         for counter_index, max_counter in enumerate(goal):
#             counter_config = []
#             for c in range(0, max_counter+1):
#                 base_counter = [0] * len(goal)
#                 base_counter[counter_index] = c
#                 counter_config.append(base_counter)
#             possible_counter_configs.append(counter_config)
#         possible_counter_configs = list(itertools.product(*possible_counter_configs))
#         cleaned_configs = []
#         for config in possible_counter_configs:
#             cleaned_config = [0] * len(goal)
#             for counter_index in range(len(goal)):
#                 cleaned_config[counter_index] = config[counter_index][counter_index]
#             cleaned_configs.append(tuple(cleaned_config))
#         counts = {}
        
#         # cleaned_configs = [
#         #     # tuple([0,0,0,1]),
#         #     tuple([0,1,0,1]),
#         #     tuple([1,0,1,0]),
#         #     # tuple([0,0,2,0]),
#         #     # tuple([0,0,1,1]),
#         #     # tuple([1,0,1,0]),
#         #     # tuple([1,1,0,0]),
#         #     # tuple([1,1,0,1]),
#         #     tuple([1,1,1,1]),
#         #     tuple([1,2,1,2]),
#         # ]
#         for config in cleaned_configs:
#             for b in sorted_buttons:
#                 button_index = buttons.index(b)
#                 for c in b:
#                     if config[c] > 0:
#                         break
#                 # Skip configs that the button cannot impact
#                 else:
#                     continue
                
#                 # v was not yet determined
#                 existing_count = counts.get(config, None)
#                 if existing_count is None:
#                     existing_count = [0] * len(buttons)
                
                
#                 previous_possible_config = copy.deepcopy(list(config))
#                 for c in b:
#                     previous_possible_config[c] -= 1
#                 previous_possible_config = tuple(previous_possible_config)
#                 previous_count = counts.get(previous_possible_config, None)

#                 if previous_count is None:
#                     previous_count = [0] * len(buttons)

#                 sum_existing_count = sum(existing_count)
#                 sum_previous_count = sum(previous_count)
#                 if sum_previous_count == 0 and sum_existing_count == 0:
#                     if any([previous_possible_config[i] != 0 for i in range(len(previous_possible_config))]):
#                         # Invalid previous combo
#                         continue
#                     new_count = [0] * len(buttons)
#                     new_count[button_index] = 1
#                     counts[config] = new_count
#                 elif sum_previous_count > 0 and sum_existing_count == 0:
#                     new_count = copy.deepcopy(previous_count)
#                     new_count[button_index] += 1
#                     counts[config] = new_count
#                 elif sum_previous_count > 0 and sum_existing_count > 0:
#                     if sum_previous_count + 1 < sum_existing_count:
#                         # Verify that updating the count matches the config
#                         new_count = copy.deepcopy(previous_count)
#                         new_count[button_index] += 1
#                         test_config = convert_counts_to_counters(new_count, buttons, len(goal))
#                         if test_config == config:
#                             counts[config] = new_count
                   
#         print(sum(counts[tuple(goal)]))
#         answer += sum(counts[tuple(goal)])
#         # check_counter = [0] * len(goal)
#         # for index, counter in enumerate(counts[tuple(goal)]):
#         #     print(index, c)
#         #     button = buttons[index]
#         #     for c in button:
#         #         check_counter[c] += counter
#         # print(check_counter)            
                
#         # answer += sum(min_count)
#     print("Answer 2", answer)


# def answer_2(input: list):
#     answer = 0
    # for index, line in enumerate(input):
    #     print("Processing line", index, line)
    #     lights = ""
    #     buttons = []
    #     joltage = []
    #     for chunk in line.split(" "):
    #         if chunk.strip()[0] == "[":
    #             lights = chunk.replace("[", "").replace("]", "")
    #         elif chunk.strip()[0] == "(":
    #             button = [int(b) for b in chunk.replace("(", "").replace(")", "").split(",")]
    #             buttons.append(button)
    #         elif chunk.strip()[0] == "{":
    #             joltage = [int(j) for j in chunk.replace("{", "").replace("}", "").split(",")]
       
    #     # goal = int("".join([str(i) for i in joltage]))
    #     goal = joltage
        
#         counts = {tuple([0] * len(goal)): [0] * len(buttons)}
#         queue = deque([tuple([0] * len(goal))])       
        
#         sorted_buttons = sorted(
#             copy.deepcopy(buttons), 
#             key=lambda x: len(x),
#             reverse=True
#         ) 
 
#         while queue:
#             current_config = queue.popleft()
#             current_count = counts[current_config]
#             for button in sorted_buttons:
#                 button_index = buttons.index(button)
#                 new_config = list(current_config)
#                 valid = True
#                 for c in button:
#                     new_config[c] += 1
#                     if new_config[c] > goal[c]:
#                         valid = False
#                         break
#                 if not valid:
#                     continue
                
#                 new_count = current_count[:] # Shallow copy
#                 new_count[button_index] += 1
#                 new_config_tuple = tuple(new_config)
#                 if new_config_tuple not in counts:
#                     counts[new_config_tuple] = new_count
#                     queue.append(new_config_tuple)
#                 else:
#                     existing_count = counts[new_config_tuple]
#                     if sum(new_count) < sum(existing_count):
#                         counts[new_config_tuple] = new_count        
#         result = sum(counts[tuple(goal)])
#         answer += result
    
#     print("Answer 2", answer)
    
    
def answer_2(input: list):
    answer = 0
    for index, line in enumerate(input):
        print("Processing line", index, line)
        lights = ""
        buttons = []
        joltage = []
        for chunk in line.split(" "):
            if chunk.strip()[0] == "[":
                lights = chunk.replace("[", "").replace("]", "")
            elif chunk.strip()[0] == "(":
                button = [int(b) for b in chunk.replace("(", "").replace(")", "").split(",")]
                buttons.append(button)
            elif chunk.strip()[0] == "{":
                joltage = [int(j) for j in chunk.replace("{", "").replace("}", "").split(",")]
        
        # goal = int("".join([str(i) for i in joltage]))
        
        coefficients = {i: [0]*len(buttons) for i in range(len(joltage))}
        for button_index, button in enumerate(buttons):
            for c in button:
                coefficients[c][button_index] += 1
        A_matrix = np.array([coefficients[i] for i in range(len(joltage))])
        b_matrix = joltage
        # print(len(A_matrix), len(A_matrix[0]), len(b_matrix))
        
        max_counter = max(joltage)
        # c = np.ones(10)
        # res = linprog(c, A_eq=coefficient_matrix, b_eq=ordinates, bounds=[(0, max_counter)], method='highs')
        # solution = np.linalg.solve(coefficient_matrix, ordinates)
        n_vars = A_matrix.shape[1]   # number of variables (=10)
        
        
        model = pulp.LpProblem("Integer_System_MinSum", pulp.LpMinimize)

        # Variables (integer, nonnegative)
        x = [
            pulp.LpVariable(f"x{i+1}", lowBound=0, upBound=max_counter, cat=pulp.LpInteger)
            for i in range(n_vars)
        ]

        # Objective: minimize the sum of variables
        model += pulp.lpSum(x)

        # Equality constraints Ax = b
        for row in range(A_matrix.shape[0]):
            model += pulp.lpSum(A_matrix[row, j] * x[j] for j in range(n_vars)) == b_matrix[row]

        # ==========================================================
        # Solve
        # ==========================================================
        # status = model.solve(pulp.PULP_CBC_CMD(msg=False))
        status = model.solve(pulp.COIN_CMD(msg=False, path="/opt/homebrew/bin/cbc"))

        print("Status:", pulp.LpStatus[status])

        if pulp.LpStatus[status] == "Optimal":
            sol = [pulp.value(var) for var in x]
            print("Optimal solution x:", sol)
            print("Sum:", sum(sol))
            answer +=  sum(sol)
        else:
            print("No optimal integer solution found.")
    print("Answer 2", int(answer)) 
        
        
if __name__ == "__main__":
    with open("../input/day10.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    # answer_1(input)
    answer_2(input)
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


# def min_coin_recursion(goal, coins, count, original_coins):
#     if goal == 0:
#         return count
#     if goal < 0:
#         return None
    
#     # Find biggest coin that is smaller than the remaining goal:
    # possible_coins = copy.deepcopy(coins)
    # possible_coins.sort(reverse=True)
#     for max_coin in possible_coins:
#         # max_coin = max(possible_coins)
#         coin_index = original_coins.index(max_coin)        
#         max_included = goal // max_coin
#         for coin_count in range(max_included, -1, -1):
#             new_count = copy.deepcopy(count)
#             new_count[coin_index] += coin_count
#             new_goal = goal - (coin_count * max_coin)
#             left_over_coins = copy.deepcopy(coins)
#             left_over_coins.remove(max_coin)
#             final_count = min_coin_recursion(new_goal, left_over_coins, new_count, original_coins)
#             if final_count is not None:
#                 return final_count
#     return None


# def recursion(current_index, sorted_buttons, left_over_goal, current_count, buttons):
#     if current_index >= len(sorted_buttons):
#         if all([c == 0 for c in left_over_goal]):
#             return current_count
#         elif any([c < 0 for c in left_over_goal]):
#             return None
#         else:
#             return None
#     # Get button info
#     button = sorted_buttons[current_index]
#     button_index = buttons.index(button)
    
#     # Goal counters that this button affects
    # goal_counters_button = []
    # for c in button:
    #     goal_counters_button.append(left_over_goal[c])
    
#     # Max increase is the min of affected counters
#     max_increase = min(goal_counters_button)
#     for increase in range(max_increase, -1, -1):
#         results = []
#         for c in button:
#             new_current_count = copy.deepcopy(current_count)
#             new_left_over_goal = copy.deepcopy(left_over_goal)
#             new_current_count[button_index] += increase
#             new_left_over_goal[c] -= increase
#             result_recursion = recursion(current_index+1, sorted_buttons, new_left_over_goal, new_current_count, buttons)
#             if result_recursion is not None:
#                 results.append(result_recursion)
#         if results:
#             # Return min count from results
#             min_count = None
#             for r in results:
#                 total_count = sum(r)
#                 if min_count is None or total_count < sum(min_count):
#                     min_count = r
#             return min_count
#     return None
        # print("LEFT OVER GOAL", button, increase, left_over_goal)


def convert_counts_to_counters(counts, buttons, goal_length):
    converted_counters = [0] * goal_length
    for button_index, count in enumerate(counts):
        button = buttons[button_index]
        for c in button:
            converted_counters[c] += count
    return converted_counters

def answer_2(input: list):
    answer = 0  
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
        goal = joltage
        
        sorted_buttons = sorted(
            copy.deepcopy(buttons), 
            key=lambda x: len(x),
            reverse=True
        )
        
        # count = recursion(0, sorted_buttons, goal, [0]*len(buttons), buttons)
        #         (3) (1,3) (2) (2,3) (0,2) (0,1)
        # Answer: [1,   3 ,    0,  3,   2,    1]

        # counter_button_map = {}
        # for button in sorted_buttons:
        #     button_index = buttons.index(button)
        #     # goal_counters_button = []
        #     for c in button:
        #         # goal_counters_button.append(goal[c])
        #         counter_button_map[c] = button_index
        
        # counts = {}
        # for button in sorted_buttons:
        #     button_index = buttons.index(button)
        possible_counter_configs = []
        for counter_index, max_counter in enumerate(goal):
            counter_config = []
            for c in range(0, max_counter+1):
                base_counter = [0] * len(goal)
                base_counter[counter_index] = c
                counter_config.append(base_counter)
            possible_counter_configs.append(counter_config)
        possible_counter_configs = list(itertools.product(*possible_counter_configs))
        cleaned_configs = []
        for config in possible_counter_configs:
            cleaned_config = [0] * len(goal)
            for counter_index in range(len(goal)):
                cleaned_config[counter_index] = config[counter_index][counter_index]
            cleaned_configs.append(tuple(cleaned_config))
        counts = {}
        
        # cleaned_configs = [
        #     # tuple([0,0,0,1]),
        #     tuple([0,1,0,1]),
        #     tuple([1,0,1,0]),
        #     # tuple([0,0,2,0]),
        #     # tuple([0,0,1,1]),
        #     # tuple([1,0,1,0]),
        #     # tuple([1,1,0,0]),
        #     # tuple([1,1,0,1]),
        #     tuple([1,1,1,1]),
        #     tuple([1,2,1,2]),
        # ]
        for config in cleaned_configs:
            for b in sorted_buttons:
                button_index = buttons.index(b)
                for c in b:
                    if config[c] > 0:
                        break
                # Skip configs that the button cannot impact
                else:
                    continue
                
                # v was not yet determined
                existing_count = counts.get(config, None)
                if existing_count is None:
                    existing_count = [0] * len(buttons)
                
                
                previous_possible_config = copy.deepcopy(list(config))
                for c in b:
                    previous_possible_config[c] -= 1
                previous_possible_config = tuple(previous_possible_config)
                previous_count = counts.get(previous_possible_config, None)

                if previous_count is None:
                    previous_count = [0] * len(buttons)

                sum_existing_count = sum(existing_count)
                sum_previous_count = sum(previous_count)
                if sum_previous_count == 0 and sum_existing_count == 0:
                    if any([previous_possible_config[i] != 0 for i in range(len(previous_possible_config))]):
                        # Invalid previous combo
                        continue
                    new_count = [0] * len(buttons)
                    new_count[button_index] = 1
                    counts[config] = new_count
                elif sum_previous_count > 0 and sum_existing_count == 0:
                    new_count = copy.deepcopy(previous_count)
                    new_count[button_index] += 1
                    counts[config] = new_count
                elif sum_previous_count > 0 and sum_existing_count > 0:
                    if sum_previous_count + 1 < sum_existing_count:
                        # Verify that updating the count matches the config
                        new_count = copy.deepcopy(previous_count)
                        new_count[button_index] += 1
                        test_config = convert_counts_to_counters(new_count, buttons, len(goal))
                        if test_config == config:
                            counts[config] = new_count
                   
        print(sum(counts[tuple(goal)]))
        answer += sum(counts[tuple(goal)])
        # check_counter = [0] * len(goal)
        # for index, counter in enumerate(counts[tuple(goal)]):
        #     print(index, c)
        #     button = buttons[index]
        #     for c in button:
        #         check_counter[c] += counter
        # print(check_counter)            
                
        # answer += sum(min_count)
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day10.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    # answer_1(input)
    answer_2(input)
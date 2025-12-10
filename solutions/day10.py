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


def min_coin_recursion(goal, coins, count):
    if goal == 0:
        return count
    if goal < 0:
        return None
    
    # Find biggest coin that is smaller than the remaining goal:
    possible_coins = []
    for coin in coins:
        if coin < goal:
            possible_coins.append(coin)
    
    while possible_coins:
        max_coin = max(possible_coins)
        coin_index = coins.index(max_coin)
        new_count = copy.deepcopy(count)
        new_count[coin_index] += 1
        new_goal = goal - max_coin
        final_count = min_coin_recursion(new_goal, coins, new_count)
        if final_count is not None:
            return final_count
        else:
            possible_coins.remove(max_coin)
    return None
    

def answer_2(input: list):
    answer = 0  
    answer = 0
    for index, line in enumerate(input):
        print("Processing line", index)
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
       
        goal = int("".join([str(i) for i in joltage]))
        
        converted_buttons = []
        for button in buttons:
            button_value = 0
            for i, b in enumerate(button):
                button_value += 10**b
            converted_buttons.append(button_value)

        total_count = min_coin_recursion(goal=goal, coins=converted_buttons, count=[0]*len(converted_buttons))
        print(total_count)
        answer += sum(total_count)
        break
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day10.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    # answer_1(input)
    answer_2(input)
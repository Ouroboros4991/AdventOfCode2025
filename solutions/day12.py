import re
import numpy as np
import copy

import networkx as nx
import matplotlib.pyplot as plt

import functools


def place_shape(grid, shape, start_coordinate):
    max_x = len(shape[0])
    max_y = len(shape)
    new_grid = copy.deepcopy(grid)
    for y in range(max_y):
        co_y = start_coordinate[1] + y
        if co_y >= len(grid):
            return None
        for x in range(max_x):
            co_x = start_coordinate[0] + x
            if co_x >= len(grid[0]):
                return None
            if shape[y][x] == "#":
                if grid[co_y][co_x] == "#":
                    # Overlaps with existing shape
                    return None
                new_grid[co_y][co_x] = "#"
    return new_grid

def find_possible_shape_placements(grid, s):
    max_x = len(grid[0])
    max_y = len(grid)
    possible_grid_configs = []
    for y in range(max_y):
        for x in range(max_x):
            new_grid = copy.deepcopy(grid)
            tmp_grid = place_shape(new_grid, s, [y, x])
            if tmp_grid:
                possible_grid_configs.append(tmp_grid)
    return possible_grid_configs

def recursion(quantaties, current_shape, grid, shape_input):
    if current_shape >= len(quantaties):
        return 1
    if not quantaties[current_shape]:
        return recursion(quantaties, current_shape+1, grid, shape_input)
    
    shape = shape_input[current_shape]
    
    max_x = len(shape[0])
    max_y = len(shape)
        
    possible_shape_configs = []

    tmp_array = shape
    for i in range(4):
        tmp_array = np.rot90(tmp_array)
        possible_shape_configs.append(tmp_array)
    possible_shape_configs.append(np.flip(shape, axis=0))
    possible_shape_configs.append(np.flip(shape, axis=1))
    unique_shapes = []
    for p_s in possible_shape_configs:
        if p_s not in unique_shapes:
            unique_shapes.append(p_s)
    
    possible_configs = 0
    possible_placements = [grid]
    for i in range(quantaties[current_shape]):
        new_possible_placements = []
        for g in possible_placements:
            for s in unique_shapes:
                possible_placements = find_possible_shape_placements(g, s)
                new_possible_placements.extend(possible_placements)
        possible_placements = new_possible_placements
    unique_configs = []
    for p in possible_placements:
        if p not in unique_configs:
            unique_configs.append(p)
    for p in unique_configs:
        possible_configs += recursion(quantaties, current_shape+1, p, shape_input)
    return possible_configs  
        

def answer_1(input: list):
    answer = 0
    shape_input = {}
    quantaties = []
    shape = []
    current_shape = None
    for line in input:
        if "x" in line:
            grid_size, q = line.split(":")
            grid_size = [int(x) for x in grid_size.split("x")]
            q = [int(x) for x in q.strip().split(" ")]
            quantaties.append((grid_size, q))
        elif ":" in line:
            current_shape = int(line.split(":")[0])
        elif not line:
            shape_input[current_shape] = np.array(shape)
            shape = []
        else:
            shape.append(list(line))
    
    for grid_size, q in quantaties:
        grid = []
        for _ in range(grid_size[1]):
            row = ["."] * grid_size[0]
            grid.append(row)
       
        possible_configs = recursion(q, 0, grid, shape_input)
        print(possible_configs)
        answer += possible_configs
        
    
    print("Answer 1", answer)


def answer_2(input: list):
    answer = 0
   
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day12.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    answer_1(input)
    answer_2(input)
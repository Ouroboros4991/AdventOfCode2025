import re
import numpy as np
import copy

import itertools
import functools

def answer_1(input: list):
    answer = 0
    input = [list(line) for line in input]        
    start_index = input[0].index("S")
    indexes = [start_index]
    for i in range(1, len(input)):
        line = input[i]
        for index in indexes:
            if line[index] == ".":
                line[index] = "|"
            elif line[index] == "^":
                answer += 1
                if index > 0:
                    line[index-1] = "|"
                if index < len(line) -1:
                    line[index+1] = "|"
        # for p_line in input:
        #     print("".join(p_line))
        # print("==========")
        indexes = [i for i, x in enumerate(line) if x == "|"]
    # answer = len(indexes)
    print("Answer 1", answer)
    
def explore_new_timelines(input: list, index: int, current_line: int, path):
    if current_line >= len(input):
        # for p_line in input:
        #     print("".join(p_line))
        # print("==========")
        return 1
    n_timelines = 0
    line = input[current_line]
    if line[index] == ".":
        new_index = index
        new_time_line = copy.deepcopy(input)
        new_time_line[current_line][new_index] = "|"
        new_path = path.copy()
        new_path.append(new_index)
        n_timelines += explore_new_timelines(new_time_line, new_index, current_line+1, new_path)
    elif line[index] == "^":
        if index > 0:
            new_index = index - 1
            new_time_line = copy.deepcopy(input)
            new_time_line[current_line][new_index] = "|"
            new_path = path.copy()
            new_path.append(new_index)
            n_timelines += explore_new_timelines(new_time_line, new_index, current_line+1, new_path)
        if index < len(line) - 1:
            new_index = index + 1
            new_time_line = copy.deepcopy(input)
            new_time_line[current_line][new_index] = "|"
            new_path = path.copy()
            new_path.append(new_index)
            n_timelines += explore_new_timelines(new_time_line, new_index, current_line+1, new_path)
    return n_timelines

# def answer_2(input: list):
#     answer = 0
#     input = [list(line) for line in input]       
#     input = input[:9] 
#     start_index = input[0].index("S")
#     answer = explore_new_timelines(input, start_index, 1, [start_index])
#     print("Answer 2", answer)
    


def answer_2(input: list):
    answer = 0
    input = [list(line) for line in input]        
    start_index = input[0].index("S")
    n_time_lines = [1] * len(input[0])
    start = len(input)-1
    for current_line in range(start, 0, -1):
        line = input[current_line]
        for index, char in enumerate(line):
            if char == "^":
                l_count = 0
                r_count = 0
                if index > 0:
                    l_count = n_time_lines[index - 1]
                if index < len(line) - 1:
                    r_count = n_time_lines[index + 1]
                count = r_count + l_count
                n_time_lines[index] = count
        # print(current_line, n_time_lines)
    print("Answer 2", n_time_lines[start_index])

# def answer_2(input: list):
#     answer = 0
#     input = [list(line) for line in input]        
#     start_index = input[0].index("S")
#     time_lines = [[start_index]]
#     for i in range(1, len(input)):
#         print(i)
#         line = input[i]
#         next_timelines = []
#         for indexes in time_lines:
#             for index in indexes:
#                 if line[index] == ".":
#                     # line[index] = "|"
#                     new_time_line = line.copy()
#                     new_time_line[index] = "|"
#                     next_timelines.append(new_time_line)
#                 elif line[index] == "^":
#                     answer += 1
#                     if index > 0:
#                         new_time_line = line.copy()
#                         new_time_line[index-1] = "|"
#                         next_timelines.append(new_time_line)
#                     if index < len(line) -1:
                        # new_time_line = line.copy()
                        # new_time_line[index+1] = "|"
                        # next_timelines.append(new_time_line)
#         time_lines = []
#         for t in next_timelines:
#             t_indexes = [i for i, x in enumerate(t) if x == "|"]
#             time_lines.append(t_indexes)
#     print("Answer 2", len(time_lines))

if __name__ == "__main__":
    with open("../input/day7.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    answer_1(input)
    answer_2(input)
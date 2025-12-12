import re
import numpy as np
import copy

import networkx as nx
import matplotlib.pyplot as plt

import functools


def recursion(current_node, device_mapping, path_taken, all_paths):
    if current_node == "out":
        all_paths.append(path_taken)
        return
    
    for node in device_mapping[current_node]:
        if node not in path_taken:
            new_path_taken = path_taken[:]
            new_path_taken.append(node)
            recursion(node, device_mapping, new_path_taken, all_paths)

def answer_1(input: list):
    answer = 0
    device_mapping = {}
    for line in input:
        input, output = line.split(":")
        input = input.strip()
        output = [o.strip() for o in output.strip().split(" ")]
        device_mapping[input] = output
    
    start_node = "you"
    path_taken = [start_node]
    all_paths = []
    recursion(start_node, device_mapping, path_taken, all_paths)
    answer = len(all_paths)
    
    print("Answer 1", answer)


# def recursion2(current_node, device_mapping, path_taken, all_paths):
#     if current_node == "out":
#         if "dac" in path_taken and "fft" in path_taken:
#             all_paths.append(path_taken)
#         return

#     for node in device_mapping[current_node]:
#         if node not in path_taken:
#             new_path_taken = path_taken[:]
#             new_path_taken.append(node)
#             recursion2(node, device_mapping, new_path_taken, all_paths)

# def answer_2(input: list):
#     answer = 0
#     device_mapping = {}
#     for line in input:
#         input, output = line.split(":")
#         input = input.strip()
#         output = [o.strip() for o in output.strip().split(" ")]
#         device_mapping[input] = output
    
#     start_node = "svr"
#     path_taken = [start_node]
#     all_paths = []
#     recursion2(start_node, device_mapping, path_taken, all_paths)
#     answer = len(all_paths)
    
#     print("Answer 2", answer)


DEVICE_MAPPING = {}

@functools.cache
def recursion2(current_node, end_node):
    if current_node == end_node:
        return 1

    total_paths = 0
    for node in DEVICE_MAPPING.get(current_node, []):
        total_paths += recursion2(node, end_node)
    return total_paths

def answer_2(input: list):
    answer = 0
    for line in input:
        input, output = line.split(":")
        input = input.strip()
        output = [o.strip() for o in output.strip().split(" ")]
        DEVICE_MAPPING[input] = output
    
    for possible_paths in [
        [
            ("svr", "fft"),
            ("fft", "dac"),
            ("dac", "out")
        ],
        [
            ("svr", "fft"),
            ("fft", "dac"),
            ("dac", "out")
        ]
    ]:
        sub_answer = 1
        for pair in possible_paths:
            start_node, end_node = pair
            paths = recursion2(start_node, end_node)
            sub_answer *= paths
    if sub_answer:
        print("Possible answer", sub_answer)
    # print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day11.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    # answer_1(input)
    answer_2(input)
import re
import numpy as np
import copy
import math

import itertools

def answer_1(input: list):
    answer = 0
    coordinates = []
    for line in input:
        coordinates.append([int(i) for i in line.split(",")])
    
    distances = []
    for co_pair in itertools.combinations(coordinates, 2):
        dist = math.dist(*co_pair)
        distances.append((dist, co_pair))
    
    sorted_distances = sorted(
        distances, 
        key=lambda x: x[0]
    )
    
    circuits = {}
    co_circuits_mapping = {}
    for i, co in enumerate(coordinates):
        circuits[i] = [co]
        key = ",".join([str(c) for c in co])
        co_circuits_mapping[key] = i
    
    top_x = 1000
    for i in range(top_x):
        d, co_pair = sorted_distances[i]
        key1 = ",".join([str(c) for c in co_pair[0]])
        key2 = ",".join([str(c) for c in co_pair[1]])
        circuit_1 = co_circuits_mapping[key1]
        circuit_2 = co_circuits_mapping[key2]
        
        # update mapping
        if circuit_1 != circuit_2:
            circuits[circuit_1].extend(circuits[circuit_2])
            for co in circuits[circuit_2]:
                co_key = ",".join([str(c) for c in co])
                co_circuits_mapping[co_key] = circuit_1

            del circuits[circuit_2]
    
    largest_circuits = [0]*3    
    for c_id, coordinates in circuits.items():
        len_c = len(coordinates)
        for i in range(3):
            if len_c > largest_circuits[i]:
                largest_circuits[i] = len_c
                break
    answer = 1
    for d in largest_circuits:
        answer *= d
    print("Answer 1", answer)

def answer_2(input: list):
    answer = 0
    coordinates = []
    for line in input:
        coordinates.append([int(i) for i in line.split(",")])
    
    distances = []
    for co_pair in itertools.combinations(coordinates, 2):
        dist = math.dist(*co_pair)
        distances.append((dist, co_pair))
    
    sorted_distances = sorted(
        distances, 
        key=lambda x: x[0]
    )
    
    circuits = {}
    co_circuits_mapping = {}
    for i, co in enumerate(coordinates):
        circuits[i] = [co]
        key = ",".join([str(c) for c in co])
        co_circuits_mapping[key] = i

    last_x_coordinates = []    
    i = 0
    while(len(list(circuits.keys())) > 1):
        d, co_pair = sorted_distances[i]
        key1 = ",".join([str(c) for c in co_pair[0]])
        key2 = ",".join([str(c) for c in co_pair[1]])
        circuit_1 = co_circuits_mapping[key1]
        circuit_2 = co_circuits_mapping[key2]
        
        # update mapping
        if circuit_1 != circuit_2:
            circuits[circuit_1].extend(circuits[circuit_2])
            for co in circuits[circuit_2]:
                co_key = ",".join([str(c) for c in co])
                co_circuits_mapping[co_key] = circuit_1

            del circuits[circuit_2]
            last_x_coordinates = [co_pair[0][0], co_pair[1][0]]
        i += 1
        # print(circuits.keys())
    
    print(last_x_coordinates)
    answer = 1
    for d in last_x_coordinates:
        answer *= d
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day8.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    # answer_1(input)
    answer_2(input)
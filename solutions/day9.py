import re
import numpy as np
import copy
import math
import shapely

import itertools

def answer_1(input: list):
    answer = 0
    coordinates = []
    for line in input:
        coordinates.append([int(i) for i in line.split(",")])
    
    areas = []
    for co_pair in itertools.combinations(coordinates, 2):
        area = (abs(co_pair[0][0]-co_pair[1][0]) + 1 )* (abs(co_pair[0][1]-co_pair[1][1]) + 1) # Make it inclusive
        areas.append((area, co_pair))
    sorted_areas = sorted(
        areas, 
        key=lambda x: x[0]
    )
    answer = sorted_areas[-1][0]

    print("Answer 1", answer)

def answer_2(input: list):
    answer = 0
    coordinates = []
    for line in input:
        coordinates.append([int(i) for i in line.split(",")])
    
    shape = shapely.Polygon(coordinates)
    areas = []
    for co_pair in itertools.combinations(coordinates, 2):
        # Convert to shapely rectangle
        rectangle = shapely.box(
            min(co_pair[0][0], co_pair[1][0]),
            min(co_pair[0][1], co_pair[1][1]),
            max(co_pair[0][0], co_pair[1][0]),
            max(co_pair[0][1], co_pair[1][1]),
        )
        area = (abs(co_pair[0][0]-co_pair[1][0]) + 1 )* (abs(co_pair[0][1]-co_pair[1][1]) + 1) # Make it inclusive       
        if rectangle.within(shape):
            areas.append((area, co_pair))
    sorted_areas = sorted(
        areas, 
        key=lambda x: x[0]
    )
    answer = sorted_areas[-1][0]
    
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day9.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    answer_1(input)
    answer_2(input)
import re
import numpy as np
import copy

def check_surrounding(matrix, x,y):
    n_items = 0
    max_y, max_x = matrix.shape
    if y > 0:
        for i in range(max(0, x-1,), min(x+2, max_x)):
            if matrix[y-1][i] == "@":
                # print(x, y-1)
                n_items += 1
    for i in range(max(0, x-1,), min(x+2, max_x)):
        if matrix[y][i] == "@" and i != x:
            # print(x, y)
            n_items += 1
    if y < max_y -1:
        for i in range(max(0, x-1,), min(x+2, max_x)):
            if matrix[y+1][i] == "@":
                # print(x, y+1)
                n_items += 1
    return n_items
            

def answer_1(matrix: list):
    answer = 0
    max_y, max_x = matrix.shape
    for y in range(max_y):
        for x in range(max_x):
            if matrix[y][x] == "@":
                n_items = check_surrounding(matrix, x, y)
                # print(x,y, n_items)
                if n_items < 4:
                    answer += 1
    # print(check_surrounding(matrix, 4, 1))
    print("Answer 1", answer)

def answer_2(matrix: list):
    answer = 0
    has_removed = True
    max_y, max_x = matrix.shape
    while has_removed:
        sub_answer = 0
        has_removed = False
        new_matrix = copy.deepcopy(matrix.copy())
        for y in range(max_y):
            for x in range(max_x):
                if matrix[y][x] == "@":
                    n_items = check_surrounding(matrix, x, y)
                    # print(x,y, n_items)
                    if n_items < 4:
                        answer += 1
                        sub_answer += 1
                        new_matrix[y][x] = "x"
                        has_removed = True
        matrix = copy.deepcopy(new_matrix.copy())
        # print(sub_answer)
        # print(matrix)
        # print("-----------")
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day4.txt") as file:
        lines = [line.strip() for line in file]
    matrix = [list(line.strip()) for line in lines]
    matrix = np.array(matrix)
    answer_1(matrix)
    answer_2(matrix)
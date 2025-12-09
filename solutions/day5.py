import re
import numpy as np
import copy

            

def answer_1(input: list):
    answer = 0
    
    ranges = []
    ingredients = []
    for line in input:
        if line:
            if "-" in line:
                ranges.append(line.split("-"))
            else:
                ingredients.append(int(line))
    for i in ingredients:
        is_fresh = False
        for n1, n2 in ranges:
            if int(n1) <= i <= int(n2):
                is_fresh = True
                break
        if is_fresh:
            answer += 1
    print("Answer 1", answer)

def answer_2(input: list):
    answer = 0
    ranges = []
    ingredients = []
    for line in input:
        if line:
            if "-" in line:
                i1, i2 = line.split("-")
                ranges.append([int(i1), int(i2)])
            else:
                ingredients.append(int(line))
    
    ranges = sorted(
        ranges, 
        key=lambda x: x[0]
    )

    new_ranges_subset = []
    for index, r in enumerate(ranges):
        n1, n2 = r
        n1 = int(n1)
        n2 = int(n2)
        for i in range(len(new_ranges_subset)):
            s1, s2 = new_ranges_subset[i]
            if s1 <= n2 and n2 <= s2:
                new_ranges_subset[i] = [s1, s2]
                break
            elif n1 <= s1 and s2 <= n2:
                new_ranges_subset[i] = [n1,n2]
                break
            elif n1 <= s1 and s1 <= n2 <= s2:
                new_ranges_subset[i] = [n1, s2]
                break
            elif s1 <= n1 <= s2 and s2 <= n2:
                new_ranges_subset[i] = [s1,n2]
                break
        else:
            new_ranges_subset.append([n1,n2])
    
    # new_ranges_subset = sorted(
    #     new_ranges_subset, 
    #     key=lambda x: x[0]
    # )
    # has_switched = True
    # while has_switched:
    #     for i in range(len(new_ranges_subset)-1):
    #         r1, r2 = new_ranges_subset[i]
    #         s1, s2 = new_ranges_subset[i+1]
    #         if n1 <= s1 and s1 <= n2 <= s2:
    #             new_ranges_subset[i] = [n1, s2]
    #             del new_ranges_subset[i+1]
    #             break
    #         elif s1 <= n1 <= s2 and s2 <= n2:
    #             new_ranges_subset[i] = [s1,n2]
    #             del new_ranges_subset[i+1]
    #             break
    #     else:
    #         has_switched = False
            
        
    for r1, r2 in new_ranges_subset:
        answer += (r2 - r1 ) + 1
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day5.txt") as file:
        lines = [line.strip() for line in file]
    input = [line.strip() for line in lines]
    answer_1(input)
    answer_2(input)
import re
import numpy as np
import copy

            

def answer_1(input: list):
    answer = 0
    problems = []
    for line in input:
        line_arr = []
        for i in line.strip().split(" "):
            if i:
                if i not in ("*", "+"):
                    i = int(i)
                line_arr.append(i)
        problems.append(line_arr)
    problems = np.array(problems)
    problems = problems.transpose()
    for problem in problems:
        operation = problem[-1]
        if operation == "+":
            sub_answer = 0
            for i in problem[:-1]:
                sub_answer = sub_answer + int(i)
        elif operation == "*":
            sub_answer = 1
            for i in problem[:-1]:
                sub_answer = sub_answer * int(i)
        else:
            raise Exception(f"Unknown operator found: {operation}")
        answer += sub_answer
    print("Answer 1", answer)

def answer_2(input: list):
    answer = 0
    problems = []
    operations = []
    for item in input[-1].split(" "):
        if item:
            operations = [item] + operations    
    
    problems = [list(line) for line in input[:-1]]
    rewritten_problems = []
    new_problem = []
    max_x = max([len(p) for p in problems])
    for x in range(max_x-1, -1, -1):
        new_digit = ""
        for y in range(len(problems)):
            new_digit += problems[y][x]
        new_digit = new_digit.strip()
        if not new_digit:
            # Start new problem
            rewritten_problems.append(new_problem)
            new_problem = []
        else:
            new_problem.append(int(new_digit))
    rewritten_problems.append(new_problem)
    for i, p in enumerate(rewritten_problems):
        p.append(operations[i])
    for problem in rewritten_problems:
        operation = problem[-1]
        if operation == "+":
            sub_answer = 0
            for i in problem[:-1]:
                sub_answer = sub_answer + int(i)
        elif operation == "*":
            sub_answer = 1
            for i in problem[:-1]:
                sub_answer = sub_answer * int(i)
        else:
            raise Exception(f"Unknown operator found: {operation}")
        answer += sub_answer
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day6.txt") as file:
        lines = [line.replace("\n", "") for line in file]
    input = [line.replace("\n", "") for line in lines]
    answer_1(input)
    answer_2(input)
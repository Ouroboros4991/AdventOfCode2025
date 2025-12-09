import re

def answer_1(banks: list):
    answer = 0
    for bank in banks:
        bank_list = list(bank)
        first_number = max(bank_list[:-1])
        index_first = bank_list.index(first_number)
        second_number = max(bank_list[index_first+1:])
        final_number = int(f"{first_number}{second_number}")
        answer += final_number
    print("Answer 1", answer)
         

def find_number(n:int, bank_list: list):
    if n == 0:
        return ""
    if n == 1:
        digit = max(bank_list)
    else:
        remaining_chars = n-1
        digit = max(bank_list[:-remaining_chars])
    index = bank_list.index(digit)
    rest_number = find_number(n-1, bank_list[index+1:])
    return f"{digit}{rest_number}"
    

def answer_2(banks: list):
    answer = 0
    for bank in banks:
        bank_list = list(bank)
        final_number = int(find_number(12, bank_list))
        answer += final_number
    print("Answer 2", answer)

if __name__ == "__main__":
    with open("../input/day3.txt") as file:
        lines = [line.strip() for line in file]
    banks = [bank.strip() for bank in lines]
    answer_1(banks)
    answer_2(banks)
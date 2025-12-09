import re

def answer_1(ids: list):
    bad_ids = []
    for id in ids:
        id1,id2 = id.split('-')
        for i in range(int(id1), int(id2)):
            id_str = str(i)
            half = len(id_str)//2
            if id_str[:half] == id_str[half:]:
                bad_ids.append(i)
    print("Answer 1", sum(bad_ids))
         
         
def answer_2(ids: list):
    bad_ids = []
    for id in ids:
        id1,id2 = id.split('-')
        for i in range(int(id1), int(id2)+1):
            id_str = str(i)
            for n in range(2, len(id_str)+1):
                substring_len = len(id_str)//n
                substring = id_str[:substring_len]
                if id_str == substring * n:
                    bad_ids.append(i)
                    break
    print("Answer 2", sum(bad_ids))       

if __name__ == "__main__":
    with open("../input/day2.txt") as file:
        lines = [line.strip() for line in file]
    ids = [id.strip() for id in lines[0].split(',')]
    # answer_1(ids)
    answer_2(ids)
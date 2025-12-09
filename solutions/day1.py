class Dial:
    def __init__(self, length):
        self.length = length
        self.possible_choises = [i for i in range(length)]
        self.current_pos = length//2
        self.zero_count = 0
    
    def get(self):
        return self.possible_choises[self.current_pos]

    def rotate_left(self):
        new_pos = self.current_pos - 1
        if new_pos == -1:
            new_pos = self.length - 1
        self.current_pos = new_pos
        if self.current_pos == 0:
            self.zero_count += 1
    
    def rotate_x_left(self, x):
        for i in range(x):
            self.rotate_left()
    
    def rotate_right(self):
        new_pos = self.current_pos + 1
        if new_pos == self.length:
            new_pos = 0
        self.current_pos = new_pos
        if self.current_pos == 0:
            self.zero_count += 1
    
    def rotate_x_right(self, x):
        for i in range(x):
            self.rotate_right()


if __name__ == "__main__":
    dial = Dial(100)
    with open("../input/day1.txt") as file:
        lines = [line.strip() for line in file]
    
    answer_1 = 0
    for line in lines:
        # print(line)
        direction = line[0]
        rotations = int(line[1:])
        if direction == "L":
            dial.rotate_x_left(rotations)
        else:
            dial.rotate_x_right(rotations)
        state = dial.get()
        if state == 0:
            answer_1 += 1
        # print( dial.zero_count)
        # print("========")
    print("Answer 1", answer_1)
    print("Answer 2", dial.zero_count)
# 
# Day 01 assignment: https://adventofcode.com/2025/day/1
#
from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1

def get_direction(token: str) -> Direction:
    direction = token[0]
    if (direction == "L"):
        return Direction.Left
    else:
        return Direction.Right

def get_directional_value(token: str) -> int:
    value_as_str = token.rstrip()[1:]
    if (get_direction(token) == Direction.Left):
        return -int(value_as_str)
    return int(value_as_str)

def get_value(token: str) -> int:
    value = token.rstrip()[1:]
    return int(value)

def part_one_solution() -> int:
    position = 50
    stopped_on_zero = 0
    with open("./input.txt", "r") as input_file:
        for line in input_file.readlines():
            position += get_directional_value(line)
            position %= 100
            if (position == 0):
                stopped_on_zero += 1
        input_file.close()
    return stopped_on_zero

def part_two_solution() -> int:
    position = 50
    passed_through_zero = 0
    stopped_on_zero_previous_turn = False
    with open("./input.txt", "r") as input_file:
        for line in input_file.readlines():
            value = get_value(line)
            direction = get_direction(line)
            passed_through_zero += value // 100
            value %= 100
            
            if (direction == Direction.Right):
                position += value
            else:
                position -= value
                
            if ((position <= 0 or position >= 100) and not stopped_on_zero_previous_turn):
                passed_through_zero += 1
                
            position %= 100
            
            if (position == 0):
                stopped_on_zero_previous_turn = True
            else:
                stopped_on_zero_previous_turn = False
                
        input_file.close()
    return passed_through_zero

def main() -> None:
    print("============ Day 01 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
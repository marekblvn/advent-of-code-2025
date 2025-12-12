# 
# Day 06 assignment: https://adventofcode.com/2025/day/6
#

import os

def apply_operation_to_value(base_value: int, operation_string: str, operation_value: int) -> int:
    if (operation_string == "+"):
        return base_value + operation_value
    elif (operation_string == "*"):
        return base_value * operation_value
    else:
        return base_value

def part_one_solution() -> int:
    total = 0
    input_file_path = "./input.txt"
    try:
        with open(input_file_path, "rb") as input_file:
            file_size = os.path.getsize(input_file_path)
            line_size_b = len(input_file.readline())
            input_file.seek(-line_size_b, 2)
            operators = input_file.read(line_size_b).decode().strip().split()
            columns = [0 if op == "+" else 1 for op in operators]
            input_file.seek(0, 0)
            for line_bytes in input_file.readlines(file_size - line_size_b):
                line = line_bytes.decode()
                tokens = [int(t) for t in line.strip().split()]
                for i in range(len(tokens)):
                    columns[i] = apply_operation_to_value(columns[i], operators[i], tokens[i])
            input_file.close()
        total = sum(columns)
    except Exception as err:
        print(err)
    return total

def part_two_solution():
    pass


def main() -> None:
    print("============ Day 06 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
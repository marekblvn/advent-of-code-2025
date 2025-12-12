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
    if not os.path.exists(input_file_path):
        print(f"Could not find file: '{input_file_path}'")
        return -1
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
    return total


def part_two_solution() -> int:
    total = 0
    input_file_path = "./input.txt"
    if not os.path.exists(input_file_path):
        print(f"Could not find file '{input_file_path}'")
        return -1
    with open(input_file_path, "rb") as input_file:
        input_file_size = os.path.getsize(input_file_path)
        line_size_b = len(input_file.readline())
        input_file.seek(-line_size_b, 2)
        operators_raw = input_file.read(line_size_b)
        operators = operators_raw.decode().strip().split()
        columns = [1 if op == "*" else 0 for op in operators]
        input_file.seek(0,0)
        j = 0
        for i in range(line_size_b):
            input_file.seek(i, 0)
            byte_token = b""
            while input_file.tell() < input_file_size - line_size_b:
                byte_token += input_file.read(1)
                input_file.seek(line_size_b - 1, 1)
            token = byte_token.decode().strip()
            if (len(token) <= 0):
                j += 1
            else:
                columns[j] = apply_operation_to_value(columns[j], operators[j], int(token))
            byte_token = b""
        input_file.close()
    total = sum(columns)
    return total


def main() -> None:
    print("============ Day 06 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
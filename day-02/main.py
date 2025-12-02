# 
# Day 02 assignment: https://adventofcode.com/2025/day/2
#
from re import finditer, match, compile
from typing import Any, Pattern

repeated_sequence_pattern = compile("^(\\d+)\\1$")
repeated_sequence_pattern_extended = compile("^(\\d+)\\1+$")

def parse_group(group: tuple[str | Any, ...]) -> tuple[int, int]:
    if (len(group) != 3):
        raise IndexError(f"Unexpected tuple length. Expected 3, found {len(group)}")
    return (int(group[1]), int(group[2]))

def find_repeated_seq_sum(interval: tuple[int, int], pattern: Pattern[str]) -> int:
    s = 0
    for i in range(interval[0], interval[1] + 1):
        m = match(pattern, str(i))
        if (m):
            s += i
    return s

def part_one_solution() -> int:
    range_pattern = r"((\d+)\-(\d+))\,?"
    res = 0
    with open("./input.txt", "r") as input_file:
        for m in finditer(range_pattern, input_file.readline()):
            group = m.groups()
            try:
                r = parse_group(group)
            except Exception as e:
                print(f"Error: {e}\nQuitting...")
                exit(1)
            res += find_repeated_seq_sum(r, repeated_sequence_pattern);
        input_file.close()
    return res

def part_two_solution() -> int:
    range_pattern = r"((\d+)\-(\d+))\,?"
    res = 0
    with open("./input.txt", "r") as input_file:
        for m in finditer(range_pattern, input_file.readline()):
            group = m.groups()
            try:
                r = parse_group(group)
            except Exception as e:
                print(f"Error: {e}\nQuitting...")
                exit(1)
            res += find_repeated_seq_sum(r, repeated_sequence_pattern_extended);
        input_file.close()
    return res

def main() -> None:
    print("============ Day 02 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
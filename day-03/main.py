# 
# Day 03 assignment: https://adventofcode.com/2025/day/3
#

# 1. Pokud je prvek na pozici j > než prvek na pozici i a zároveň prvek na pozici j není poslední, pak se i musí přesunout na pozici j
# 2. V každé iteraci přesuneme j o jednu pozici dopředu

def get_largest_joltage(battery_line: str) -> int:
    a,b = battery_line[0], battery_line[1]
    for i in range(1, len(battery_line)):
        if (battery_line[i] > b):
            b = battery_line[i]
        if (battery_line[i] > a and i < len(battery_line) - 1):
            a = battery_line[i]
            b = battery_line[i+1]
    return int(a+b)

def part_one_solution() -> int:
    total_joltage = 0
    with open("./input.txt", "r") as input_file:
        for line in input_file.readlines():
            lj = get_largest_joltage(line.rstrip()) 
            total_joltage += lj
        input_file.close()
    return total_joltage

def get_largest_joltage_ext(battery_line: str) -> int:
    """
    Greedy algorithm
    """
    r = len(battery_line) - 12
    result: list[int] = []
    for battery in battery_line:
        current = int(battery)
        while (len(result) > 0 and current > result[-1] and r > 0):
            result.pop()
            r -= 1
        result.append(current)
    if (r > 0):
        result = result[:-r]
    return int("".join(map(str, result)))

def part_two_solution() -> int:
    total_joltage = 0
    with open("./input.txt", "r") as input_file:
        for line in input_file.readlines():
            total_joltage += get_largest_joltage_ext(line.rstrip())
        input_file.close()
    return total_joltage

def main() -> None:
    print("============ Day 03 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
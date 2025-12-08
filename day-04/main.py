# 
# Day 04 assignment: https://adventofcode.com/2025/day/4
#

def get_adjacent_rolls(x: int,y: int, grid: list[str]) -> int:
    rolls = 0
    adjacent = [
        grid[y-1][x-1], grid[y-1][x], grid[y-1][x+1],
        grid[y][x-1], grid[y][x+1],
        grid[y+1][x-1], grid[y+1][x], grid[y+1][x+1],
    ]
    for cell in adjacent:
        if cell == "@" or cell == "X":
            rolls += 1
    return rolls

def mark_roll_for_removal(x: int, y: int, grid: list[str]) -> None:
    grid[y] = grid[y][:x] + "X" + grid[y][x+1:]

def remove_old_rolls(grid: list[str]) -> list[str]:
    return [line.replace("X",".") for line in grid]

def part_one_solution() -> int:
    total_accessible = 0
    lines = []
    with open("./input.txt", "r") as input_file:
        lines = [l.rstrip() for l in input_file.readlines()]
        input_file.close()
    Y = len(lines)
    X = len(lines[0])
    lines.insert(0, "." * X)
    lines.append("." * X)
    lines = ["." + line + "." for line in lines]
    for y in range(1, Y+1):
        for x in range(1, X+1):
            if (lines[y][x] == "."):
                continue
            adj_rolls = get_adjacent_rolls(x,y,lines)
            if (adj_rolls < 4):
                total_accessible += 1
    return total_accessible

def part_two_solution() -> int:
    rolls_removed = 0
    removed_last_turn = 1
    lines = []
    with open("./input.txt", "r") as input_file:
        lines = [l.rstrip() for l in input_file.readlines()]
        input_file.close()
    Y = len(lines)
    X = len(lines[0])
    lines.insert(0, "." * X)
    lines.append("." * X)
    lines = ["." + line + "." for line in lines]
    while (removed_last_turn > 0):
        removed_last_turn = 0
        for y in range(1, Y+1):
            for x in range(1, X+1):
                if (lines[y][x] != "@"):
                    continue
                adj_rolls = get_adjacent_rolls(x,y,lines)
                if (adj_rolls < 4):
                    removed_last_turn += 1
                    mark_roll_for_removal(x,y,lines)
        lines = remove_old_rolls(lines)
        rolls_removed += removed_last_turn
    return rolls_removed


def main() -> None:
    print("============ Day 03 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
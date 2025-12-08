# 
# Day 05 assignment: https://adventofcode.com/2025/day/5
#

# Použít stromy pro prohledání intervalů - nebudeme muset zkoušet každý interval zvlášť -----> INTERVAL TREE

# TODO: Implement own IntervalTree

from intervaltree import IntervalTree, Interval

def part_one_solution() -> int:
    available_ids = 0
    with open("./input.txt", "r") as input_file:
        [ranges, id_strings] = input_file.read().split("\n\n")
        input_file.close()
    lines = [l.split("-") for l in ranges.splitlines()]
    ranges = [Interval(int(r[0]) - 1, int(r[1]) + 1) for r in lines]
    interval_tree = IntervalTree(ranges)
    ids = [int(id) for id in id_strings.splitlines()]
    for id in ids:
        if interval_tree.overlaps_point(id): # type: ignore
            available_ids += 1
    return available_ids

def part_two_solution() -> int:
    unique_ids = 0
    with open("./input.txt", "r") as input_file:
        [ranges, _] = input_file.read().split("\n\n")
        input_file.close()
    lines = [l.split("-") for l in ranges.splitlines()]
    ranges = [Interval(int(r[0]), int(r[1]) + 1) for r in lines]
    interval_tree = IntervalTree(ranges)
    interval_tree.merge_overlaps() # type: ignore
    for interval in interval_tree: # type: ignore
        unique_ids += interval.length() # type: ignore
    return unique_ids # type: ignore


def main() -> None:
    print("============ Day 05 ============")
    part_one_sol = part_one_solution()
    print(f"Part 1 solution: {part_one_sol}")
    part_two_sol = part_two_solution()
    print(f"Part 2 solution: {part_two_sol}")

if __name__ == "__main__":
    main()
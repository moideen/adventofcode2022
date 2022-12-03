# Advent of Code 2022 - Day 3
# Moideen Kalladi

import itertools

# open and read input file
with open("input.txt", "r") as f:
    lines = f.read().split("\n")

# quick function to get priority of any item
priority = lambda x: ord(x) - 96 if x.islower() else ord(x) - 38

priority_sum = 0

# avoid blank string at the end
for line in lines[:-1]:
    # split into two compartments
    line1 = line[: int(len(line) / 2)]
    line2 = line[int(len(line) / 2) :]

    # get common item
    common = "".join(set(line1).intersection(set(line2)))

    priority_sum += priority(common)

print(f"Priority Sum: {priority_sum}")

# part 2

priority_sum_2 = 0

# grab groups of three lines:
for i in range(0, len(lines) - 1, 3):
    group = lines[:-1][i : i + 3]
    common = "".join(
        set(group[0]).intersection(set(group[1]).intersection(set(group[2])))
    )
    priority_sum_2 += priority(common)

print(f"Priority Sum 2: {priority_sum_2}")

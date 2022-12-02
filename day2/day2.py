# Advent of Code 2022 - Day 2
# Moideen Kalladi

# open and read input file
with open("input.txt", "r") as f:
    lines = f.read().split("\n")

# easier just to map out all 9 combinations

score_map = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
    "": 0,  # in case of a blank at the end
}

total_score = sum([score_map[line] for line in lines])

print(f"Total score: {total_score}")

# part 2

score_map_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
    "": 0,  # in case of a blank at the end
}

total_score_2 = sum([score_map_2[line] for line in lines])

print(f"Total score 2: {total_score_2}")

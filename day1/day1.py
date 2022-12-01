# Advent of Code 2022 - Day 1 Problem 1
# Moideen Kalladi

# open and read input file
with open("input.txt", "r") as f:
	lines = f.read().split("\n")

# list to hold calorie counts and integer to hold current count
cals = []
current_cals = 0

# loop through and count up calories
for line in lines:
	if line == "":
		cals.append(current_cals)
		current_cals = 0
	else:
		current_cals += int(line)

# part 1 - print maximum calories
print(f"Maximum calories: {max(cals)}")

# part 2 - print sum of top 3 calories
print(f"Sum of three larges calories: {sum(sorted(cals, reverse=True)[:3])}")
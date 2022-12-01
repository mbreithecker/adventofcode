lines = open('input.txt', 'r').readlines()

positions = [int(p) for p in lines[0].split(",")]

# part one
costs = 10e20
optimal_height = 0

for height in range(max(positions)):
    current_cost = 0
    # calculate cost for height
    for p in positions:
        current_cost += abs(p-height)

    # check if the current height-costs are the new minimum
    if current_cost <= costs:
        costs = current_cost
        optimal_height = height

cost = 0
for p in positions:
    cost += abs(p-optimal_height)

print("Part 1:", cost)

# part two

costs = 10e20
optimal_height = 0

for height in range(max(positions)):
    current_cost = 0
    for p in positions:
        # use Gauss sum law, i.e. sum sum_{k=1}^n k = n (n+1) / 2
        current_cost += int(abs(p-height) * (abs(p-height)+1) / 2)

    # check if the current height-costs are the new minimum
    if current_cost <= costs:
        costs = current_cost
        optimal_height = height

cost = 0
for p in positions:
    cost += int(abs(p-optimal_height) * (abs(p-optimal_height)+1) / 2)

print("Part 2:", cost)

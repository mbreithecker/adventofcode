lines = open('input.txt', 'r').readlines()

fish = [int(p) for p in lines[0].split(",")]

# part one (algorithm is too slow for part two)
for day in range(0, 80):
    for i in range(len(fish)):
        fish[i] -= 1  # decrease timer for each fish
        if fish[i] == -1:
            fish[i] = 6  # reset fish
            fish.append(8)  # spawn new fish

print("Part 1: ", len(fish))

# part two (faster algorithm, group fish with same properties (timers))
fish = [int(p) for p in lines[0].split(",")]

# the position represents the current time, and the value represents the amount of fish with this timer value
fishShift = [0]*9

# init fishShift array
for f in fish:
    fishShift[f] += 1

for day in range(0, 256):
    newShift = [0]*9
    for i in range(8):
        # decrease timer for every fish by shifting the array
        newShift[i] = fishShift[i+1]

    newShift[6] += fishShift[0]  # reset zero fish-timer to 6 days
    newShift[8] = fishShift[0]  # spawn new fish
    fishShift = newShift

print("Part 2: ", sum(fishShift))

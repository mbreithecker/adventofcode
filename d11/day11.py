lines = open('input.txt', 'r').readlines()
arr = [[int(c) for c in line.strip()] for line in lines]

flashed_count = 0
for step in range(1000):
    # increase energy of all octopus
    for y in range(len(arr)):
        for x in range(len(arr)):
            arr[y][x] += 1

    flag_flashed = True
    # repeat until no flashes appear any more
    while flag_flashed:
        flag_flashed = False
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x] > 9:
                    # flash
                    flag_flashed = True
                    flashed_count += 1
                    # increment surrounding octopus
                    if y > 0: arr[y-1][x] += 1
                    if y+1 < len(arr): arr[y+1][x] += 1
                    if x > 0: arr[y][x-1] += 1
                    if x+1 < len(arr[0]): arr[y][x+1] += 1
                    if y > 0 and x > 0: arr[y-1][x-1] += 1
                    if y+1 < len(arr) and x+1 < len(arr[0]): arr[y+1][x+1] += 1
                    if x > 0 and y+1 < len(arr): arr[y+1][x-1] += 1
                    if y > 0 and x+1 < len(arr[0]): arr[y-1][x+1] += 1
                    # Make it impossible for current octopus to flash again.
                    # And octopus is marked because it has a value < 0
                    arr[y][x] = -100000

    # counter for part two
    value_belowZero_counter = 0

    # set all fields with value < 0 to zero
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] <= 0:
                value_belowZero_counter += 1
                arr[y][x] = 0

    if step == 99:
        print("Part 1:", flashed_count)

    if value_belowZero_counter == len(arr) ** 2:
        print("Part 2: ", step+1)
        break


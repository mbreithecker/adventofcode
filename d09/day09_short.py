import numpy as np

lines = open('input.txt', 'r').readlines()

arr = list()
# parse input as 2d-integer lists and add border of 9
arr.append([9] * (len(lines[0]) + 1))
arr += [[9] + [int(s) for s in line.strip()] + [9] for line in lines]
arr.append([9] * (len(lines[0]) + 1))

# part one
low_counter = 0
for x in range(1, len(arr) - 1):
    for y in range(1, len(arr[0]) - 1):
        if arr[x - 1][y] > arr[x][y] and arr[x + 1][y] > arr[x][y] and arr[x][y - 1] > arr[x][y] and arr[x][y + 1] > arr[x][y]:
            low_counter += arr[x][y] + 1

print("Part 1: ", low_counter)

# part two
def mark_neighbors(arr, x, y, marker):
    if arr[x][y] < 9:
        arr[x][y] = marker
        mark_neighbors(arr, x + 1, y, marker)
        mark_neighbors(arr, x - 1, y, marker)
        mark_neighbors(arr, x, y + 1, marker)
        mark_neighbors(arr, x, y - 1, marker)


# mark basins: count starting at 10
latest_marker_number = 10
for x in range(1, len(arr) - 1):
    for y in range(1, len(arr[0]) - 1):

        # dont mark nines as they don't belong to basins
        if arr[x][y] == 9:
            continue

        marker_number = latest_marker_number
        # check if neighbor is already part of a basin
        for neighbor in [arr[x - 1][y], arr[x + 1][y], arr[x][y - 1], arr[x][y + 1]]:
            if neighbor >= 10:
                marker_number = neighbor
                break
        else:
            latest_marker_number += 1

        mark_neighbors(arr, x, y, marker_number)

# count elements of basins
marker_score = dict()
for x in range(1, len(arr) - 1):
    for y in range(1, len(arr[0]) - 1):
        if arr[x][y] != 9:
            marker_score.setdefault(arr[x][y], 0)
            marker_score[arr[x][y]] += 1

print("Part 2: ", np.prod(sorted(marker_score.values())[-3:]))

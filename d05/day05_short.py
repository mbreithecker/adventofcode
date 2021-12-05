lines = open('input.txt', 'r').readlines()

grid1 = dict() # grid for part one
grid2 = dict() # grid for part two
for line in lines:
    # get coordinates from string
    (x1, y1, x2, y2) = [int(coord) for coord_string in line.split(" -> ") for coord in coord_string.split(",")]
    deltaX = x2-x1
    deltaY = y2-y1
    maxNorm = max(abs(deltaX), abs(deltaY))

    for t in range(0, maxNorm + 1):
        # parametrisation for line
        x = x1 + int(deltaX/maxNorm * t)
        y = y1 + int(deltaY/maxNorm * t)
        # increment grid for part 2
        grid2.setdefault((x, y), 0)
        grid2[(x, y)] += 1
        # if lines are parallel to x/y - axis, also increase part one
        if deltaY == 0 or deltaX == 0:
            grid1.setdefault((x, y), 0)
            grid1[(x, y)] += 1

print("Part 1: ", sum([val >= 2 for val in grid1.values()]))
print("Part 2: ", sum([val >= 2 for val in grid2.values()]))

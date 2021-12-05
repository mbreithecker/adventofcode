lines = open('input.txt', 'r').readlines()

# part one
grid = dict()
for line in lines:
    # extract coord
    (x1, y1, x2, y2) = [int(coord) for coord_string in line.split(" -> ") for coord in coord_string.split(",")]
    # parallel to x-axis
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            if (x1, y) not in grid:
                grid[(x1, y)] = 0

            grid[(x1, y)] += 1

    # parallel to y-axis
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            if (x, y1) not in grid:
                grid[(x, y1)] = 0

            grid[(x, y1)] += 1

highest_count = 0
for val in grid.values():
    if val >= 2:
        highest_count += 1

print(highest_count)

# part two
grid = dict()
for line in lines:
    (x1, y1, x2, y2) = [int(coord) for coord_string in line.split(" -> ") for coord in coord_string.split(",")]
    # parallel to x-axis
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) not in grid:
                grid[(x1, y)] = 0

            grid[(x1, y)] += 1

    # parallel to y-axis
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) not in grid:
                grid[(x, y1)] = 0

            grid[(x, y1)] += 1

    else:
        # check for diagonal
        for diag_counter in range(0, max(x1, x2)-min(x1, x2)+1):
            signX = -1 if x1 > x2 else 1 # determine direction to move
            signY = -1 if y1 > y2 else 1 # determine direction to move
            x = x1 + signX * diag_counter
            y = y1 + signY * diag_counter

            if (x,y) not in grid:
                grid[(x,y)] = 0

            grid[(x,y)] += 1

highest_count = 0
for val in grid.values():
    if val >= 2:
        highest_count += 1

print(highest_count)

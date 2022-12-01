# print '#' when there is one (or multiple) point(s)
def print_paper(paper):
    width = max([p[0] for p in paper])+1
    height = max([p[1] for p in paper])+1
    arr = [[" " for _ in range(width)] for _ in range(height)]

    for point in paper:
        arr[point[1]][point[0]] = "#"

    for y in range(height):
        for x in range(width):
            print(arr[y][x], end="")

        print()


coords_string, fold_instructions_string = open('input.txt', 'r').read().split("\n\n")
coords = [(int(p.split(",")[0].strip()), int(p.split(",")[1].strip())) for p in coords_string.split("\n")]
fold_instructions = [(p.replace("fold along ", "").split("=")[0], int(p.replace("fold along ", "").split("=")[1])) for p in fold_instructions_string.split("\n") ]

# use set to represent paper, as every coordinate can only be contained once
paper = set(coords)

for num, (axis, pos) in enumerate(fold_instructions):
    for coord in paper.copy():
        if axis == 'y':
            if coord[1] > pos:
                paper.remove(coord)
                # mirror at y-axis=pos
                newCoord = (coord[0], 2*pos - coord[1])
                paper.add(newCoord)

        if axis == 'x':
            if coord[0] > pos:
                paper.remove(coord)
                # mirror at x-axis=pos
                newCoord = (2*pos - coord[0], coord[1])
                paper.add(newCoord)

    if num == 0:
        print("Part 1:", len(paper))

print("Part 2:")
print_paper(paper)

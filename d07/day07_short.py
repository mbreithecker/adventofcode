positions = [int(p) for p in open('input.txt', 'r').read().split(",")]
print("Part 1:", min([sum([abs(p-height) for p in positions]) for height in range(max(positions))]))
print("Part 2:", min([sum([int(abs(p-height)*(abs(p-height)+1)/2) for p in positions]) for height in range(max(positions))]))

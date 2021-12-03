arr = [int(line) for line in open('input.txt', 'r').readlines()]
print("Part 1:", len([i for i in range(0, len(arr) - 1) if arr[i+1] > arr[i]]))
print("Part 2:", len([i for i in range(0, len(arr) - 3) if arr[i+3] + arr[i+2] + arr[i+1] > arr[i] + arr[i+1] + arr[i+2]]))

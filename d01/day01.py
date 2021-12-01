arr = [int (line) for line in open('input.txt', 'r').readlines()]

#part one
inc = 0
deepest = 0
for i in arr:
    if i > deepest:
        inc += 1

    deepest = i

print(inc - 1)

#part two
inc = 0
deepest = 0
for i in range(0, len(arr)-2):
    if arr[i]+arr[i+1]+arr[i+2] > deepest:
        inc += 1

    deepest = arr[i]+arr[i+1]+arr[i+2]

print(inc - 1)


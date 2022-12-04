a = open("input.txt").read().splitlines()
ds = [set(r[0: len(r) // 2]).intersection(set(r[len(r) // 2:])).pop() for r in a]
print("p1: ", sum([ord(c) - (96 if c > 'Z' else 38) for c in ds]))

g = [a[i:i + 3] for i in range(0, len(a), 3)]
ds = [set(x[0]).intersection(set(x[1])).intersection(set(x[2])).pop() for x in g]
print("p2: ", sum([ord(c) - (96 if c > 'Z' else 38) for c in ds]))

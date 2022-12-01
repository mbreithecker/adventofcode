lines = open('input.txt', 'r').readlines()

# part one
conjugate = {")": "(", "}": "{", ">": "<", "]": "["}
score_map_part1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_map_part2 = {"(": 1, "[": 2, "{": 3, "<": 4}
score_part1 = 0
scores_part2 = list()

for line in lines:
    stack = list()
    for c in line.strip():
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        else:
            if stack.pop() != conjugate[c]:
                score_part1 += score_map_part1[c]
                break
    else:
        # part two
        if len(stack) != 0:
            # closing characters are missing
            score = 0
            for element in stack[::-1]:
                score *= 5
                score += score_map_part2[element]

            scores_part2.append(score)

print("Part 1: ", score_part1)
print("Part 2: ", sorted(scores_part2)[len(scores_part2) // 2])

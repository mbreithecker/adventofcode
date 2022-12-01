def string_explode(number):
    bracket_counter = 0
    for i in range(len(number)):
        c = number[i]
        if c == "[": bracket_counter += 1
        if c == "]": bracket_counter -= 1

        # find nested number to explode
        if bracket_counter == 5:
            if c.isdigit():
                # extract numbers from string
                commaPos = number.find(",", i)
                closingBracketPos = number.find("]", commaPos)
                x = number[i: commaPos]
                y = number[commaPos + 1: closingBracketPos]
                leftNumber = number[:i-1]
                rightNumber = number[closingBracketPos+1:]

                # add x to next left number
                for k in range(len(leftNumber)-1, 0, -1):
                    if leftNumber[k].isdigit():
                        numberStart = k
                        while numberStart >= 0 and leftNumber[numberStart].isdigit(): numberStart -= 1
                        if numberStart > 0:
                            leftNumber = leftNumber[:numberStart+1] + str(int(x) + int(leftNumber[numberStart+1:k+1])) + leftNumber[k+1:]
                        break

                # add y to next right number
                for k in range(len(rightNumber)):
                    if rightNumber[k].isdigit():
                        numberEnd = k
                        while numberEnd < len(rightNumber) and rightNumber[numberEnd].isdigit(): numberEnd += 1
                        if numberEnd < len(rightNumber):
                            rightNumber = rightNumber[:k] + str(int(y) + int(rightNumber[k:numberEnd])) + rightNumber[numberEnd:]
                        break

                new_number = leftNumber + "0" + rightNumber
                return True, new_number

    return False, number


def string_split(number):
    for i in range(len(number)):
        c = number[i]
        if c.isdigit():
            # find digit
            digit_end = i
            while digit_end < len(number) and number[digit_end].isdigit(): digit_end += 1
            value = int(number[i:digit_end])

            if value >= 10:
                # split number
                new_number = number[:i] + "[" + str(value//2) + "," + str(value//2 + value%2) + "]" + number[digit_end:]
                return True, new_number

    return False, number


def string_reduce(number):
    number = number.strip()
    flag_changed = True
    # apply rules as long as they simplify the term
    while flag_changed:
        flag_changed, new_number = string_explode(number)
        if flag_changed:
            number = new_number
            continue

        flag_changed, new_number = string_split(number)
        if flag_changed:
            number = new_number
            continue

    return number


# pares number into tree for easier calculation of the magnitude
def parse_number(line, depth=0):
    line = line.strip()
    # find comma separating the outer most pair
    bracket_counter = -1
    for i in range(len(line)):
        c = line[i]
        if c == "[":
            bracket_counter += 1
        elif c == "]":
            bracket_counter -= 1

        # comma found
        elif c == "," and bracket_counter == 0:
            x = line[1:i]
            if not x.isdigit():
                x = parse_number(x, depth + 1)
            else:
                x = int(x)

            y = line[i+1:-1]
            if not y.isdigit():
                y = parse_number(y, depth + 1)
            else:
                y = int(y)

            pre_number = {"depth": depth, "x": x, "y": y}
            if type(x) is dict:
                x["parent"] = pre_number

            if type(y) is dict:
                y["parent"] = pre_number

            return pre_number


def calculate_magnitude(number):
    if type(number) is int:
        return number

    return 3 * calculate_magnitude(number["x"]) + 2 * calculate_magnitude(number["y"])


# part 1
lines = open("input.txt", "r").readlines()
sum_string = string_reduce(lines[0])
for line in lines[1:]:
    sum_string = "[" + sum_string + "," + string_reduce(line) + "]"
    sum_string = string_reduce(sum_string)

print("Part 1:", calculate_magnitude(parse_number(sum_string)))

# part 2
highest_value = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i==j: continue
        sum_string = "[" + lines[i] + "," + lines[j] + "]"
        sum_string = string_reduce(sum_string)
        mag = calculate_magnitude(parse_number(sum_string))
        if mag > highest_value:
            highest_value = mag

print("Part 2:", highest_value)

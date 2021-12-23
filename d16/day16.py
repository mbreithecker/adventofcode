# Needed for part 1 and 2
def parse_package(binary_string):
    version = int(binary_string[0:3], 2)
    binary_string = binary_string[3:]

    type_id = int(binary_string[0: 3], 2)
    binary_string = binary_string[3:]

    if type_id == 4:
        # literal package
        number_string = ""
        while binary_string[0] == "1":
            number_string += binary_string[1:5]
            binary_string = binary_string[5:]

        # add last group which started with a "0"
        number_string += binary_string[1:5]
        binary_string = binary_string[5:]

        value = int(number_string, 2)
        return {"version": version, "type_id": type_id, "value": value}, binary_string

    else:
        # operator package
        mode = binary_string[0: 1]
        binary_string = binary_string[1:]

        if mode == "0":
            # total-length mode
            total_length = int(binary_string[0: 15], 2)
            binary_string = binary_string[15:]
            sub_list = list()
            bit_read_count = 0
            while bit_read_count < total_length:
                sub, remaining_string = parse_package(binary_string)
                sub_list.append(sub)
                bit_read_count += len(binary_string)-len(remaining_string)
                binary_string = remaining_string

            return {"version": version, "type_id": type_id, "sub_packets": sub_list}, binary_string

        elif mode == "1":
            number_of_packets = int(binary_string[0: 11], 2)
            binary_string = binary_string[11:]
            sub_list = list()
            for i in range(number_of_packets):
                sub, remaining_string = parse_package(binary_string)
                sub_list.append(sub)
                binary_string = remaining_string

            return {"version": version, "type_id": type_id, "sub_packets": sub_list}, binary_string


# Needed for part 2
def calculate_expression(package):
    if package["type_id"] == 4:
        return package["value"]

    if package["type_id"] == 0:
        return sum([calculate_expression(s) for s in package["sub_packets"]])

    if package["type_id"] == 1:
        package_product = 1
        for sub in package["sub_packets"]:
            package_product *= calculate_expression(sub)

        return package_product

    if package["type_id"] == 2:
        return min([calculate_expression(s) for s in package["sub_packets"]])

    if package["type_id"] == 3:
        return max([calculate_expression(s) for s in package["sub_packets"]])

    if package["type_id"] == 5:
        return 1 if calculate_expression(package["sub_packets"][0]) > calculate_expression(package["sub_packets"][1]) else 0

    if package["type_id"] == 6:
        return 1 if calculate_expression(package["sub_packets"][0]) < calculate_expression(package["sub_packets"][1]) else 0

    if package["type_id"] == 7:
        return 1 if calculate_expression(package["sub_packets"][0]) == calculate_expression(package["sub_packets"][1]) else 0


# create binary string from hex input
binary = ""
for hex_char in open("input.txt", "r").read():
    for bit in bin(int(hex_char, 16) + 16)[3:]:
        binary += bit

package = parse_package(binary)[0]

# traverse package for part 1
package_queue = [package]
version_sum = 0
while len(package_queue) != 0:
    p = package_queue[0]
    version_sum += p["version"]
    if "sub_packets" in p:
        for sub in p["sub_packets"]:
            package_queue.append(sub)

    package_queue.remove(p)

print("Part 1: ", version_sum)
print("Part 2: ", calculate_expression(package))

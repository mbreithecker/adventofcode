lines = open('input.txt', 'r').readlines()

# create graph
node_hash_list = dict()
node_hash_list["start"] = set()

for line in lines:
    p1, p2 = line.strip().split("-")
    if p2 not in node_hash_list:
        node_hash_list[p2] = set()

    if p1 not in node_hash_list:
        node_hash_list[p1] = set()

    if not p1 == "end" and not p2 == "start":
        node_hash_list[p1].add(p2)

    if not p2 == "end" and not p1 == "start":
        node_hash_list[p2].add(p1)

# traverse graph PART ONE
possible_paths = list()
path1 = ["start"]
possible_paths.append(path1)

flag_paths_updated = True
while flag_paths_updated:
    flag_paths_updated = False
    for path in possible_paths.copy():
        if path[-1] == "end":
            continue  # ignore

        # try to find next move
        for nextStep in node_hash_list[path[-1]]:
            copyPath = [p for p in path]
            if nextStep not in path or nextStep.isupper():
                # append path
                copyPath.append(nextStep)
                flag_paths_updated = True

                possible_paths.append(copyPath)

        possible_paths.remove(path)

print("Part 1: ", len(possible_paths))


# PART TWO
def small_cave_one_more_visit_allowed(path, nextStep):
    if nextStep == "end":
        return True

    small_caves = set()
    for name in path:
        if name.isupper():
            continue

        if name in small_caves:
            return nextStep not in path

        small_caves.add(name)

    return True


# traverse graph PART Two
possible_paths = list()
possible_paths.append(["start"])
possible_path_counter = 0

flag_paths_updated = True
while flag_paths_updated:
    flag_paths_updated = False
    for path in possible_paths.copy():
        if path[-1] == "end":
            possible_path_counter += 1
            possible_paths.remove(path)
            continue  # ignore

        # try to find next move
        for nextStep in node_hash_list[path[-1]]:
            copyPath = [p for p in path]
            if nextStep.isupper() or small_cave_one_more_visit_allowed(copyPath, nextStep):
                # append path
                copyPath.append(nextStep)
                flag_paths_updated = True

                possible_paths.append(copyPath)

        possible_paths.remove(path)

print("Paths: ", possible_path_counter)

def shoot_probe(velocity, target_area):
    r = [0, 0]
    max_height = 0
    while r[1] >= target_area[0][1] and r[0] <= target_area[1][0]:
        r[0] += velocity[0]
        r[1] += velocity[1]

        if velocity[0] < 0:
            velocity[0] += 1
        elif velocity[0] > 0:
            velocity[0] -= 1

        velocity[1] -= 1

        if r[1] > max_height:
            max_height = r[1]

        # is target in area?
        if target_area[0][0] <= r[0] <= target_area[1][0] and target_area[0][1] <= r[1] <= target_area[1][1]:
            return True, max_height

    return False, 0


# find best velocity
highest_y = 0
best_velocity = 0
counter = 0
target_area = ((179, -109), (201, -63))

# not the best approach, does not work for general input
for vy in range(-1000, 1000):
    for vx in range(2000):
        success, height = shoot_probe([vx, vy], target_area)
        if success:
            counter += 1
            if height > highest_y:
                highest_y = height

print("Part 1:", highest_y)
print("Part 2:", counter)

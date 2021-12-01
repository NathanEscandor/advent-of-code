def get_depth_measurements():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [int(s.strip()) for s in lines]
        return stripped


def part_1(measurements):
    prev = None
    count = 0
    for depth_measurement in measurements:
        if prev != None:
            if depth_measurement > prev:
                count += 1

        prev = depth_measurement

    return count


measurements = get_depth_measurements()
increases = part_1(measurements)

print()
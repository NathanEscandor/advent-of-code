def get_depth_measurements():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return stripped


#Note: this produces off by 1 for some reason. (gives 1580, ans is 1581)
#      not completely sure why that is. need to write tests.
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
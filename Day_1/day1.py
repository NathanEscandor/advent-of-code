def get_depth_measurements():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [int(s.strip()) for s in lines]
        return stripped

def get_window_sums(window_size, measurements):
    windows = []
    for index in range(len(measurements)+1):
        if index+window_size <= len(measurements):
            window_sum = sum(measurements[index:index+window_size])
            windows.append(window_sum)
    return windows



def part_1(measurements):
    prev = None
    count = 0
    for depth_measurement in measurements:
        if prev != None:
            if depth_measurement > prev:
                count += 1

        prev = depth_measurement

    return count

def part_2():
    pass

measurements = get_depth_measurements()
increases = part_1(measurements)
windows = get_window_sums(3, measurements)
window_increases = part_1(windows)

breakpoint()
# print()
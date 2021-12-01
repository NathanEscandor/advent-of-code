def get_depth_measurements():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [int(s.strip()) for s in lines]
        return stripped

def get_window_sums(measurements, window_size):
    windows = []
    for index in range(len(measurements)+1):
        if index+window_size <= len(measurements):
            window_sum = sum(measurements[index:index+window_size])
            windows.append(window_sum)
    return windows

def get_increases(measurements):
    prev = None
    count = 0
    for depth_measurement in measurements:
        if prev != None:
            if depth_measurement > prev:
                count += 1

        prev = depth_measurement

    return count    


def part_1():
    measurements = get_depth_measurements()
    increases = get_increases(measurements)
    return increases

def part_2(window_size):
    measurements = get_depth_measurements()
    window_sums = get_window_sums(measurements, window_size)
    window_increases = get_increases(window_sums)
    return window_increases


increases = part_1()
window_increases = part_2(3)


breakpoint()

def get_commands():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return lines

# def get_window_sums(measurements, window_size):
#     windows = []
#     for index in range(len(measurements)+1):
#         if index+window_size <= len(measurements):
#             window_sum = sum(measurements[index:index+window_size])
#             windows.append(window_sum)
#     return windows

# def get_increases(measurements):
#     prev = None
#     count = 0
#     for depth_measurement in measurements:
#         if prev != None:
#             if depth_measurement > prev:
#                 count += 1

#         prev = depth_measurement

#     return count    


# def part_1():
#     measurements = get_depth_measurements()
#     increases = get_increases(measurements)
#     return increases

# def part_2(window_size):
#     measurements = get_depth_measurements()
#     window_sums = get_window_sums(measurements, window_size)
#     window_increases = get_increases(window_sums)
#     return window_increases

list_of_commands = get_commands()


position = 0
depth = 0

for command in list_of_commands:
    clean_command = command.strip()
    command_split = clean_command.split(" ")
    print(command_split)

    if command_split[0] == 'forward':
        position = position + int(command_split[1])
    elif command_split[0] == 'down':
        depth = depth + int(command_split[1])
    elif command_split[0] == 'up':
        depth = depth - int(command_split[1])

print(position)
print(depth)
breakpoint()
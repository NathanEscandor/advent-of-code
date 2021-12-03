def get_commands():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return lines

list_of_commands = get_commands()

aim = 0
position = 0
depth = 0

for command in list_of_commands:
    clean_command = command.strip()
    command_split = clean_command.split(" ")
    print(command_split)

    if command_split[0] == 'forward':
        position = position + int(command_split[1])
        depth = depth + (aim * int(command_split[1]))
    elif command_split[0] == 'down':
        aim = aim + int(command_split[1])
    elif command_split[0] == 'up':
        aim = aim - int(command_split[1])

print(position * depth)
breakpoint()
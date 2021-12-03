def get_diagnostic():
    with open('puzzle_input.txt', 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return stripped



def get_gamma(lines):
    gamma = []
    for position in range(len(lines[0])):
        zero = 0
        one = 0
        count = 0
        for line in lines:
            if int(line[position]) == 1:
                one += 1
            elif int(line[position]) == 0:
                zero += 1
            count += 1
        if zero > one:
            gamma.append(0)
        else:
            gamma.append(1)
    return gamma
        
report_lines = get_diagnostic()
gamma = get_gamma(report_lines)
gamma_str = ''.join(map(str, gamma))

epsilon = ''.join(['1' if i == '0' else '0' for i in gamma_str])
breakpoint()
power_consumption = int(gamma_str, 2) * int(epsilon, 2)

breakpoint()



# for command in list_of_commands:
#     clean_command = command.strip()
#     command_split = clean_command.split(" ")
#     print(command_split)

#     if command_split[0] == 'forward':
#         position = position + int(command_split[1])
#         depth = depth + (aim * int(command_split[1]))
#     elif command_split[0] == 'down':
#         aim = aim + int(command_split[1])
#     elif command_split[0] == 'up':
#         aim = aim - int(command_split[1])

print(position * depth)
breakpoint()
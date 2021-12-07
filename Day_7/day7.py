def get_cleaned_lines(filename):
    file_lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return stripped

filename = 'puzzle_input.txt'
str_positions = get_cleaned_lines(filename)[0].split(',')
positions = [int(position) for position in str_positions]

greatest = 0
for position in positions:
    if position > greatest:
        greatest = position

possibilities = []
for i in range(greatest):
    total_fuel = 0
    for position in positions:
        total_fuel += abs(position-i)
    possibilities.append(total_fuel)
    
part1 = min(possibilities)

breakpoint()
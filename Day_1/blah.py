def get_input():
    with open("puzzle_input.txt", "r") as f:
        return [int(line.strip()) for line in f]

def part_1(depth):
    return sum([1 for i in range(len(depth)) if depth[i] > depth[i-1]])

input = get_input()
part_1(input)
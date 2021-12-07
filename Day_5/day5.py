def get_cleaned_lines(filename):
    file_lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return stripped

def get_highest_index(lines):
    highest_index = 0
    for line in lines:
        indexes = line.split(' -> ')
        for index in indexes:
            xy = index.split(',')
            if int(xy[0]) > highest_index:
                highest_index = int(xy[0])
            if int(xy[1]) > highest_index:
                highest_index = int(xy[1])

    return highest_index+1

def generate_empty_diagram(indexes: int):
    diagram = []
    for i in range(indexes):
        this_row = ['.' for points in range(indexes)]
        diagram.append(this_row)
    
    return diagram

def get_draws(draw_line):
    draws = [int(value) for value in draw_line.split(',')]
    return draws

def print_diagram(diagram):
    for line in diagram:
        for value in line:
            print(str(value) + ' ', end='')
        print()

def get_update_range(point1, point2):
    difference = point2 - point1
    update_range = []
    if difference > 0:
        update_range = list(range(point1, point2)).append(point2+1)
    else:
        update_range = list(range(point2, point1)).append(point1+1)

    # print(str(point1) + ' -> ' + str(point2))
    # for i in update_range:
    #     print(i)
    return update_range

def calculate_vents_diagram(lines, highest_index):
    diagram = generate_empty_diagram(highest_index)

    for line in lines:
        points = line.split(' -> ')
        x1 = int(points[0].split(',')[0])
        y1 = int(points[0].split(',')[1])
        x2 = int(points[1].split(',')[0])
        y2 = int(points[1].split(',')[1])

        # only considering horiz/vert lines. x1=x2 xor y1=y2
        # if bool(xd) != bool(yd):
        if x1 == x2:
            update_range = get_update_range(y1, y2)
            for position in update_range:
                value = diagram[x1][position]
                # if position not in range(highest_index):
                #     breakpoint()
                if value == '.':
                    diagram[x1][position] = 1
                else:
                    diagram[x1][position] = value+1
        elif y1 == y2:
            # breakpoint()
            update_range = get_update_range(x1, x2)
            print(update_range)
            for position in update_range:
                # breakpoint()
                value = diagram[position][y1]
                # if position not in range(highest_index):
                #     breakpoint()
                if value == '.':
                    diagram[position][y1] = 1
                else:
                    diagram[position][y1] = value+1
        print(points)
        print_diagram(diagram)
        breakpoint()

    return diagram


filename = 'test_input.txt'
lines = get_cleaned_lines(filename)
highest_index = get_highest_index(lines)
# empty_diagram = generate_empty_diagram(highest_index)
diagram = calculate_vents_diagram(lines, highest_index)


breakpoint()
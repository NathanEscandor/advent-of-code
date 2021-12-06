filename = 'test_input.txt'

def get_cleaned_lines():
    file_lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        stripped = [s.strip() for s in lines]
        return stripped

def get_draws(draw_line):
    draws = [int(value) for value in draw_line.split(',')]
    return draws

def get_boards(cleaned_lines):
    boards = []
    this_board = []
    for line in cleaned_lines:
        if ',' in line:
            continue
        elif line == '':
            boards.append(this_board)
            this_board = []
        else:
            board_row = [int(value) for value in line.split()]
            this_board.append(board_row)
    boards.append(this_board)
    boards.remove([])
    return boards

def empty_board():
    board = []
    for i in range(5):
        board.append([0, 0, 0, 0, 0])
    return board

def is_row_win(dummy_board):
    for i in range(5):
        if sum(dummy_board[i]) == 5:
            return i
    return False


def is_column_win(dummy_board):
    # [0][0], [1][0], [2][0]
    for j in range(5):
        count = 0
        for i in range(5):
            count += dummy_board[i][j]
        if count == 5:
            return j
    return False

def col_win_data():
    db = empty_board()
    db[0][0] = 1
    db[1][0] = 1
    db[2][0] = 1
    db[3][0] = 1
    db[4][0] = 1
    return db

def row_win_data():
    db = empty_board()
    db[0] = [1, 1, 1, 1, 1]
    return db

cleaned_lines = get_cleaned_lines()
draws = get_draws(cleaned_lines[0])
boards = get_boards(cleaned_lines)
dummy_boards = [empty_board() for board in boards]

for draw in draws:
    if draw == 24:
        breakpoint()
        a = 1
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for column in range(len(boards[board][row])):
                if boards[board][row][column] == draw:
                    dummy_boards[board][row][column] = 1
    for board in range(len(boards)):
        if is_row_win(dummy_boards[board]) != False:
            breakpoint()
            break
        if is_column_win(dummy_boards[board]) != False:
            breakpoint()
            break



db = col_win_data()
result = is_column_win(db)


breakpoint()
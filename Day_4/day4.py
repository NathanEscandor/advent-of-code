filename = 'puzzle_input.txt'

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

def flatten_board(board):
    flat_board = []
    for i in range(len(board)):
        for j in range(len(board)):
            flat_board.append(board[i][j])
    return flat_board

def empty_board():
    board = []
    for i in range(5):
        board.append([0, 0, 0, 0, 0])
    return board

def is_row_win(flat_board):
    for i in range(5):
        count = 0
        for j in range(5):
            if flat_board[i+j] == 'x':
                count += 1
        if count == 5:
            return True
    return False

def is_column_win(flat_board):
    for i in range(5):
        count = 0
        for j in range(5):
            if flat_board[i+(5*j)] == 'x':
                count += 1
        if count == 5:
            return True
    return False

def calculate_score(flat_board, draw):
    total = 0
    for item in flat_board:
        if item != 'x':
            total += item
    return total * draw



# def is_column_win(dummy_board):
#     # [0][0], [1][0], [2][0]
#     for j in range(5):
#         count = 0
#         for i in range(5):
#             count += dummy_board[i][j]
#         if count == 5:
#             return j
#     return False

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
flat_boards = [flatten_board(board) for board in boards]

count = 0
final_score = 0
for draw in draws:
    for board in flat_boards:
        if draw in board:
            board[board.index(draw)] = 'x'
            count += 1
            if is_row_win(board):
                final_score = calculate_score(board, draw)
                breakpoint()
            elif is_column_win(board):
                final_score = calculate_score(board, draw)
                breakpoint()

breakpoint()


breakpoint()
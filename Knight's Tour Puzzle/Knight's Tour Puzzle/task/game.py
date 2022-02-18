from operator import itemgetter

BOARD = 1
POSITION = 0


def id_possible_moves(knight_x, knight_y):

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    mover_x = [-1, 1, -2, 2, -2, 2, -1, 1]
    mover_y = [2, 2, 1, 1, -1, -1, -2, -2]
    move_x = [x + knight_x for x in mover_x]
    move_y = [x + knight_y for x in mover_y]

    return move_x, move_y


def count_possible_moves(brd_x, brd_y, knight_x, knight_y, p_spots):
    move_count = 0

    if knight_x - 1 > 0 and knight_y + 2 <= brd_y and not p_spots.count([knight_x - 1, knight_y + 2]):  # 2
        move_count += 1

    if knight_x + 1 <= brd_x and knight_y + 2 <= brd_y and not p_spots.count([knight_x + 1, knight_y + 2]):  # 1
        move_count += 1

    if knight_x - 2 > 0 and knight_y + 1 <= brd_y and not p_spots.count([knight_x - 2, knight_y + 1]):  # 3
        move_count += 1

    if knight_x + 2 <= brd_x and knight_y + 1 <= brd_y and not p_spots.count([knight_x + 2, knight_y + 1]):  # 8
        move_count += 1

    if knight_x - 2 > 0 and knight_y - 1 > 0 and not p_spots.count([knight_x - 2, knight_y - 1]):  # 4
        move_count += 1

    if knight_x + 2 <= brd_x and knight_y - 1 > 0 and not p_spots.count([knight_x + 2, knight_y - 1]):  # 7
        move_count += 1

    if knight_x - 1 > 0 and knight_y - 2 > 0 and not p_spots.count([knight_x - 1, knight_y - 2]):  # 5
        move_count += 1

    if knight_x + 1 <= brd_x and knight_y - 2 > 0 and not p_spots.count([knight_x + 1, knight_y - 2]):  # 6
        move_count += 1

    return move_count - 1


def check_input_dimension(dimension, dimension_type):
    if len(dimension) != 2 or not dimension[0].isdecimal() or not dimension[1].isdecimal() or int(dimension[0]) <= 0 \
            or int(dimension[1]) <= 0:
        if dimension_type == BOARD:
            print("Invalid dimensions!")
        else:
            print("Invalid position!")
        return 0
    else:
        return 1


def is_safe(x, y, n, m, board):
    """
        A utility function to check if n,m are valid indexes
        for N*M chessboard
    """
    if n > x >= 0 and m > y >= 0 and board[y][x] == -1:
        return True
    return False


def print_solution(n, m, board):
    """
        A utility function to print Chessboard matrix
    """
    print("\nHere's the solution!")
    if m > 9:
        add_pad = 1
        pad = ' '
        cell_size = 3
    else:
        add_pad = 0
        pad = ''
        cell_size = 2

    print(pad, " ", end='', sep='')
    for i in range((n + 1) * (cell_size+1), 0, -1):
        if i == 1:
            print("-")
        else:
            print("-", end='')

    for j in range(m - 1, -1, -1):
        if j < 10 and add_pad:
            pad = ' '
        else:
            pad = ''
        print(pad, j + 1, '| ', end='', sep='')
        for i in range(n):
            for k in range(cell_size-1):
                print('', end='')
            if board[j][i] < 10:
                print(' ', board[j][i], end=' ', sep='')
            else:
                print(board[j][i], end=' ')
        print('|')

    print(pad, " ", end='', sep='')

    for i in range((n + 1) * (cell_size+1), 0, -1):
        if i == 1:
            print("-")
        else:
            print("-", end='')

    print(pad, '   ', end='', sep='')

    for i in range(n):
        print('', i+1, '', end='')


def manual_solve(brd_x, brd_y, x_strt, y_strt):
    """
        This function lets the user try to solve the Knight
        Tour problem.

    """

    # Initialization of Board matrix
    board = [[-1 for i in range(brd_x)] for i in range(brd_y)]

    move_x, move_y = id_possible_moves(x_strt, y_strt)

    # Since the Knight is initially at the first block
    board[y_strt-1][x_strt-1] = 1

    # Step counter for knight's position

    more_moves = 0
    all_squares_filled = 0
    next_move = []
    prev_spots = []

    while True:
        if x_strt <= brd_x and y_strt <= brd_y:
            more_moves = create_chessboard(brd_x, brd_y, x_strt, y_strt, move_x, move_y, prev_spots)
            prev_spots.insert(0, [x_strt, y_strt])
            print('\n')
            while True:
                if len(prev_spots) == brd_x * brd_y:  # All squares filled
                    all_squares_filled = 1
                    print('What a great tour! Congratulations!')
                    break

                if not more_moves:
                    print('No more possible moves!')
                    print('Your knight visited', len(prev_spots), 'squares!')
                    break

                next_move = list(map(int, input("Enter your next move: ").split()))
                # convert string input to int list
                next_move_x = next_move[0]
                next_move_y = next_move[1]

                prev = []
                prev_x, prev_y = id_possible_moves(x_strt, y_strt)
                for i in range(len(prev_x)):
                    prev.insert(i, [prev_x[i], prev_y[i]])

                move_x, move_y = id_possible_moves(next_move_x, next_move_y)
                if prev.count([next_move_x, next_move_y]):
                    break
                else:
                    print("Invalid move! ", end='')
            if more_moves and not all_squares_filled:
                x_strt = next_move[0]
                y_strt = next_move[1]
            else:
                break


def create_chessboard(brd_x, brd_y, knight_x, knight_y, m_x, m_y, p_spots):
    more_moves = 0

    if len(p_spots):
        p_spots = sorted(p_spots, key=itemgetter(0))
        p_spots = sorted(p_spots, key=itemgetter(1), reverse=True)
        num_prev_spots = len(p_spots)
    else:
        num_prev_spots = 0
    prev_spot_count = 0

    if brd_y > 9:
        add_pad = 1
        pad = ' '
        cell_size = 3
    else:
        add_pad = 0
        pad = ''
        cell_size = 2

    print(pad, " ", end='', sep='')
    for i in range(brd_x * (cell_size+1) + 3, 0, -1):
        if i == 1:
            print("-")
        else:
            print("-", end='')

    o_x_point, o_y_point = get_next_coord(m_x, m_y, brd_x, brd_y, p_spots)

    if o_y_point:
        more_moves = 1

    for i in range(brd_y, 0, -1):
        if i < 10 and add_pad:
            pad = ' '
        else:
            pad = ''
        print(pad, i, '| ', end='', sep='')
        for j in range(brd_x):
            if knight_x == j+1 and knight_y == i:      # Print X
                for k in range(cell_size-1):
                    print(' ', end='')
                print('X ', end='')
            elif len(p_spots) and prev_spot_count < num_prev_spots and p_spots[prev_spot_count][0] == j+1 \
                    and p_spots[prev_spot_count][1] == i:      # Print *
                for k in range(cell_size-1):
                    print(' ', end='')
                print('* ', end='')
                if p_spots[prev_spot_count][0] == o_x_point and p_spots[prev_spot_count][1] == o_y_point:
                    if len(m_x):
                        o_x_point, o_y_point = get_next_coord(m_x, m_y, brd_x, brd_y, p_spots)
                prev_spot_count += 1
            elif o_x_point == j+1 and o_y_point == i:  # Print number of moves
                for k in range(cell_size-1):
                    print(' ', end='')
                move_count = count_possible_moves(brd_x, brd_y, o_x_point, o_y_point, p_spots)
                print(move_count, ' ', end='', sep='')
                if len(m_x):
                    o_x_point, o_y_point = get_next_coord(m_x, m_y, brd_x, brd_y, p_spots)
            else:
                for k in range(cell_size):
                    print('_', end='')
                print(' ', end='')
        print('|')

    print(pad, " ", end='', sep='')
    for i in range(brd_x * (cell_size+1) + 3, 0, -1):
        if i == 1:
            print("-")
        else:
            print("-", end='')

    print(pad, '   ', end='', sep='')
    for i in range(brd_x):
        print('', i+1, '', end='')

    return more_moves


def get_next_coord(x_list, y_list, max_x, max_y, prev_spots):
    coord_x = 0
    coord_y = 0

    while True:
        if len(x_list):
            coord_x = x_list.pop(0)
            coord_y = y_list.pop(0)
        else:
            break

        if 0 < coord_x <= max_x and 0 < coord_y <= max_y:
            if not len(prev_spots):
                break
            elif not prev_spots.count([coord_x, coord_y]):
                break

    return coord_x, coord_y


def solve_kt(n, m, n_start, m_start, manual):
    """
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than 1 solutions,
        this function prints one of the feasible solutions.
    """

    # Initialization of Board matrix
    board = [[-1 for i in range(n)] for i in range(m)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[m_start-1][n_start-1] = 1

    # Step counter for knight's position
    pos = 2

    # Checking if solution exists or not
    solution = 1
    if not solve_ktutil(n, m, board, n_start-1, m_start-1, move_x, move_y, pos):
        print("No solution exists!")
        if manual == 'y':
            solution = 0
    elif manual == 'n':
        print_solution(n, m, board)

    if manual == 'y':
        return solution


def solve_ktutil(n, m, board, curr_x, curr_y, move_x, move_y, pos):
    """
        A recursive utility function to solve Knight Tour
        problem
    """

    if pos == n * m + 1:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, n, m, board):
            board[new_y][new_x] = pos
            if solve_ktutil(n, m, board, new_x, new_y, move_x, move_y, pos + 1):
                return True

            # Backtracking
            board[new_y][new_x] = -1
    return False


# Driver Code
if __name__ == "__main__":
    # Function Call

    try_puzzle = 0
    board_dimension = []
    good_board = 0

    while not good_board:
        board_dimension = input("Enter your board dimensions: ").split()
        good_board = check_input_dimension(board_dimension, BOARD)

    good_position = 0
    while not good_position:
        starting_position = input("Enter in the Knight's starting position: ").split()
        good_position = check_input_dimension(starting_position, POSITION)

        bad_answer = 1
        if good_position:
            while bad_answer:
                try_puzzle = input("Do you want to try the puzzle? (y/n): ")
                if try_puzzle != 'y' and try_puzzle != 'n':
                    print("Invalid Input!")
                else:
                    bad_answer = 0

            x_board = int(board_dimension[0])
            y_board = int(board_dimension[1])
            x_start = int(starting_position.pop(0))
            y_start = int(starting_position.pop(0))

            if x_start <= x_board and y_start <= y_board:
                solution_exits = solve_kt(x_board, y_board, x_start, y_start, try_puzzle)
                if try_puzzle == 'y' and solution_exits:
                    manual_solve(x_board, y_board, x_start, y_start)

                break
            else:
                print("Invalid position!")
                good_position = 0

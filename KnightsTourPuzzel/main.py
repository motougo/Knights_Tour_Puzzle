def create_chessboard (knight_x, knight_y):
    print("  -------------------")
    for i in range(8, 0, -1):
        print(i, '| ', end='')
        for j in range(8):
            if knight_x == j+1 and knight_y == i:
                print('X ', end='')
            else:
                print('_ ', end='')
        print('|')
    print("  -------------------")
    print('    1 2 3 4 5 6 7 8')

starting_position = input("Enter in the Knight's starting position: ").split()

x = starting_position.pop(0)
y = starting_position.pop(0)

if not x.isdecimal() or not y.isdecimal() or len(starting_position) > 0:
    print("Invalid dimensions!")
else:
    x_start = int(x)
    y_start = int(y)
    if 0 < x_start > 8 or 0 < y_start > 8:
        print("Invalid dimensions!")
    else:
        create_chessboard(x_start, y_start)





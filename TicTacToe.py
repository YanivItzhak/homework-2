
def print_board():
    print('0 1 2')

    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

board =[
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
]


def x_player(conter=0):
    while True:
        row_x=int(input('Player X please enter col [0-2]:'))
        if row_x < 0 or row_x > 2:
            print('must be between 0-2')

        else:
            break

    while True :
        col_x = int(input('Player X please enter col [0-2]:'))
        if col_x < 0 or col_x > 2:
            print('must be between 0-2')
        else:
            break
    board[row_x] [col_x] ='X'

    print_board()

def O_player():
    while True:
        row_O=int(input('Player O please enter col [0-2]:'))
        if row_O < 0 or row_O > 2:
            print('must be between 0-2')
        else:
            break

    while True :
        col_O = int(input('Player O please enter col [0-2]:'))
        if col_O < 0 or col_O > 2:
            print('must be between 0-2')
        else:
            break
    board[row_O] [col_O] ='O'

    print_board()


def row_ABC():

    row_A = board[0][0], board[0][1], board[0][2]
    if row_A == ('X', 'X', 'X'):
        print('player X win!')
        win_x+=1

    elif row_A == ('O', 'O', 'O'):
        print('player O win! ')
        win_O+=1


    row_B = board[1][0], board[1][1], board[1][2]

    if row_B == ('X', 'X', 'X'):
        print('player X win!')
    elif row_B == ('O', 'O', 'O'):
        print('player O win! ')


    row_C = board[2][0], board[2][1], board[2][2]

    if row_C == ('X', 'X', 'X'):
        print('player X win!')
    elif row_C == ('O', 'O', 'O'):
        print('player O win! ')


def col_ABC():
    col_A = board[0][0], board[1][0], board[2][0]

    if col_A == ('X', 'X', 'X'):
        print('player X win!')
    elif col_A == ('O', 'O', 'O'):
        print('player O win! ')


    col_B = board[0][1], board[1][1], board[2][1]

    if col_B == ('X', 'X', 'X'):
        print('player X win!')
    elif col_B == ('O', 'O', 'O'):
        print('player O win! ')


    col_C = board[0][2], board[1][2], board[2][2]

    if col_C == ('X', 'X', 'X'):
        print('player X win!')
    elif col_C == ('O', 'O', 'O'):
        print('player O win! ')


def slant():

    slant_A = board[0][0], board[1][1], board[2][2]

    if slant_A == ('X', 'X', 'X'):
        print('player X win!')
    elif slant_A == ('O', 'O', 'O'):
        print('player O win! ')


    slant_B = board[0][2], board[1][1], board[2][0]

    if slant_B == ('X', 'X', 'X'):
        print('player X win!')
    elif slant_B == ('O', 'O', 'O'):
        print('player O win! ')






print_board()
x_player()
#O_player()
x_player()
#O_player()
x_player()
#O_player()
row_ABC()
col_ABC()
slant()
print('game over')

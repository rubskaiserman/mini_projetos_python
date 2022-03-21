board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_board(board):
    for line in board:
        for position in line:
            print(position, end=' ')
        print()
    print()


def tie_test(board):
    test = False
    for line in board:
        for position in line:
            if position == '_':
                test = True
                break
    return test


def play_game(board):
    while True:
        print_board(board)
        line = int(input('Selecione uma linha: ')) - 1
        column = int(input('Selecione uma coluna: ')) - 1
        board[line][column] = 'X'
        if board[line] == ['X', 'X', 'X'] or (board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X') or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
            print_board(board)
            print('X venceu')
            break
        else:
            if tie_test:
                print_board(board)
                line = int(input('Selecione uma linha: ')) - 1
                column = int(input('Selecione uma coluna: ')) - 1
                board[line][column] = 'O'
                if board[line] == ['O', 'O', 'O'] or (board[0][column] == 'O' and board[1][column] == 'O' and board[2][column] == 'O') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
                    print_board(board)
                    print('O venceu')
                    break
            else:
                print_board(board)
                print('Velha')
                break


play_game(board)

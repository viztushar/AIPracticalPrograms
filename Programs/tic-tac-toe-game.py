import numpy as np

def create_board():
    return (np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]))

def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return (l)


def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


def diag_win(board, player):
    win = True

    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    return (win)


def is_game_over(board):
    winner = 0

    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player
            print("Winner is:" + str(winner))

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner



def input_board(loc, board, player):
    if (loc == 1):
        board[0, 0] = player
    elif (loc == 2):
        board[0, 1] = player
    elif (loc == 3):
        board[0, 2] = player
    elif (loc == 4):
        board[1, 0] = player
    elif (loc == 5):
        board[1, 1] = player
    elif (loc == 6):
        board[1, 2] = player
    elif (loc == 7):
        board[2, 0] = player
    elif (loc == 8):
        board[2, 1] = player
    elif (loc == 9):
        board[2, 2] = player
    return (board)


def play_game():
    c,winner = 0,0
    board = create_board()
    while winner == 0:
        print(board)
        print("Player 1 choose where to place")
        n = int(input(">> "))
        board = input_board(n, board, 1)
        print(board)
        if (is_game_over(board)):
            break
        print("Player 2 choose where to place")
        n = int(input(">> "))
        board = input_board(n, board, 2)
        print(board)
        winner = is_game_over(board)
        if(winner !=0):
            break

play_game()
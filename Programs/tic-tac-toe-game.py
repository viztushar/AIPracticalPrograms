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
            print("Player " + (str(winner)) + " is winner")

    if np.all(board != 0) and winner == 0:
        winner = -1

    if winner == -1:
        print("draw")
    return winner


def input_board(loc, board, player):
    if (loc == 1) and not ((board[0, 0] == 1) or (board[0, 0] == 2)):
        board[0, 0] = player
    elif (loc == 2) and not ((board[0, 1] == 1) or (board[0, 1] == 2)):
        board[0, 1] = player
    elif (loc == 3) and not ((board[0, 2] == 1) or (board[0, 2] == 2)):
        board[0, 2] = player
    elif (loc == 4) and not ((board[1, 0] == 1) or (board[1, 0] == 2)):
        board[1, 0] = player
    elif (loc == 5) and not ((board[1, 1] == 1) or (board[1, 1] == 2)):
        board[1, 1] = player
    elif (loc == 6) and not ((board[1, 2] == 1) or (board[1, 2] == 2)):
        board[1, 2] = player
    elif (loc == 7) and not ((board[2, 0] == 1) or (board[2, 0] == 2)):
        board[2, 0] = player
    elif (loc == 8) and not ((board[2, 1] == 1) or (board[2, 1] == 2)):
        board[2, 1] = player
    elif (loc == 9) and not ((board[2, 2] == 1) or (board[2, 2] == 2)):
        board[2, 2] = player

    else:
        print("you cant choose this place")
        print("Player " + ((str)(player)) + " choose where to place")
        n = int(input(">> "))
        board = input_board(n, board, player)
    return board


def play_game():
    c, winner = 0, 0
    board = create_board()
    print(board)
    while winner == 0:
        print("Player 1 choose where to place")
        n = int(input(">> "))
        board = input_board(n, board, 1)
        print(board)
        if is_game_over(board):
            break
        print("Player 2 choose where to place")
        n = int(input(">> "))
        board = input_board(n, board, 2)
        print(board)
        winner = is_game_over(board)
        if winner != 0:
            break


play_game()

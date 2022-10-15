import random


def coinflip(p1choice, p2choice):
    coin = random.randrange(1, 2, 1)
    if coin == 1:
        winner = p1choice
        print("{name} gets to go first".format(name=p1choice))
    else:
        winner = p2choice
        print("{name} gets to go first".format(name=p2choice))


def checkWin(board, player):
    if board[0][0] + board[0][1] + board[0][2] == player * 3:
        if board[0][0] == 0 or board[0][1] == 0 or board[0][2] == 0:
            return False
        else:
            return True

    elif board[1][0] + board[1][1] + board[1][2] == player * 3:
        if board[1][0] == 0 or board[1][1] == 0 or board[1][2] == 0:
            return False
        else:
            return True

    elif board[2][0] + board[2][1] + board[2][2] == player * 3:
        if board[2][0] == 0 or board[2][1] == 0 or board[2][2] == 0:
            return False
        else:
            return True

    elif board[0][0] + board[1][0] + board[2][0] == player * 3:
        if board[0][0] == 0 or board[1][0] == 0 or board[2][0] == 0:
            return False
        else:
            return True

    elif board[0][1] + board[1][1] + board[2][1] == player * 3:
        if board[0][1] == 0 or board[1][1] == 0 or board[2][1] == 0:
            return False
        else:
            return True

    elif board[0][2] + board[1][2] + board[2][2] == player * 3:
        if board[0][2] == 0 or board[1][2] == 0 or board[2][2] == 0:
            return False
        else:
            return True

    elif board[0][0] + board[1][1] + board[2][2] == player * 3:
        if board[0][0] == 0 or board[1][1] == 0 or board[2][2] == 0:
            return False
        else:
            return True

    elif board[2][0] + board[0][1] + board[0][2] == player * 3:
        if board[2][0] == 0 or board[0][1] == 0 or board[0][2] == 0:
            return False
        else:
            return True


def validateMove(move, board):
    if board[move[0]][move[0]] == 0:
        return True
    else:
        return False

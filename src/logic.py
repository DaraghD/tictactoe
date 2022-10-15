def checkWin(board,player):
    if board[0][0] + board[0][1] + board[0][2] == player*3:
        if board[0][0] == 0 or board[0][1] == 0 or board[0][2] == 0:
            return False
        else:
            return True
    elif board[1][0] + board[1][1] + board[1][2] == player*3:
        return True

    elif board[2][0] + board[2][1] + board[2][2] == player*3:
        return True

    elif board[0][0] + board[1][0] + board[2][0] == player*3:
        return True

    elif board[0][1] + board[1][1] + board[2][1] == player*3:
        return True

    elif board[0][2] + board[1][2] + board[2][2] == player*3:
        return True

    elif board[0][0] + board[1][1] + board[2][2] == player*3:

        return True

    elif board[2][0] + board[1][1] + board[0][2] == player*3:
        return True


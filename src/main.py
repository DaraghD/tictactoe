board = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],

]


def printBoard():
    print(board[0])
    print(board[1])
    print(board[2])


# [] = row , [] = column
row = int(input("enter input: row"))
row = row - 1

column = int(input("enter input: column"))
column = column - 1
printBoard()
print("{r} = row , {c} = column".format(r=row, c=column))

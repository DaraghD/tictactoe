import move
import board
import logic

def main():
    p1moved = 0
    while p1moved == 0:
        p1 = move.get_move()
        if logic.validateMove(p1, board.board):
            board.board[p1[0]][p1[1]] = 1
            board.printBoard()
        else:
            print("Sqaure taken!\nTry Again")
            continue

        if logic.checkWin(board.board,1):
            print("player one won")
            exit(1)

    p2moved = 0
    while p2moved == 0:
        p2 = move.get_move()
        if logic.validateMove(p2, board.board):
            board.board[p2[0]][p2[1]] = 2
            board.printBoard()
            p2moved = 1
        else:
            print("Sqaure taken!\nTry Again")
            continue
            
    if logic.checkWin(board.board,2) :
        print("player one lost")
        exit(1)

while True:
    main()

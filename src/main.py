import move
import board
import logic

def main():
    while True:


        p1 = move.get_move()
        board.board[p1[0]][p1[1]] = 1
        board.printBoard()

        if logic.checkWin(board.board,1):
            print("player one won")
            exit(1)

        p2 = move.get_move()
        board.board[p2[0]][p2[1]] = 2
        board.printBoard()
        if logic.checkWin(board.board,2) :
            print("player one lost")
            exit(1)

main()

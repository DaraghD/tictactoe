import move
import board

def main():
    while True:
        p1 = move.get_move()
        board.board[p1[0]][p1[1]] = 1
        board.printBoard()

        p2 = move.get_move()
        board.board[p2[0]][p2[1]] = 2
        board.printBoard()

main()

import logic
import move
import display


def main():
    table = display.init()
    p1moved = 0
    while p1moved == 0:
        p1 = move.get_move()
        if logic.validateMove(p1, table):
            table[p1[0]][p1[1]] = 1
            display.show(table)
        else:
            print("Square taken!\nTry Again")
            continue

        if logic.checkWin(table, 1):
            print("player one won\n")
            choice = int(input("Play again:1 \n Exit: 2 "))
            if choice == 1:
                main()
            else:
                exit(0)


    p2moved = 0
    while p2moved == 0:
        p2 = move.get_move()
        if logic.validateMove(p2, table):
            table[p2[0]][p2[1]] = 2
            display.show(table)
            p2moved = 1
        else:
            print("Sqaure taken!\nTry Again")
            continue

    if logic.checkWin(table, 2):
        print("player one lost")
        choice = int(input("Play again:1 \n Exit: 2 "))
        if choice == 1:
            main()
        else:
            exit(0)

main()
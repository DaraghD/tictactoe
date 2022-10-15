import logic
import move
import display
import connect
import pickle

def main():
    table = display.init()
    p1moved = 0

    ip = "127.0.0.1"
    s = connect.join_server(ip)

    client = s[0]
    if s[1] == 1:
        table = client.recv(1024)
        table = pickle.loads(table)
        display.show(table)

    while p1moved == 0:
        p1 = move.get_move()
        if logic.validateMove(p1, table):
            table[p1[0]][p1[1]] = 1
            display.show(table)

            ptab = pickle.dumps(table)
            client.send(ptab)

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



main()

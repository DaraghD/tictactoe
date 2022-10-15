import socket
import pickle


def gen_sock():
    port = 5222

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen()
    return s

    
def handle_clients(s):
    first = 1
    users = 0
    while True:
        conn, addr = s.accept()
        users = users + 1

        if first == 1:
           conn.send("first".encode())
           table = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]
           table = conn.send(pickle.dumps(table))
           first = 0
        else:
            conn.send("second".encode())

        if users == 2:
            break
        else:
            continue


def main():
    s = gen_sock()
    handle_clients(s)

    table = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    table = conn.send(pickle.dumps(table))

main()



import socket

def join_server(ip):
    go = 0
    port = 5222

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    message = client.recv(1024).decode()

    if message == "first":
        go = 1

    print("connected\n")

    return (client, go)



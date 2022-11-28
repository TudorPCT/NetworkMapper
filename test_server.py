import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", int(sys.argv[1])))
s.listen(1)
while True:
    connection, address = s.accept()
    print("Connected address:", address)
    while True:
        data = connection.recv(100).decode("UTF-8")
        if not data:
            break
        print("Received: ", data)
        if "exit" in data:
            break
    connection.close()

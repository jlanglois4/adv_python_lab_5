import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65442

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    statement = ""
    print("t3_hevil\nSay Something (bye to Quit)")
    s.sendall("Hello".encode())
    while "bye" not in statement.lower():
        statement = input("You: ")
        s.sendall(statement.encode())
        data = s.recv(1024)
        print('Adversaries: ', repr(data)[2:-1])

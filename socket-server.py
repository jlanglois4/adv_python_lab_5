import socket
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65442

thoughts = ["Let's see some ID.", "Halt.", "You could not have seen me coming.", "You have no chance.", "Leave this place."]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    message = ""
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                continue
            message = repr(data)[2:-1]
            print('Received by server: ', message)
            if "bye" in message.lower():
                back_message = "Good Bye".encode()
            else:
                rand_num = random.randint(0, 4)
                back_message = thoughts[rand_num].encode()
            conn.sendall(back_message)



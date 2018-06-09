import socket

# server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 10002))
    sock.listen(socket.SOMAXCONN)

    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))

conn.close()
sock.close()

# client


with socket.create_connection(("127.0.0.1", 10002)) as sock:
    sock.sendall(b"hello!")

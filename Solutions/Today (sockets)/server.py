import socket
from math import sin, cos
from multiprocessing import Process

# https://realpython.com/python-sockets/

function = lambda x: sin(x) + cos(x)
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)


def connection_handler(conn):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            try:
                data = float(data)
                data = function(data)
                data = str(data).encode()
                conn.send(data)
            except Exception as e:
                print(f"error occurd at connecetion {conn}", e)
                data = b"Invalid input"
                conn.send(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            client_process = Process(target=connection_handler, args=(conn,))
            client_process.start()

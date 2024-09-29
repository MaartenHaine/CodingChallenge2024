"""
Connect via tcp to a server and get a the message
the server is has the ip address ? and the port number is ?
"""
import socket

IP = "192.168.1.1"
PORT = 1234

def get_message()->str:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    # Receive data from the server
    message = s.recv(1024)

    # Close the connection
    s.close()

    return message.decode('utf-8')
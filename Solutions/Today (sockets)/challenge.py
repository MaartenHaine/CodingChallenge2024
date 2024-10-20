"""
Connect via tcp to a server and get a the message
the server is has the ip address ? and the port number is ?
"""
import socket
import matplotlib.pyplot as plt

IP = "127.0.0.1"
PORT = 12345

def get_message()->str:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    # Receive data from the server
    responses = []
    for i in range(-400, 400, 1):
        response = s.send(f"{i/100}".encode())
        responses.append(float(s.recv(1024)))
    plt.plot([x/100 for x in range(-400, 400, 1)], responses)
    plt.show()

    # Close the connection
    s.close()

    return "sin(x)"

get_message()
"""
You are analyzing a foreign network, and you come across a computer on the domain bcc.local
with an open socket on port 12345. After successfully establishing a tcp connection,
you send a number to the socket, and the system responds with a seemingly random number.

Your task is to figure out the mathematical function that is running on the server's
side based on the inputs and outputs you observe.
example:
    function = \sum_{n=0}^{inf}0.1^n*cos(3^n*pi*x)
"""
import socket
#import matplotlib.pyplot as plt

IP = "bcc.local"
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

#get_message()
print("sin(x)")

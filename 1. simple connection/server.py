import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# For IP sockets, the address that we bind to is a 
# tuple of the hostname and the port number.
port = 1234
server = socket.gethostname()

print("\nBinding to port ", port, ", please wait ... ")
s.bind((server, port))
print("Server started: " + server)
print("Waiting for a client ...")

# queue of 5
s.listen(5)

# And now, we just listen!
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

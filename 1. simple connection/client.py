import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now, since this is the client, rather than binding, we are going to connect.
port = 1234
server = socket.gethostname()

s.connect((server, 1234))
print("Connected to server!")

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now, since this is the client, rather than binding, we are going to connect.
port = 1234
# server = '192.168.1.241'
server = socket.gethostname()

s.connect((server, 1234))
print("Connected to server!")

# Looping through entire message until it ends!
while True: 
    full_msg = ''
    while True:
        msg = s.recv(8)
        if len(msg) <=0:
            break
        full_msg += msg.decode("utf-8")

    if len(full_msg) > 0:
        print(full_msg)
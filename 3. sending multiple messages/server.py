import socket
import time

HEADERSIZE = 10

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234
server = socket.gethostname()

print("\nBinding to port ", port, ", please wait ... ")
s.bind((server, port)) # What is bind doing
print("Server started: " + server)
print("Waiting for a client ...")

s.listen(5)

# And now, we just listen!
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    
    # # # New # # # 
    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+ msg

    clientsocket.send(bytes(msg, "utf-8"))
    
    while True:
        time.sleep(7)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+ msg

        print(msg)
        clientsocket.send(bytes(msg,"utf-8"))

    
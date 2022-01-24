import socket
import time
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000 
# connect to the server on local computer
s.connect(('10.0.0.2', port))
# receive data from the server and decoding to get the string.
#print (s.recv(1024).decode())
# close the connection
while True:
    time.sleep(1)
    print(s.recv(1024)) 





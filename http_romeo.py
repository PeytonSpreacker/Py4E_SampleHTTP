# imports the socket library
import socket

# creates a internet-ready stream socket for the program, essentially a file handle with no connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connects the made socket to a port using a tuple parameter
mysock.connect(('data.pr4e.org', 80))

# code the command to send to the port - makes this instantaneous so the port does not prematurely close the connection.
# encode converts python to UFT8 for sending the data
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode()

# sends the command to the port
mysock.send(cmd)

# prints the data found on the exact page until it reaches a blank, or the end of the data
# decode is the opposite of encode - converts to UNICODE
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
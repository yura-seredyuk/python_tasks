# import socket

# if __name__ == "__main__":
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(("localhost", 5000))
#     data = "Message from client"
#     sock.sendall(data)
#     result = sock.recv(4096)
#     print(result)
#     sock.close()
import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 5000))
request = None

# try:
    # while request != 'quit':
for i in range(1,11):
    request = f"Message {i}"
    time.sleep(1)
    if request:
        server.send(request.encode())
        response = server.recv(4096).decode()
        print(response)
# except KeyboardInterrupt:
#     server.close()
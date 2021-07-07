# import asyncio, socket

# async def handle_client(reader, writer):
#     request = None
#     while request != 'quit':
#         request = (await reader.read(4096)).decode()
#         response = request + '\n'
#         writer.write(response.encode())
#         await writer.drain()
#     writer.close()

# async def run_server():
#     server = await asyncio.start_server(handle_client, 'localhost', 5000)
#     async with server:
#         await server.serve_forever()

# asyncio.run(run_server())

# import socket
# from select import select

# tasks = []
# to_read = {}
# to_write = {}


# def server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind(('localhost', 5000))
#     server_socket.listen()

#     while True:
#         yield('read', server_socket)
#         client_socket, addr = server_socket.accept()
#         print('Conection from', addr)
#         tasks.append(client(client_socket))

# def client(client_socket):
#     while True:
#         yield('read', client_socket)
#         request = client_socket.recv(4096)

#         if not request:
#             break
#         else:
#             print(request.decode())
#             response = 'Server message'.encode()

#             yield('write', client_socket)
#             client_socket.send(response)
    
#     print('Outside inner while loop!')
#     client_socket.close()

# def event_loop():
#     while any([tasks, to_read, to_write]):
#         while not tasks:
#             ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

#             for sock in ready_to_read:
#                 tasks.append(to_read.pop(sock))

#             for sock in ready_to_write:
#                 tasks.append(to_write.pop(sock))
#         try:
#             task = tasks.pop(0)
#             reason, sock = next(task)
#             if reason == 'read':
#                 to_read[sock] = task
#             if reason == 'write':
#                 to_write[sock] = task

#         except StopIteration:
#             print('Done')

# tasks.append(server())
# event_loop()

import socket
import asyncio

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


async def server():
    print('Ready for accept:')
    client_socket, addr = server_socket.accept()
    print('Conection from', addr)
    await client(client_socket)

async def client(client_socket):
    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            print(request.decode())
            response = 'Server message'.encode()
            client_socket.send(response)
    
    print('Outside inner while loop!')
    client_socket.close()

def event_loop():
    loop = asyncio.get_event_loop()
    while True:
        asyncio.run(server())
    loop.close()

event_loop()
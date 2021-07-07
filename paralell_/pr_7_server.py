from multiprocessing import Process, Queue
from multiprocessing.reduction import reduce_handle, rebuild_handle
from contextlib import closing
import socket


def process_sockets(queue):
    while True:
        fd = rebuild_handle(queue.get())
        with closing(socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)) as connection:
            print(connection)
            connection.sendall('hello!\n')
            connection.shutdown(socket.SHUT_WR)


def main():
    queue = Queue()
    process = Process(target=process_sockets, args=(queue,))
    process.daemon = True
    process.start()

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5000))

    with closing(server):
        server.listen(1)

        while True:
            connection, _ = server.accept()

            queue.put(
                reduce_handle(connection.fileno())
            )


if __name__ == '__main__':
    main()

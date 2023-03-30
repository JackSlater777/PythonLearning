import multiprocessing
import socket


def run(conn, addr):
    print('Connection from address {}'.format(addr))
    data = conn.recv(1024)
    print('Received {}'.format(data.decode()))
    conn.send(data)
    conn.close()
    print('Closed connection from {}'.format(addr))


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False
        self._pool = multiprocessing.Pool(5)

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print('Server is up')
        while self._running:
            conn, addr = self._socket.accept()
            self._pool.apply_async(run, (conn, addr))

        self._socket.close()

    def stop(self):
        self._running = False
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()


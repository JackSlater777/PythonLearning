# * Написать юнит тесты для TCP-сервера (код см. далее), использовать mock чтобы эмулировать действия клиента и
# создание потоков, получить code coverage репорт в html формате.

# Класс потока под клиента
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):  # Метод для работы с наследниками класса threading.Thread
        print('Connection from address {}'.format(self._address))
        data = self._connection.recv(1024)
        print('Received {}'.format(data.decode()))
        self._connection.send(data)
        self._connection.close()
        print(f'Closed connection from {self._address}')

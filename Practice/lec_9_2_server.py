# * Написать клиентское и серверное приложения. Клиент при установке соединения отправляет на сервер
# информацию о пользователе (имя, возраст), хранимую в атрибутах объекта класса User. Сервер должен выводить информацию
# о подключенных пользователях. Клиентское приложение должно быть запущено несколько раз с различными пользователями.

# для сервера
import socket
import pickle
from lec_9_2_user import User  # импорт класса


# Добавляем людей в список
def add_user(lst, u):
    lst.append(u)
    return lst


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # '127.0.0.1' соответствует хосту, на котором запускается скрипт
port = 12345
s.bind((host, port))
s.listen(5)  # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()
    users = []  # Список под пользователей
    new_user = pickle.loads(conn.recv(1024))
    conn.send(pickle.dumps(add_user(users, new_user)))
    # conn.send(pickle.dumps(user.users))
    conn.close()
s.close()

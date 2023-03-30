# Для клиента
import socket
import pickle
from lec_9_2_user import User  # импорт класса


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))  # подключаемся к серверу
# Вводим данные экземпляра
name = input('Введите имя: ')
age = int(input('Введите возраст: '))
a = User(name, age)
s.send(pickle.dumps(a))
print(pickle.loads(s.recv(1024)))  # получаем и выводим данные, полученные от сервера
s.close()

# Возможно, надо делать вот так:
# Сериализуем и десериализуем список
# lst = ['Ivan', 'Vasya']
# with open("dumpfile", "wb") as f:
#     pickle.dump(len(lst), f)
#     for hum in lst:
#         pickle.dump(hum, f)

# with open("dumpfile", "rb") as f:
#     humans = []
#     num = pickle.load(f)
#     i = 0
#     while i < num:
#         humans.append(pickle.load(f))
#         i += 1

# Написать клиентское и серверное приложения. Клиент отправляет на сервер список зашифрованных слов,
# сервер дешифрует слова по словарю и возвращает клиенту список расшифрованных слов. Клиент должен вывести полученный
# список.

import socket


# import pickle

# За декодирование принят по умолчанию следующий словарь:
# d1 = {'*': 'h', '@': 'e', '#': 'l', '?': 'o'}


# Описываем словарь и метод декодирования
def decoder(strn):
    # Вводим строку кода
    # s1 = list(input())
    # Вводим строку соответствующего декодирования посимвольно
    # s2 = list(input())
    # Формируем словарь под декодирование
    # d1 = dict(zip(s1, s2))
    # d2 = dict (zip (s2,s1))  # Обратная операция - в задаче не нужна
    d1 = {'*': 'h', '@': 'e', '#': 'l', '?': 'o'}
    # Создаем новую строку под декодирование
    s_new = ''
    # Декодируем строки в списке
    # for s in ls:
    #     i = 0
    #     s_new = ''
    #     while i < len(s):
    #         if s[i] in d1:
    #             s_new += d1[s[i]]
    #         i += 1
    #     ls_new.append(s_new)
    # return ls_new

    # Декодируем строку
    i = 0
    while i < len(strn):
        if strn[i] in d1:
            s_new += d1[strn[i]]
        i += 1
    print(s_new)
    return s_new


# для сервера
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # '127.0.0.1' соответствует хосту, на котором запускается скрипт
port = 12346
s.bind((host, port))  # привязывает адрес (имя хоста, номер порта) к сокету
s.listen(5)  # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()  # Новый сокет для взаимодействия с новым клиентом (переводим в отдельное окно)
    # lst = conn.recv(1024).decode()
    st = conn.recv(1024).decode()
    # decoder(lst)
    # conn.send(decoder(lst).encode())
    conn.send(decoder(st).encode())
    conn.close()
s.close()

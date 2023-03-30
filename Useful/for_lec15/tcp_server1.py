import socket

# 1-й параметр - семейство адресов, с которыми будет работать сокет
# AF_INET соответствует адресам IPv4
# 2-й параметр - протокол транспортного уровня
# SOCK_STREAM соотвествует протоколу TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # '127.0.0.1' соответствует хосту, на котором запускается скрипт
port = 12346
s.bind((host, port))
s.listen(5)  # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()
    name = conn.recv(1024).decode()
    print(f"Client name {name}")
    conn.send(f'Hello, {name}'.encode())
    conn.close()
s.close()

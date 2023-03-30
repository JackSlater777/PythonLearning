# * (ПРОВЕРИТЬ) Создать несколько потоков таким образом, чтоб каждый из них мог хранить приватные данные, доступные
# только ему самому. Запустить потоки с одной функцией, выводящей в каждом потоке его имя приватные данные (имя
# исполняемого потока можно узнать, используя current_thread().name из библиотеки threading).

import threading


def get_thread_name():
    print("This is", threading.current_thread().name)


threads = []  # Список под потоки

for i in range(5):
    thr = threading.Thread(target=get_thread_name)
    thr.start()
    threads.append(thr)

# Ждем завершения потоков
for thr in threads:
    thr.join()  # для каждого потока ПОДОЖДАТЬ, пока он выполнится

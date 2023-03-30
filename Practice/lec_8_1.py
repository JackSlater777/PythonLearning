# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного
# числа start (по умолчанию 3) до заданного числа end. Далее необходимо:
# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread. Что будет,
# если 'забыть' выполнить start или join для потоков?
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
# Что будет, если 'забыть' выполнить start или join для процессов?
# Замерить время исполнения каждого варианта и сравнить результаты.

import threading
import multiprocessing
from time import perf_counter


# Для каждого числа i проверять i % j !=0 для всех j от 2 до кв. корень из i.
def find_primes(end, start=3):
    lst = []  # список под простые числа
    j = 2
    prime_number = True
    while start <= end:
        # print(f'число на проверку: {start}')
        while j <= (start ** 0.5) and (prime_number is True):
            # print(f'число-делитель: {j}')
            if start % j == 0:
                # print(f'{start} не является простым числом')
                prime_number = False
            j += 1
        if prime_number is True:
            # print(f'{start} ЯВЛЯЕТСЯ простым числом')
            lst.append(start)
        start += 1
        j = 2
        prime_number = True

    return lst


# Без распараллеливания

# Запускаем счетчик времени
t1_start = perf_counter()
find_primes(10000)
find_primes(20000, 10001)
find_primes(30000, 20001)
# Останавливаем счетчик времени
t1_stop = perf_counter()
# Выводим затраченное время
print(f"Затраченное время без распараллеливания: {t1_stop - t1_start}")


# С распараллеливанием

# Запускаем счетчик времени
t2_start = perf_counter()
# Формируем потоки
t1 = threading.Thread(target=find_primes, args=(10000,))
t2 = threading.Thread(target=find_primes, args=(20000, 10001))
t3 = threading.Thread(target=find_primes, args=(30000, 20001))
# Запускаем потоки
t1.start()
t2.start()
t3.start()
# Ждем завершения потоков
t1.join()
t2.join()
t3.join()
# Останавливаем счетчик времени
t2_stop = perf_counter()
# Выводим затраченное время
print(f"Затраченное время с распараллеливанием: {t2_stop - t2_start}")


# С распараллеливанием и выключенными join

# Запускаем счетчик времени
t3_start = perf_counter()
# Формируем потоки
t1 = threading.Thread(target=find_primes, args=(10000,))
t2 = threading.Thread(target=find_primes, args=(20000, 10001))
t3 = threading.Thread(target=find_primes, args=(30000, 20001))
# Запускаем потоки
t1.start()
t2.start()
t3.start()
# Ждем завершения потоков
# t1.join()
# t2.join()
# t3.join()
# Останавливаем счетчик времени
t3_stop = perf_counter()
# Выводим затраченное время
print(f"Затраченное время с распараллеливанием и выключенными join: {t3_stop - t3_start}")


# С распараллеливанием и выключенными start

# Запускаем счетчик времени
t3_start = perf_counter()
# Формируем потоки
t1 = threading.Thread(target=find_primes, args=(10000,))
t2 = threading.Thread(target=find_primes, args=(20000, 10001))
t3 = threading.Thread(target=find_primes, args=(30000, 20001))
# Запускаем потоки
# t1.start()
# t2.start()
# t3.start()
# Ждем завершения потоков
t1.join()
t2.join()
t3.join()
# Останавливаем счетчик времени
t3_stop = perf_counter()
# Выводим затраченное время
print(f"Затраченное время с распараллеливанием и выключенными start: {t3_stop - t3_start}")


# С многопроцессностью

if __name__ == '__main__':  # обязательно для многопроцессного приложения
    # Запускаем счетчик времени
    t4_start = perf_counter()
    # Формируем процессы
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()
    # Ждем завершения процессов
    p1.join()
    p2.join()
    p3.join()
    # Останавливаем счетчик времени
    t4_stop = perf_counter()
    # Выводим затраченное время
    print(f"Затраченное время с многопроцессностью: {t4_stop - t4_start}")


# С многопроцессностью и выключенными start

if __name__ == '__main__':  # обязательно для многопроцессного приложения
    # Запускаем счетчик времени
    t5_start = perf_counter()
    # Формируем процессы
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    # Запускаем процессы
    # p1.start()
    # p2.start()
    # p3.start()
    # Ждем завершения процессов
    p1.join()
    p2.join()
    p3.join()
    # Останавливаем счетчик времени
    t5_stop = perf_counter()
    # Выводим затраченное время
    print(f"Затраченное время с многопроцессностью и выключенными start: {t5_stop - t5_start}")


# С многопроцессностью и выключенными join

if __name__ == '__main__':  # обязательно для многопроцессного приложения
    # Запускаем счетчик времени
    t5_start = perf_counter()
    # Формируем процессы
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()
    # Ждем завершения процессов
    # p1.join()
    # p2.join()
    # p3.join()
    # Останавливаем счетчик времени
    t5_stop = perf_counter()
    # Выводим затраченное время
    print(f"Затраченное время с многопроцессностью и выключенными join: {t5_stop - t5_start}")

# ________________________________________________________
# Затраченное время без распараллеливания: 0.08259939999697963
# Затраченное время с распараллеливанием: 0.12142230000245036
# Затраченное время с распараллеливанием и выключенными join: 0.02953680000064196
# Затраченное время с распараллеливанием и выключенными start: RuntimeError: cannot join thread before it is started
# Затраченное время с многопроцессностью: 0.09670679999908316
# Затраченное время с многопроцессностью и выключенными start: AssertionError: can only join a started process
# Затраченное время с многопроцессностью и выключенными join: 0.008432499998889398
# _________________________________________________________

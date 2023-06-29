# Какие встроенные типы существуют в Python?
# immutable: str, int, tuple
# mutable: list, dict, set


# ------------------------------------------
# Как работает этот код?
try:
    n = 1 + 'A'  # Пытаемся выполнить этот код
except:
    n = 1  # Попадаем сюда, если во выполнение блока try завершилось Exception'ом
finally:
    print('H, Ozon')  # Выполняем в любом случае


# ------------------------------------------
# Что такое менеджер контекста? Как его создать через класс? Что нужно написать в методе __exit__?
# Ответ: обработку исключений
with open('1.txt', 'w') as file:
    file.write("Hello, Ozon!")

class MyCtxManager:
    # Выполняется перед кодом, который обернут
    def __enter__(self):
        print("Hello")

    # Выполняется после кода, который обернут.
    # Код внутри exit выполнится всегда, даже если выбросится исключение перед ним.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye")

with MyCtxManager() as myctxmgr:
    x = 100
    y = 200
    # raise Exception
    print(f"{x + y = }")


# ------------------------------------------
# Что такое декоратор? Как написать?
# Ответ: см. замыкание
def counter(func):
    """Обертка для подсчета количества вызовов функции"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f"{func.__name__} called {wrapper.count} times")
        return res
    wrapper.count = 0
    return wrapper

@counter
def foobar():
    pass

foobar()  # foobar called 1 times


# ------------------------------------------
# Что такое генератор? Особенности?
# Ответ: это объект, который позволяет получать из итерируемого объекта порционно (ПЕРЕДЕЛАТЬ!)
def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

lst = [i for i in gen(5)]
print(lst)  # [0, 1, 2, 3, 4]


# ------------------------------------------
# Что будет после исполнения этого кода?
def func(val, *args, **kwargs):
    print(val)  # Hi
    print(args)  # ('Ozon', {'a': 1, 'b': 2})
    print(kwargs)  # {'pi': 3.14, 'e': 2.71}

func("Hi", "Ozon", {"a": 1, "b": 2}, pi=3.14, e=2.71)


# ------------------------------------------
# Что будет после исполнения этого кода?
class C:
    pass

a = C()
b = C()
print(a == b)  # False, т.к. нет критериев сравнения
print(a is b)  # False, т.к. экземпляры находятся в разных участках памяти


# ------------------------------------------
# Что нужно сделать, чтобы иметь возможность сравнивать атрибуты экземпляров?
# Ответ: перегрузка операторов

class MyComparableClass:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        if self.val == other.val:
            return True
        else:
            return False

a = MyComparableClass(1)
b = MyComparableClass(1)
print(a == b)  # True

# ------------------------------------------
# Что будет после исполнения этого кода?
# Ответ: ф-ия zip зипует в кортежи элементы итерируемых объектов, dict преобразует их в словарь, где
# ключ - элемент с 0-ым индексом, а значение - элемент с 1-ым индексом
res = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(res)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# ------------------------------------------
# Что может являться ключом словаря?
# Ответ: только неизменяемые объекты


# ------------------------------------------
# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает список с n чисел Фибоначчи.
# Последовательность Фибоначчи - это последовательность чисел, где каждое следующее число - сумма двух предыдущих.
# Часть первых чисел Фибоначчи для fib(7): [0, 1, 1, 2, 3, 5, 8]
def fib(n: int) -> list:
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    if n == 0:
        return []
    else:
        lst = []
        cnt = 0
        while cnt < n:
            if cnt == 0:
                lst.append(0)
            elif cnt == 1:
                lst.append(1)
            else:
                elem = lst[cnt-2] + lst[cnt-1]
                lst.append(elem)
            cnt += 1
        return lst

print(fib(5))  # [0, 1, 1, 2, 3]
print(fib(-1))  # ValueError
print(fib("-1"))  # TypeError


# ------------------------------------------
# *Простые числа * - это натуральные числа больше единицы, которые делятся нацело только на единицу и на
# себя.Например, число 3 простое, так как нацело делится только на 1 и 3. Число 4 сложное, так как нацело делится
# не только на 1 и 4, но также на число 2. Напишите функцию, которая проверяет является ли целое неотрицательное
# n простым. Часть первых простых чисел: [2, 3, 5, 7, 11, 13]
def is_prime(n: int) -> bool:
    tpl = tuple(i for i in range(n))
    for num in tpl:
        if num == 0 or num == 1:
            continue
        else:
            if n % num == 0:
                return False
    return True

print(is_prime(5))  # True
print(is_prime(10))  # False


# ------------------------------------------
# Есть handler для возврата информации о последнем заказе в личном кабинете клиента.
# Какие 3 бизнес сценария ты проверил бы в первую очередь?

# GET / client / last_order?client_id={client_id}

# 1. """negative tc - invalid client_id"""
# Проверить, когда client_id == 0: GET /client/last_order?client_id=0

# 2. """positive tc - get info about last order with valid client_id"""
# GET / client/last_order?client_id = {client_id}

# 3. """positive tc - get empty last order with recently signed-in client_id"""
# GET /client/last_order?client_id={client_id}

# ------------------------------------------
# Что такое pipe | в однострочнике:
# tail - f / var / log / dmesg.log | grep 'ERR'?
# Что делают команды?


# ------------------------------------------
# Как получить список запущенных контейнеров?
# Ответ: docker ps


# ------------------------------------------
# Как работает git rebase?
# Ответ: он меняет commit pointer на последний

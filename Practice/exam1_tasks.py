# 1. (РЕШЕНО) Написать реализацию встроенной функции len: функция принимает список, возвращает его длину.
# Стандартную функцию len использовать нельзя! (3 балла)
def my_len(st):
    cnt = 0
    for _ in st:
        cnt += 1
    return cnt


s = input()
print(my_len(s))


# 2. (РЕШЕНО) Написать реализацию функции reversed: функция принимает список, возвращает его же, располагая элементы
# в обратном порядке. Стандартную функцию reversed и метод reverse использовать нельзя! (3 балла)
def my_reverse(ls):
    i = 0
    j = len(ls) - 1
    while i < j:
        ls[i], ls[j] = ls[j], ls[i]
        i += 1
        j -= 1
    return ls


lst = [1, 2, 3, 4]
print(my_reverse(lst))


# 3. (РЕШЕНО) * Написать реализацию функции range: она может принимать от одного до трех аргументов, при этом аргументами
# должны быть целые числа (int). range(старт, стоп, шаг) - так выглядит стандартный вызов функции range() в Python.
# По умолчанию старт равняется нулю, шаг - единице. Возвращает список целых чисел в форме
# [старт, старт + шаг, старт + шаг * 2...]. Если шаг положительное число, последним элементом списка будет
# наибольшее (старт + i * шаг) меньшее числа стоп. Если шаг отрицательное число, то последний элемент будет
# наименьшее (старт + i * шаг) большее числа стоп. Предусмотреть случаи ошибочных аргументов (например, шаг == 0).
# Стандартный генератор range использовать нельзя! (5 баллов).
# def my_range(start=0, stop, step=1):
def my_range(*args):
    # if 3 < len(args) < 1:
    if len(args) > 3 or len(args) < 1:
        print('Incorrect arguments!')
        raise Exception
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) > 1:
        start = args[0]
        stop = args[1]
        if len(args) == 2:
            step = 1
        elif len(args) == 3:
            step = args[2]
            if args[2] == 0:
                print('Incorrect step!')
                raise Exception
    lst = []
    rn = start
    if step > 0:
        while rn < stop:
            lst.append(rn)
            rn += step
    elif step < 0:
        while rn > stop:
            lst.append(rn)
            rn += step
    return lst


print(my_range(10))  # start stop step
print(my_range(0, -10, -1))


# 4. (РЕШЕНО) Написать функцию to_title: принимает строку, ищет пробелы, первые буквы после них и после начала строки
# делает заглавными. Строковый метод title использовать нельзя! (3 балла)
#
# >>> to_title('orlov Ilya evgenyevich')
# 'Orlov Ilya Evgenyevich'
def to_title(st):
    st = list(st)
    print(st)
    i = 0
    while i < len(st):
        if st[i] == ' ':
            st[i + 1] = st[i + 1].upper()
        i += 1
    st[0] = st[0].upper()
    st = "".join(st)
    return st


print(to_title('orlov Ilya evgenyevich'))


# 5. (РЕШЕНО) Написать функцию count_symbol: считает сколько раз символ встречается в строке.
# Строковый метод count использовать нельзя! (3 балла)
def count_symbol(st):
    d = {}
    for i in st:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
    return d


s = 'Ivan Karazanov'.lower()
print(count_symbol(s))

# 6. (РЕШЕНО) * Написать реализацию функции format. Стандартную функцию format использовать нельзя!
# (5 баллов, с re – 7 баллов)
# >>> myformat('{1}, {0}, {2}', 'a', 'b', 'c')
# 'b, a, c'
# >>> myformat('coordinates: {}, {}', '37.4N', '18.3W')
# 'coordinates: 37.4N, 18.3W'
import re


def myformat(*args):
    if args[0].find('{}') == -1:
        myformat1(*args)
    else:
        myformat2(*args)


def myformat1(*args):
    # Для первого варианта
    # Превращаем кортеж в список
    args = list(args)
    # Задаем шаблон для скобок или скобок с индексом
    pattern1 = re.compile('{(|\d)}')
    # формируем список под нужные индексы
    lst = []
    # Добавляем в список найденные по шаблону индексы
    lst += re.findall(pattern1, args[0])  # ['1', '0', '2']
    # Если (индекс аргумента - 1) (т.к. аргумент[0] - строка с индексами)  равен числовому значению списка - заменяем 
    for i in range(len(lst)):
        j = 0 # индекс аргумента
        # print(f'i: {i}')
        # print(f'int(lst[i]): {int(lst[i])}')
        while j < (len(args)):
            # print(f'j: {j}')
            # print(f'args[j]: {args[j]}')
            if j - 1 == int(lst[i]):
                lst[i] = args[j]
                j = len(args)
            j += 1
    
    lst1 = ', '.join(lst)
    print(lst1)


def myformat2(*args):
    # Для второго варианта
    # Превращаем кортеж в список
    args = list(args)
    # Задаем шаблон для скобок или скобок с индексом
    pattern1 = re.compile('{(|\d)}')
    # Задаем индекс строки в списке без скобок (замены)
    i = 1
    while i < len(args):
        # Заменяем скобки на строку
        args[0] = re.sub(pattern1, args[i], args[0], count=1)
        # print(args[0])
        i += 1

    print(args[0])


myformat('{1}, {0}, {2}', 'a', 'b', 'c')
myformat('coordinates: {}, {}', '37.4N', '18.3W')


# 7. (РЕШЕНО) Написать функцию copyfile: функция принимает два аргумента – имена файлов source и destination,
# открывает source, читает его, открывает destination, пишет в него. Если source не найден или destination
# уже существует, то выбрасываются соответствующие исключения. Нужно проверить выполнение функции как для
# правильных аргументов, так и для приводящих к исключениям. Исключения перехватывать не требуется. (3 балла)

# Альтернатива: shutil.copyfile(src, dst, *, follow_symlinks=True)

def copyfile(src, dest):
    with open(src) as f:
        # Задаем индекс текста и индекс элемента, с которого "считаем" параграф
        s = f.read()  # Переносим текст файла в переменную, выбрасывает исключение, если такого файла нет
        with open(dest, 'x') as g:  # Открываем destination - если не существует, выбрасывает исключение
            g.write(s)  # Записываем текст из переменной в destination


# Указываем пути файлов
# source = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\karazanov\1.txt'
source = r'.\1.txt'  # Относительный путь
# destination = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\karazanov\2.txt'
destination = r'.\1_copy.txt'  # Относительный путь

copyfile(source, destination)


# 8. (РЕШЕНО) * Написать функцию copydir - копирование директории с использованием copyfile из задания 7,
# а также проверки на существование source и destination. (5 баллов)

# Альтернатива: shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
# ignore_dangling_symlinks=False, dirs_exist_ok=False)

import os


def copydir(s, d):
    # Если destination не существует
    if not os.path.exists(d):
        d = s + '_copy'
        os.mkdir(d)  # создаем каталог с именем d
    # Если destination существует
    if os.path.exists(d):
        # Пофайлово применяем функцию copyfile
        files = os.listdir(s)  # возвращаем список, содержащий имена файлов и директорий в каталоге, заданном путем s
        for file in files:
            fl = os.path.join(s, file)  # формируем путь файла для копирования
            fl_copy = os.path.join(d, file)  # # формируем путь файла под копирование
            # Проверяем, является ли объект файлом
            if os.path.isfile(fl):
                copyfile(fl, fl_copy)  # Выполняем функцию копирования
            # Проверяем, является ли объект подпапкой
            elif os.path.isdir(fl):
                os.mkdir(fl_copy)  # создаем подпапку под копирование
                copydir(fl, fl_copy)  # Делаем рекурсию на копирование папки


# Указываем пути директорий
# source = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\karazanov\1'
source = r'.\1'
# destination = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\karazanov\1_copy'
destination = r'.\1_copy'

copydir(source, destination)


# 9. (РЕШЕНО) Создайте класс User, в котором будут поля name (имя), age (возраст) и геттеры и сеттеры для них.
# Создайте класс Worker, который наследуется от класса User и имеет дополнительное поле salary (зарплата),
# а также геттер и сеттер для этого поля. Создайте объект этого класса name='John', age=25, salary=1000.
# Создайте второй объект этого класса 'Jack', age=26, salary=2000. Найдите сумму зарплат объектов John и Jack. (3 балла)
class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg1):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, arg2):
        pass


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, bonus):
        pass


w1 = Worker('John', 25, 1000)
w2 = Worker('Jack', 26, 2000)

# print(w1.salary)
# print(w2.salary)
sum_salary = w1.salary + w2.salary
print(sum_salary)


# 10. * (РЕШЕНО) Создайте класс Money (деньги) для работы с денежными суммами. Число должно быть представлено
# двумя полями: для рублей и для копеек. Дробная часть (копейки) при выводе на экран должна быть отделена от целой
# части запятой. Необходимо реализовать сложение, вычитание, деление сумм и операции сравнения. Также нужно добавить
# атрибут текущий курс по доллару и метод перевода по текущему курсу в доллары (для справки по перегрузке операторов -
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html). (7 баллов)
class Money:
    def __init__(self, ruble, kopeyka, exchange):
        self.ruble = ruble
        self.kopeyka = kopeyka
        self.exchange = exchange
        self.ruble_sum = (self.ruble + (self.kopeyka / 100))
        self.dollar_sum = 0

    def convert_ruble_sum_to_dollar_sum(self):
        self.dollar_sum += (self.ruble_sum / self.exchange)
        print(f'Вы обменяли {self.ruble_sum} рублей по курсу {self.exchange} рублей за доллар')
        print(f'У вас на руках {self.dollar_sum} долларов')
        self.ruble = 0
        self.kopeyka = 0
        self.ruble_sum = 0
        print(f'У вас на руках {self.ruble_sum} рублей')

    def convert_dollar_sum_to_ruble_sum(self):
        self.ruble_sum += (self.dollar_sum * self.exchange)
        print(f'Вы обменяли {self.dollar_sum} долларов по курсу {self.exchange} рублей за доллар')
        print(f'У вас на руках {self.ruble_sum} рублей')
        self.ruble = self.ruble_sum // 100
        self.kopeyka = self.ruble_sum % 100
        self.dollar_sum = 0
        print(f'У вас на руках {self.dollar_sum} долларов')

    def __add__(self, other):
        rub = self.ruble + other.ruble
        kop = self.kopeyka + other.kopeyka
        exchange = self.exchange  # тут решение неоднозначное и остается на усмотрение разработчика
        return Money(rub, kop, exchange)

    def __sub__(self, other):
        rub = self.ruble - other.ruble
        kop = self.kopeyka - other.kopeyka
        exchange = self.exchange  # тут решение неоднозначное и остается на усмотрение разработчика
        return Money(rub, kop, exchange)

    def __truediv__(self, other):
        rub = self.ruble / other.ruble
        kop = self.kopeyka / other.kopeyka
        exchange = self.exchange  # тут решение неоднозначное и остается на усмотрение разработчика
        return Money(rub, kop, exchange)

    def __le__(self, other):  # Магический метод lesser or equal
        # print(my_sum1 <= my_sum2)  # вызывается при такой функции
        if self.ruble_sum == other.ruble_sum:
            print("Суммы в рублях равны")
            return self.ruble_sum == other.ruble_sum
        elif self.ruble_sum < other.ruble_sum:
            print(f"Сумма {my_sum1} меньше суммы {my_sum2}")
            return self.ruble_sum <= other.ruble_sum

    def __ge__(self, other):  # Магический метод greater or equal
        # print(my_sum1 >= my_sum2)  # вызывается при такой функции
        if self.ruble_sum == other.ruble_sum:
            print("Суммы в рублях равны")
            return self.ruble_sum == other.ruble_sum
        elif self.ruble_sum > other.ruble_sum:
            print(f"Сумма {my_sum1} больше суммы {my_sum2}")
            return self.ruble_sum >= other.ruble_sum

    def __repr__(self):
        return str(self.ruble_sum)


# my_sum = Money(int(input("Введите кол-во рублей: ")), int(input("Введите кол-во копеек: ")), float(input("Введите обменный курс одного доллара в следующем формате 60.50: ")))
my_sum1 = Money(70, 150, 65.25)
# my_sum1.convert_ruble_sum_to_dollar_sum()
# my_sum1.convert_dollar_sum_to_ruble_sum()
my_sum2 = Money(110, 64, 69.33)
my_sum3 = Money(85, 64, 69.15)
print(f"Сумма в рублях: {my_sum1 + my_sum2}")
print(f"Сумма в рублях: {my_sum1 + my_sum2 + my_sum3}")
print(f"Разница в рублях: {my_sum1 - my_sum2}")
print(f"Разница в рублях: {my_sum1 - my_sum2 - my_sum3}")
print(f"Соотношение рублевых сумм: {my_sum1 / my_sum2}")
my_sum1 <= my_sum2
my_sum1 >= my_sum2

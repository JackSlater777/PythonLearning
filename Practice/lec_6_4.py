# Часто задача программиста заключается в том, чтоб найти в документации готовую функцию, которая
# реализует необходимое решение. Данное задании предполагает самостоятельное изучение документации
# к библиотеке itertools (это набор готовых итераторов), чтобы подобрать те функции, которые дадут
# правильные ответы на следующие вопросы (иногда надо будет добавить свои аргументы при вызове функций
# помимо тех, что указаны в задании).
# Требуется написать код, который использует указанные входные данные и выводит на экран возвращаемое значение.
# Помните, что функции могут возвращать генератор, который нужно "развернуть" для вывода на экран.

from itertools import chain
from itertools import filterfalse
from itertools import combinations


def concatenate_lists(x, y, z):
    res = list(chain(x, y, z))
    return res


def sort_strings(lst):
    res = list(filterfalse(lambda i: len(i) < 5, lst))
    return res


def combinate(s):
    res = list(combinations(s, 4))
    return res


# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7]).
ls_x = [1, 2, 3]
ls_y = [4, 5]
ls_z = [6, 7]
print(concatenate_lists(ls_x, ls_y, ls_z))

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов,
# у которых длина не меньше пяти (['hello', 'write']).
ls = ['hello', 'i', 'write', 'cool', 'code']
print(sort_strings(ls))

# Функция выдает на строку 'password' все возможные комбинации вида
# ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
st = 'password'
print(combinate(st))

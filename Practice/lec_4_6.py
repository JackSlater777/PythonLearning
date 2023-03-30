# * Есть список списков (матрица). Каждый внутренний список - это строка матрицы. Необходимо
# реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
import random


def delete_number(a, x, y, number):
    i = x - 1
    j = y - 1
    number_of_deleted_columns = 0
    while i >= 0:
        while j >= 0:
            print(f"i = {[i]}, j = {[j]}")
            if a[i][j] == number:
                print(f"Элемент {a[i][j]}")
                number_column = j
                number_row = x - 1
                while number_row >= 0:
                    print(f"Удаляю элемент {a[number_row][number_column]}")
                    a[number_row].pop(number_column)
                    number_row -= 1
                number_of_deleted_columns += 1
            j -= 1
        i -= 1
        j = y - 1 - number_of_deleted_columns
        print(f"i = {[i]}, j = {[j]}")
    for ls in a:
        print(" ".join(map(str, ls)))


# Составляем матрицу из n строк и m столбцов
n, m = (int(i) for i in input("Введите число строк и столбцов матрицы: ").split())
# Генерируем списки со случайными числами
matrix = [[random.randint(0, 9) for j in range(m)] for i in range(n)]
# Выводим на экран как матрицу
for lst in matrix:
    print(" ".join(map(str, lst)))
# Цифра-индикатор удаления столбца
s = int(input("Введите цифру, которая будет указывать на удаление столбца: "))
delete_number(matrix, n, m, s)

# Если удалять элементы по убыванию (reverse), по индексу съезда не будет. Собрать столбцы в объект (кортеж?)

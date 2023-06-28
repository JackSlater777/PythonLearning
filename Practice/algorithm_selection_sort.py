# Алгоритм сортировки выбором заключается в поиске на необработанном срезе массива
# или списка минимального значения и в дальнейшем обмене этого значения с первым элементом
# необработанного среза. На следующем шаге необработанный срез уменьшается на один элемент.

# Временная сложность - O(n^2)
# Вычислительная сложность - O(1)


def selection_sort(array):
    """Функция сортировки выбором"""
    # Сначала надо найти минимальное значение на срезе от i до конца списка.
    for i in range(len(array) - 1):
        # minimum - индекс ячейки с минимальным значением.
        minimum = i  # Сначала предполагаем, что в ячейке i содержится минимальный элемент
        j = i + 1  # Поиск начинаем с ячейки следующей за i
        while j < len(array):  # Пока не дойдем до конца списка...
            # ...будем сравнивать значение ячейки j, со значением ячейки minimum.
            if array[j] < array[minimum]:  # Если в j значение меньше, чем в m...
                minimum = j  # ...сохраним в minimum номер найденного на данный момент минимума
            j = j + 1  # Перейдем к следующей ячейке
        # В ячейку i записывается найденный минимум, а значение из ячейки i переносится на старое место минимума
        array[i], array[minimum] = array[minimum], array[i]


if __name__ == '__main__':
    lst = [5, 3, 6, 2, 10]
    selection_sort(lst)  # [2, 3, 5, 6, 10]
    print(lst)
# Алгоритм сортировки выбором заключается в поиске на необработанном срезе массива
# или списка минимального значения и в дальнейшем обмене этого значения с первым элементом
# необработанного среза. На следующем шаге необработанный срез уменьшается на один элемент.


def selection_sort(array):  # сортируется массив
    """
    Функция сортировки выбором
    """
    # Сначала надо найти минимальное значение на срезе от i до конца списка.
    for i in range(len(array) - 1):
        # m - индекс ячейки с минимальным значением.
        # Сначала предполагаем, что в ячейке i содержится минимальный элемент.
        m = i
        # Поиск начинаем с ячейки следующей за i.
        j = i + 1
        # Пока не дойдем до конца списка,
        while j < len(array):
            # будем сравнивать значение ячейки j, со значением ячейки m.
            if array[j] < array[m]:
                # Если в j значение меньше, чем в m, сохраним в m номер найденного на данный момент минимума.
                m = j
            # Перейдем к следующей ячейке.
            j = j + 1
        # ОБМЕН ЗНАЧЕНИЙ
        # В ячейку i записывается найденный минимум, а значение из ячейки i переносится на старое место минимума.
        array[i], array[m] = array[m], array[i]


if __name__ == '__main__':
    lst = [5, 3, 6, 2, 10]
    selection_sort(lst)  # [2, 3, 5, 6, 10]
    print(lst)

# В быстрой сортировке используется стратегия «разделяй и властвуй» - использование рекурсии. Следовательно,
# массив должен разделяться до тех пор, пока мы не придем к базовому случаю.

# Временная сложность (средний случай) - O(n log n)
# Временная сложность (худший случай) - O(n^2)
# Вычислительная сложность - O(n)


def quicksort(array):
    """Пустые массивы и массивы, содержащие всего один элемент,
    # станут базовым случаем. Такие массивы можно просто возвращать
    # в исходном виде - сортировать ничего не нужно."""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # В массиве выбирается элемент, который называется опорным
        less = [i for i in array[1:] if i <= pivot]  # Формируем подмассив элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Формируем подмассив элементов больше опорного
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([10, 5, 15, 2, 7, 3]))  # [2, 3, 5, 7, 10, 15]
    print(quicksort([10, 5]))  # [5, 10]
    print(quicksort([5]))  # [5]
    print(quicksort([10, 5, 17]))  # [5, 10, 17]

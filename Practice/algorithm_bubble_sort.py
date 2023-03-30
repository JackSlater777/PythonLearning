# Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного
# сравнения и обмена соседних элементов, если предшествующий оказывается больше последующего.

# В процессе выполнения данного алгоритма элементы с большими значениями оказываются в конце списка,
# а элементы с меньшими значениями постепенно перемещаются по направлению к началу списка. Образно
# говоря, тяжелые элементы падают на дно, а легкие медленно всплывают подобно пузырькам воздуха.

def bubble_sort(a):  # Общая O(N^2)
    n = len(a)
    for i in range(n):  # O(N)
        for j in range(n - 1):  # O(N)
            if a[j] > a[j + 1]:  # O(1)
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t


if __name__ == '__main__':
    lst = [9, 1, 15, 8, 161, 32, 55]
    bubble_sort(lst)
    print(lst)
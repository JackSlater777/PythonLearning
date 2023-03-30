# (ПРОВЕРИТЬ!) Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list)
# параллельно с различными наборами аргументов.

from multiprocessing import Pool


# def my_add(*args):
def my_add(ls1, ls2):
    lst = []  # список для результатов сложения
    # for i in range(len(args)):
    # for arg in args:
    for i in range(len(ls1)):
        for j in range(len(ls2)):
            if i == j:
                if type(ls1[i]) == type(ls2[j]):
                    lst.append(ls1[i] + ls2[j])

                else:
                    raise Exception
    return lst


# lst1 = [1, 'Vasya', 2, 'Ivan']  # первый список с элементами
lst1 = [1, 'Vasya', 'Ivan']  # первый список с элементами
lst2 = [5, 'Vasya', 'Ivan', 3]  # второй список с элементами

if __name__ == '__main__':
    pool = Pool(processes=4)
    # res = pool.map(my_add, lst1, lst2)
    res = pool.starmap(my_add, [(lst1, lst2)])
    # res = pool.map(sum, lst1, lst2)
    print(res)

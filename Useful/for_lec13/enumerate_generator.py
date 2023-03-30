def my_enumerate(lst):
    lst_1 = []
    for i in lst:
        lst_1.append((i, i ** 2, i ** 3))
    return lst_1


def my_enumerate_gen(lst):
    for i in lst:
        yield i, i ** 2, i ** 3


m = my_enumerate_gen([4, 5, 6])
print(next(m))
print(next(m))

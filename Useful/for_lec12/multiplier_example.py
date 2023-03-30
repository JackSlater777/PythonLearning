import functools


def multiplier(src, m):
    return [m * i for i in src]


def mul1(src):
    return multiplier(src, 10)


mul2 = lambda src: multiplier(src, 10)


mul3 = functools.partial(multiplier, m=10)

lst = [1, 2, 3]
print(mul1(lst))
print(mul2(lst))
print(mul3(lst))

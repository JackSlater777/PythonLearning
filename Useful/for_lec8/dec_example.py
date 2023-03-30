def dec(func):
    def new_fun(a, b):
        res = func(a, b)
        return res, a * b

    return new_fun


@dec
def fun(a, b):
    return a + b


#fun = dec(fun)

print(fun(10, 20))
print(fun(100, 200))


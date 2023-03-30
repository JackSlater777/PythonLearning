import time


def time_fun(pfun):
    def inner_fun(*nargs, **kwargs1):
        print(f"{nargs=}")
        print(f"{kwargs1=}")
        start = time.perf_counter_ns()
        res = pfun(*nargs, **kwargs1)
        print(f"Total time: {time.perf_counter_ns() - start}")
        return res
    return inner_fun


def fun(a, b):
    print(f"Arguments: {a}, {b}")
    return a + b


print("Nodecorator")
print(fun(10, 20))

print("Decorator")
fun = time_fun(fun)
print(fun(10, 20))
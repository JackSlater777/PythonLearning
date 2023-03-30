def fun(x, y):
    res = x + y
    print(res)


def zond(x):
    assert x == 300


class Ctx:
    def __enter__(self):
        self.bkp = print

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.bkp

# bkp = print

print = zond
fun(100, 200)

# print = bkp

print("The end")



# assert fun(100, 200) == 300
# if fun(100, 200) == 300:
#     print("OK")
# else:
#     print("Not OK")
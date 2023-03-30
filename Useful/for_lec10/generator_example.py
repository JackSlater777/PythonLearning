def fun(n):
    i = 0
    cnt = 0
    while cnt < n:
        yield i
        i += 2
        cnt += 1


for i in fun(5):
    print(i)

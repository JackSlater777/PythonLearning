def my_gen(lst, n):
    cnt = 0
    for i in lst:
        if i == n:
            yield cnt
        cnt += 1

# Вывести N четных чисел

N = int(input())
lst = []
i = 0
cnt = 0
while cnt < N:
    if i % 2 == 0:
        lst.append(i)
        cnt += 1
    i += 1
print(lst)
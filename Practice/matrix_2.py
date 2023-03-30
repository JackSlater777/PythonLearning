# Выведите таблицу размером n*n, заполненную числами от 1 до n^2 по спирали, выходящей из
# левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n = 5):

# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())

# Матрица из 1
m = [[1 for j in range(n)] for i in range(n)]

# Цикл
cycle_n = 0

###
while cycle_n < n:
    # Верхняя строка
    # Первый цикл отличается от последующих стартовой позицией j
    reverse_i = cycle_n
    k = 0
    # Для первого цикла:
    if cycle_n == 0:
        reverse_j = cycle_n
        while reverse_j <= n - 1 - cycle_n:
            m[reverse_i][reverse_j] = m[cycle_n][cycle_n] + k
            k += 1
            reverse_j += 1
    # Для всех последующих
    elif cycle_n > 0:
        reverse_j = cycle_n - 1
        while reverse_j <= n - 1 - cycle_n:
            m[reverse_i][reverse_j] = m[cycle_n][cycle_n - 1] + k
            k += 1
            reverse_j += 1

    # Правый столбец
    reverse_i = cycle_n
    reverse_j = n - 1 - cycle_n
    k = 0

    while reverse_i <= n - 1 - cycle_n:
        m[reverse_i][reverse_j] = m[cycle_n][n - 1 - cycle_n] + k
        k += 1
        reverse_i += 1

    # Нижняя строка
    reverse_i = n - 1 - cycle_n
    reverse_j = n - 1 - cycle_n
    k = 0

    while reverse_j >= cycle_n:
        m[reverse_i][reverse_j] = m[n - 1 - cycle_n][n - 1 - cycle_n] + k
        k += 1
        reverse_j -= 1

    # Левый столбец
    reverse_i = n - 1 - cycle_n
    reverse_j = cycle_n
    k = 0

    while reverse_i >= 1 + cycle_n:
        m[reverse_i][reverse_j] = m[n - 1 - cycle_n][cycle_n] + k
        k += 1
        reverse_i -= 1

    cycle_n += 1

# Выводим на экран в виде матрицы
for ls in m:
    print(" ".join(map(str, ls)))

# Другие решения
# №1
# n = int(input())
# m = [[0] * n for i in range(n)]
# i, j, di, dj = 0, 0, 0, 1

# for k in range(n * n):
#     m[i][j] = k + 1
#     if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
#         di, dj = dj, -di
#     i, j = i + di, j + dj

# [print(*i) for i in m]

# №2
# n=int(input())
# t=[[0]*n for i in range (n)]
# i,j=0,0
# for k in range(1, n*n+1):
#   t[i][j]=k
#   if k==n*n: break
#   if i<=j+1 and i+j<n-1: j+=1
#   elif i<j and i+j>=n-1: i+=1
#   elif i>=j and i+j>n-1: j-=1
#   elif i>j+1 and i+j<=n-1: i-=1
# for i in range(n):
#   print(*t[i])

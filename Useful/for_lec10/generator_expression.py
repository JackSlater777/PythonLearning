lst = [1, 2, 3, 4]

a = [x ** 2 for x in lst]  # O(N) по памяти
b = (x ** 2 for x in lst)  # O(1) по памяти
y = 100

print(dict.fromkeys(b, y ** 2))

# Составить программу, которая будет считывать введённое пятизначное число.
# После чего, каждую цифру этого числа необходимо вывести в новой строке:
# Число: 10819
# 1 цифра равна 1
# 2 цифра равна 0
# 3 цифра равна 8
# 4 цифра равна 1
# 5 цифра равна 9
# Статус - решено

a = input("Введите пятизначное число: ")
# Индекс первого символа
i = 0
# Индекс последнего символа строки
j = len(a) - 1

while i <= j:
    print(f"{i+1} цифра равна {a[i]}")
    i += 1

# Написать и вызвать функцию, принимающую два числа и выводящую
# на экран большее из двух.
# Статус - решено


def compare(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("x equals y, so no result for you!")


x = int(input("Enter x: "))
y = int(input("Enter y: "))

compare(x, y)

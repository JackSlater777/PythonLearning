# Написать и вызвать функцию, принимающую два числа и возвращающую
# большее из двух.
# Статус - решено


def compare(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(compare(x, y))

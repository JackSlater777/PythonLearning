# Введите 1-е число: 10
# Введите 2-е число: 20
# Результат: 50%
def percent(x, y):
    return int(x / y * 100)


x = float(input("Введите 1-e число: "))
y = float(input("Введите 2-e число: "))

print(f"Процент равен: {percent(x, y)}%")


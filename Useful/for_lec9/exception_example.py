n = input('Input number: ')
m = input('Input number: ')
try:
    n = int(n)
    m = int(m)
    print(n / m)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except Exception as ex:
    print(f"Got exception: {type(ex)}: {ex}")
else:
    print("Все ОК! Исключений нет!")
finally:
    print("Happy end!")
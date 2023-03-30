# Реализовать приложение, загадывающее целое число из заданного
# пользователем диапазона и предлагающее пользователю это число угадать.
# Отгадывание числа должно быть реализовано в цикле: пока пользователь
# не угадает, или не введет нечисловой символ, продолжать опрос.
# Если пользователь вводит неправильное число, вывести подсказку:
# больше оно или меньше загаданного.
import random


x = int(input("Enter the lowest interval level: "))
y = int(input("Enter the highest interval level: "))
number = random.randint(x, y)
number_is_discovered = False

while not number_is_discovered:
    a = input("What number do I have? Enter: ")
    if not a.isdecimal():
        print("This is not a number!")
        break
    else:
        a = int(a)
        if a == number:
            number_is_discovered = True
            print("Correct!")
        elif a > number:
            print("My number is smaller than you think!")
        elif a < number:
            print("My number is bigger than you think!")

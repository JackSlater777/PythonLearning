# Реализовать цикл, формирующий число из вводимых пользователем символов,
# пока не будет введено слово “stop” (или “Stop”, или “STOP”). Если
# пользователь ввел не числовой символ, вывести предупреждение и запросить
# новый символ.
# Статус - решено

b = ''

while True:
    a = input("Enter a number: ")
    if a.lower() == "stop":
        print(b)
        break
    elif not a.isdecimal():
        print("This is not a number! Try again")
    else:
        b += a

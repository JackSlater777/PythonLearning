# Приложение для игры в камень-ножницы-бумага
import random


def stone_scissors_paper(x: int, y: int, lst):
    z = x - y
    t = ("камень", "ножницы", "бумага")
    print(f"\nПервый игрок выбрал {t[x]}")
    print(f"Второй игрок выбрал {t[y]}")
    if z == 0:
        print("Ничья!\n")
    elif z == -1 or z == 2:
        print("Победил первый игрок!\n")
        lst[0] += 1
        return lst
    elif z == 1 or z == -2:
        print("Победил второй игрок!\n")
        lst[1] += 1
        return lst


if __name__ == '__main__':
    i_am_tired = False
    wins = [0, 0]

    while not i_am_tired:
        print(f"Счет {wins[0]}:{wins[1]}")
        your_choice = input("Введите 0-камень, 1-ножницы, 2-бумага, 3-хватит: ")
        if not your_choice.isdigit() or int(your_choice) < 0 or int(your_choice) > 3:
            print("Некорректные данные!")
            break
        elif int(your_choice) == 3:
            print("До новых встреч!")
            i_am_tired = True
        else:
            computer_choice = random.randint(0, 2)
            stone_scissors_paper(int(your_choice), computer_choice, wins)

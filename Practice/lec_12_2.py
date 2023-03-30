# Написать юнит тесты для класса Money из задания 10 контрольной работы (файл Tasks\py_exam_1.pptx),
# получить code coverage репорт в html формате.

class Money:
    def __init__(self, ruble, kopeyka):
        self.ruble = ruble
        self.kopeyka = kopeyka
        self.exchange = 69.15
        self.ruble_sum = (self.ruble + (self.kopeyka / 100))
        self.dollar_sum = 0

    def convert_ruble_sum_to_dollar_sum(self):
        self.dollar_sum += (self.ruble_sum / self.exchange)
        print(f'Вы обменяли {self.ruble_sum} рублей по курсу {self.exchange} рублей за доллар')
        print(f'У вас на руках {self.dollar_sum} долларов')
        self.ruble = 0
        self.kopeyka = 0
        self.ruble_sum = 0
        print(f'У вас на руках {self.ruble_sum} рублей')
        return self.dollar_sum

    def convert_dollar_sum_to_ruble_sum(self):
        self.ruble_sum += (self.dollar_sum * self.exchange)
        print(f'Вы обменяли {self.dollar_sum} долларов по курсу {self.exchange} рублей за доллар')
        print(f'У вас на руках {self.ruble_sum} рублей')
        self.ruble = self.ruble_sum // 100
        self.kopeyka = self.ruble_sum % 100
        self.dollar_sum = 0
        print(f'У вас на руках {self.dollar_sum} долларов')
        return self.ruble_sum

    def __add__(self, other):
        rub = self.ruble + other.ruble
        kop = self.kopeyka + other.kopeyka
        return Money(rub, kop)

    def __sub__(self, other):
        rub = self.ruble - other.ruble
        kop = self.kopeyka - other.kopeyka
        # my_sum1 = Money(70, 150)
        # my_sum2 = Money(110, 64)
        # -40, +86
        # Expected :-38.86
        # Actual   :-39.14
        return Money(rub, kop)

    def __truediv__(self, other):
        rub = self.ruble / other.ruble
        kop = self.kopeyka / other.kopeyka
        return Money(rub, kop)

    def __le__(self, other):  # Магический метод lesser or equal
        # print(my_sum1 <= my_sum2)  # вызывается при такой функции
        if self.ruble_sum == other.ruble_sum:
            print("Суммы в рублях равны")
            return self.ruble_sum == other.ruble_sum
        elif self.ruble_sum < other.ruble_sum:
            print(f"Сумма {my_sum1} меньше суммы {my_sum2}")
            return self.ruble_sum <= other.ruble_sum

    def __ge__(self, other):  # Магический метод greater or equal
        # print(my_sum1 >= my_sum2)  # вызывается при такой функции
        if self.ruble_sum == other.ruble_sum:
            print("Суммы в рублях равны")
            return self.ruble_sum == other.ruble_sum
        elif self.ruble_sum > other.ruble_sum:
            print(f"Сумма {my_sum1} больше суммы {my_sum2}")
            return self.ruble_sum >= other.ruble_sum

    def __repr__(self):
        return str(self.ruble_sum)


# my_sum = Money(int(input("Введите кол-во рублей: ")), int(input("Введите кол-во копеек: ")),
#                float(input("Введите обменный курс одного доллара в следующем формате 60.50: ")))

my_sum1 = Money(70, 150)
# my_sum1.convert_ruble_sum_to_dollar_sum()
# my_sum1.convert_dollar_sum_to_ruble_sum()

my_sum2 = Money(110, 64)
# my_sum2.convert_ruble_sum_to_dollar_sum()
# my_sum2.convert_dollar_sum_to_ruble_sum()

my_sum3 = Money(85, 64)
# my_sum3.convert_ruble_sum_to_dollar_sum()
# my_sum3.convert_dollar_sum_to_ruble_sum()

print(f"Сумма в рублях: {my_sum1 + my_sum2}")
print(f"Сумма в рублях: {my_sum1 + my_sum2 + my_sum3}")
print(f"Разница в рублях: {my_sum1 - my_sum2}")
print(f"Разница в рублях: {my_sum2 - my_sum1}")
# print(f"Разница в рублях: {my_sum1 - my_sum2 - my_sum3}")
print(f"Соотношение рублевых сумм: {my_sum1 / my_sum2}")
my_sum1 <= my_sum2
my_sum1 >= my_sum2

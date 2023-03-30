class MyMoney:
    def __init__(self, rub, kop):
        self._rub = rub
        self._kop = kop

    def calc_by_rate(self, rate):
        if rate is None:
            return None
        else:
            return self._rub / rate


m = MyMoney(100, 0)
r = input("Введите курс: ")
print(m.calc_by_rate(50))
print(m.calc_by_rate(100))

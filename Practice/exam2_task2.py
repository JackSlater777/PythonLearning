# 2. Напишите свой класс-итератор, который при итерации генерирует простые числа (столько, сколько задали при создании
# экземпляра класса). (5 баллов) - РЕШЕНО НЕ ДО КОНЦА ПРАВИЛЬНО!

# задаем свой класс исключений
# обязательно должен наследоваться от встроенного класса Exception
class NonValidInput(Exception):
    pass  # как правило, тело класса исключения остается пустым


# Формируем класс под итератор
class MyIter:
    def __init__(self, cnt):
        self._cnt = cnt
        self._num = 3
        self._lst = []

        # Выбрасываем исключение, если аргумент - не число или меньше единицы
        if type(self._cnt) != int or self._cnt < 1:
            raise NonValidInput

    def __iter__(self):
        return self

    def __next__(self):
        # # Выбрасываем исключение, если аргумент - не число или меньше единицы
        # if type(self._cnt) != int or self._cnt < 1:
        #     raise NonValidInput
        # Пока счетчик выводимых простых чисел не дойдет до нуля
        while self._cnt > 0:
            # Флаг простого числа
            is_simple = True
            # Задаем минимальный делитель
            i = 2
            # Задаем верхний порог i = n = квадр корень из числа
            n = self._num ** 0.5
            # Пока делитель меньше либо равен квадратному корню из тестируемого числа
            while i <= n and is_simple is True:
                # Если остаток от деления равен нулю
                if self._num % i == 0:
                    # Число не является простым
                    is_simple = False
                i += 1
            # Если в результате цикла флаг не сбился, число - простое
            if i > n and is_simple is True:
                # Добавляем простое число в список
                self._lst.append(self._num)
                # Уменьшает счетчик
                self._cnt -= 1
            # Тестируем следующее число
            self._num += 1
            return self._lst
        raise StopIteration


# Создаем экземпляр
m = MyIter(10)
# Выдаем заданное количество порций итераций
for i in m:
    print(i)

# Функции на вход подаётся последовательность чисел source и множитель m.
# На выходе функции ожидается новая последовательность на основе source,
# где каждый член был умножен на m. Если source не был указан, то берётся
# последовательность [1,2,3]. Укажите ошибки, допущенные в данной функции,
# и предложите свою реализацию.

# def multiplier(m=1, source=[1,2,3]):
#     result = source
#     for i, x in enumerate(source):
#         result[i] *= m
#     return result


# >>> multiplier(5)
# [5, 10, 15]
# >>> multiplier(12, [1,2])
# [12, 24]

# def multiplier(m=1, source=[1, 2, 3]):  # дефолт аргумент изменяемый объект
def multiplier(m=1, source=None):
    if source is None:
        source = [1, 2, 3]
    # result = source  # Зачем это?
    for i, x in enumerate(source):
        # result[i] *= m  # Тут ошибка? Должно быть source[i]
        source[i] *= m
    # print(result)  # За ненадобностью переменной result выводим source
    print(source)
    # return result  # Возвращать в случае ненадобности переменной result надо source
    return source


multiplier(5)
multiplier(12, [1, 2])

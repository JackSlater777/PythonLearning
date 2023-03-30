# (НЕРЕШЕНО!) lec_6_1
# В чем ошибка в данной программе и как ее можно исправить?
# def chargen():
#     while True:
#         for c in '0123456789':
#             yield c
# words = [c + c for c in chargen()][:10]

def chargen():
    i = 0
    st = '0123456789'  # Непонятно, нужен ли на выходе список int или str? В случае int: конвертировать объект в int
    # while True:  # нет условия для выхода из цикла
    while i < len(st):
        #  for c in '0123456789':  # объекту лучше выделить переменную, цикл for не нужен
        yield st[i]
        i += 1


words = [c + c for c in chargen()]
print(words)

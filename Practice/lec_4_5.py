# Интерполировать некие шаблоны в строке: есть строка с определенного вида форматированием, необходимо
# заменить в этой строке все вхождения шаблонов на их значение из словаря.
s = input("Введите строку: ")
d = {'!': 111, '?': 222, '#': 333}

for key, value in d.items():
    # Конвертируем ключи и значения в строку
    key1 = str(key)
    value1 = str(value)
    # Заменяем ключи на значения
    s = s.replace(key1, value1)

print(s)

# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле или строке.
# То есть, передается на вход файл или строка, необходимо заменить все символы табуляции на четыре пробела,
# либо же заменить все комбинации из четырех символов пробела на символ табуляции.

def replace_symbols(string, sc, tc):
    if sc == 0 and tc == 0:
        print(f"Строка {string} не имеет 4 пробелов или табуляций")
        return None
    elif sc > 0 and tc > 0:
        choice = int(input("Хотите заменить \n1 - пробелы \nили \n2 - табуляцию? "))
        if choice == 1:
            string = string.replace(space, tab)
        elif choice == 2:
            string = string.replace(tab, space)
    elif sc > 0 and tc == 0:
        string = string.replace(space, tab)
    elif tc > 0 and sc == 0:
        string = string.replace(tab, space)
    print(f"Строка с замененными символами: {string}")
    return string


# s = input("Введите строку с 4 пробелами и/или табуляциями: ")
# s = "abcdefgg"
s = "ab    cd    ef\tgg"
print(f"Строка: {s}")

space = "    "
space_count = s.count(space)

tab = "\t"
tab_count = s.count(tab)

replace_symbols(s, space_count, tab_count)

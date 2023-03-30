# Используя модуль re, найти все команды Git с аргументами в файле Practice/README.md
import re


lst = []  # Создаем список под все найденные команды

pattern = re.compile("git\s\w*\s")  # компилируем (подготавливаем) шаблон для ускорения поиска
# path = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\README.md'
path = r'..\README.md'  # Относительный путь

with open(path) as f:
    for line in f:
        lst += re.findall(pattern, line)  # '*' - 0 или более чисел ('+' - 1 или более чисел)

print(lst)

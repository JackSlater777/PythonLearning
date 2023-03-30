# Написать генератор для построчного чтения файла.

def my_gen(p):
    with open(p) as f:
        # for i in f.readlines():  # Создает список строк, не нужно
        for i in f:  # построчно проходим по файлу
            # print(f'{i}')
            yield i


# path = r'C:\Users\Иван\Desktop\python_work\PythonCourseATIS_0422\Practice\karazanov\text.txt'
path = r'.\text.txt'  # Относительный путь
g = my_gen(path)
for i in g:  # генераторы и итераторы сами являются итерируемыми объектами
    print(i)

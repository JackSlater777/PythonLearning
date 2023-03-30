# Написать класс WrapStrToFIle, который будет иметь одно вычисляемое свойство (property) под названием
# content. В конструкторе класс должен инициализовать атрибут filepath, путем присваивания результата
# функции mktemp библиотеки tempfile. При попытке чтения свойства content должен внутри кода свойства
# открываться файл, используя атрибут filepath (с помощью функции open, из этого файла читается все
# содержимое и возвращается из свойства. Если файл не существует, то возникает ошибка, поэтому должна
# быть обертка вокруг открытия файла на чтение (try...except), с помощью которого будет возвращаться
# 'Файл еще не существует'. При присваивании значения свойству content файл по указанному пути должен
# открываться на запись и записываться содержимое. Не забудьте закрывать файл после чтения или записи.
# При удалении атрибута content, должен удаляться и файл.

import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'
        try:
            with open(self.filepath, 'r') as f:
                s = f.read()
                return s
        except FileNotFoundError:
            print("File doesn't exist")

    @content.setter
    def content(self, value):
        # попытка записи в файл указанного содержимого
        with open(self.filepath, 'w') as f:
            f.write(value)
            # return f

    @content.deleter
    def content(self):
        # удаляем файл: os.remove(имя_файла)
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content  # после этого файла не существует

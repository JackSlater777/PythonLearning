# Написать класс-обертку над SQLite (с возможностями менеджера контекста), которая может на вход принимать строки
# SQL запросов и возвращать данные в формате json. Класс должен иметь, как минимум, методы select и execute.

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
import os


# Создаем класс контекст-менеджера
class MyCtxManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):  # Выполняется перед кодом, который обернут
        print("Hello")
        self.conn = sqlite3.connect(self.name)
        self.conn.row_factory = sqlite3.Row

    def select(self, films_id):
        # Создаем курсор - специальный объект, который делает запросы и получает их результаты
        cur = self.conn.cursor()
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        cur.execute("SELECT F.name, F.desc"
                    " FROM films AS F"
                    " AND F.id = :films_id",
                    {'films_id': films_id})
        print("Информация:")
        # Получаем результат сделанного запроса
        lst = []
        for row in cur.fetchall():
            print(dict(row))
            lst.append(dict(row))
        return lst

    # Писать метод на каждое поле - вроде как негибкое решение, потому что поля могу добавляться и придется код
    # переписывать. Если делать все внутри функции, то мы все равно сталкиваемся с необходимостью динамически
    # формировать сам текст запроса (указывать или не указывать F.name, F.desc). А это открытые ворота для SQL-инъекций.
    # Идеальным решением стало бы использованием ORM. Но в текущих условиях (DB-API) можно либо действительно
    # прописывать отдельные методы, либо вообще снять с метода select ответственность за формирование запроса, чтоб
    # она принимала его уже в готовом виде и просто формировала результат:
    # def select(self, request, values):
    #     cur = self.conn.cursor()
    #     cur.execute(request, values)
    #     # Получаем результат сделанного запроса
    #     lst = []
    #     for row in cur.fetchall():
    #         lst.append(dict(row))
    #     return lst

    def execute(self, films_id, name, desc):
        # Создаем курсор - специальный объект, который делает запросы и получает их результаты
        cur = self.conn.cursor()
        try:
            # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
            cur.execute("INSERT INTO films (id, name, desc)"
                        " AND films.id = :films_id"
                        " VALUES (:id, :name, :desc)",
                        {'films_id': films_id, 'name': name, 'desc': desc})
            # Если мы не просто читаем, но и вносим изменения в базу данных, необходимо сохранить транзакцию
            self.conn.commit()
            return True
        except:
            return False

    def __exit__(self, exc_type, exc_val, exc_tb):  # Выполняется после кода, который обернут
        # Код внутри exit выполнится всегда, даже если выбросится исключение перед ним
        # Не забываем закрыть соединение с базой данных после работы
        self.conn.close()
        print("Bye")


# Вывод информации о фильме на экран
# def show_film_info(con, films_id):
#     cur = con.cursor()
#     cur.execute("SELECT F.name, F.desc"
#                 " FROM films AS F"
#                 " AND F.id = :films_id",
#                 {'films_id': films_id})
#     print("Информация:")
#     for row in cur.fetchall():
#         print(dict(row))


# Файл базы данных
db_name = r'.\sqlite-tools\myfilms.db'
db_exists = os.path.exists(db_name)

# Создаем экземпляр менеджера контекста к нашей базе данных
with MyCtxManager(db_name) as myctx:
    # РАБОТАЕМ С БАЗОЙ
    myctx.select(1)
    myctx.execute(5, 'Tragedy', 'Very Boring')

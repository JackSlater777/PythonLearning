# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала
# их и сохраняла в файл human.data, и другую функцию, которая бы читала файл human.data,
# десериализовывала его содержимое и выводила результат на печать. Примечание: чтоб у экземпляров
# Human были разные значения атрибутов, можно воспользоваться функциями random.randint() и random.choice().

import random
import pickle


class Human:
    def __init__(self, name, surname, age, education, bloodgroup):
        # Задаем параметры экземпляров
        self.name = name
        self.surname = surname
        self.age = age
        self.education = education
        self.bloodgroup = bloodgroup

    def options(self):
        # Выводим информацию об экземпляре
        print(f"{self.name} {self.surname}: {self.education} speciality, {self.age} years, "
              f"{self.bloodgroup} bloodgroup")


# Фабрика экземпляров
def example_fabric():
    # Генерируем список имен
    name_lst = ['Ivan', 'Oleg', 'Petr', 'Alexey', 'Maxim', 'Dmitriy']
    name = random.choice(name_lst)
    # Генерируем список фамилий
    surname_lst = ['Ivanov', 'Olegov', 'Petrov', 'Alexeev', 'Maximov', 'Dmitriev']
    surname = random.choice(surname_lst)
    # Генерируем возраст
    age = random.randint(18, 35)
    # Генерируем список образования
    education_lst = ['Maths', 'Physics', 'Biology', 'Chemistry']
    education = random.choice(education_lst)
    # Генерируем группу крови
    bloodgroup = random.randint(1, 4)
    # Формируем экземпляр
    return name, surname, age, education, bloodgroup


# Сериализация данных
def my_serialization(hlst, pth):
    with open(pth, "wb") as f:  # первая буква - режим открытия (w - запись), вторая буква - тип кодирования
        pickle.dump(len(hlst), f, protocol=pickle.HIGHEST_PROTOCOL)
        for hum in hlst:
            pickle.dump(hum, f, protocol=pickle.HIGHEST_PROTOCOL)  # запись/сохранение объекта в файл

    return pth

            
# Десериализация данных
def my_deserialization(pth):
    with open(pth, "rb") as f:
        humans = []
        num = pickle.load(f)
        i = 0
        while i < num:
            humans.append(pickle.load(f))
            i += 1

    # Выводим данные экземпляров на экран
    for human in humans:
        human.options()

    return humans


# Задаем кол-во экземпляров
n = int(input("Введите количество экземпляров: "))
# Генерируем экземпляры
humans_lst = [Human(*example_fabric()) for _ in range(n)]

# Выводим данные экземпляров на экран
for human in humans_lst:
    human.options()

# Указываем путь файла
path = r'.\human.data'  # относительный путь

# Сериализуем
my_serialization(humans_lst, path)

# Десериализуем
my_deserialization(path)

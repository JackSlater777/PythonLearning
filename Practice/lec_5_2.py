# Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать
# от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).

import time
import random
import importlib.util


spec = importlib.util.spec_from_file_location(
    name="my_module",  # note that ".test" is not a valid module name
    # location="/path/to/.test.py",
    location="lec_5_1.py",
)
my_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_module)
Man = my_module.Man


# class Man:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def solve_task():
#         print("I'm not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task():
        think_time = random.randint(0, 3) + 3
        time.sleep(think_time)
        Man.solve_task()


p = Pupil('Petr')
print(Man.__dict__)

import random
import time
import importlib.util

spec = importlib.util.spec_from_file_location(
    name="my_module",  # note that ".test" is not a valid module name
    location="lec_5.1.py",
)
my_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_module)
Man = my_module.Man
#print(my_module.__dict__)



class Pupil(Man):
    def __init__(self, name):
        self.__name = name

    @staticmethod
    def solve_task():
        #think_time = random.randint(0, 3) + 3
        #time.sleep(think_time)
        Man.solve_task()

# SOLID

p = Pupil("Petr")
print(p._Pupil__name)
p.solve_task()
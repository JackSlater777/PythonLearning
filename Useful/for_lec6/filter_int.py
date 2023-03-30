import pytest


class Tank:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def __repr__(self):
        return f"Tank with {self.speed=}, {self.power=}"


def fun():
    pass


t1 = Tank(10, 200)
t2 = Tank(20, 150)
t3 = Tank(30, 100)

lst = [t2, t1, t3]
lst.sort(key=lambda i: i.speed)
print(lst)

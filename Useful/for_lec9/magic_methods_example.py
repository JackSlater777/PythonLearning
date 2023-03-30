class Tank:
    def __init__(self, power, speed, num):
        self._power = power
        self._speed = speed
        self._num = num

    def __lt__(self, other):
        if self._power == other._power:
            return self._speed < other._speed
        else:
            return self._power < other._power

    def __le__(self, other):
        if self._power == other._power:
            return self._speed <= other._speed
        else:
            return self._power <= other._power

    def __eq__(self, other):
        return self._power == other._power and self._speed == other._speed



    def __repr__(self):
        return f"{type(self).__name__} N{self._num} id: {id(self)}"

    def __str__(self):
        return f"{type(self).__name__} N{self._num}"

    def shoot(self):
        pass

class TankT34(Tank):
    def shoot(self):
        print("Ba-bah")

class TankTiger(Tank):
    def shoot(self):
        print("BA-BAH")

class TankAbrams(Tank):
    def shoot(self):
        print("buh")


t1 = TankT34(30, 30, 1)
t2 = TankTiger(40, 20, 1)
t3 = TankTiger(40, 30, 2)
t4 = TankTiger(40, 10, 3)
t5 = TankAbrams(10, 10, 1)

print(f"{t1 == t2=}")

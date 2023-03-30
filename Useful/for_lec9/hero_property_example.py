class HeroException(Exception):
    pass


class Hero:
    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if isinstance(value, int):
            self._power = value
        else:
            raise HeroException('Bad power')

    def __add__(self, other):
        return Hero(self.power + other.power)


h = Hero(1000)
h.power = "10000"
print(h.power)

h2 = Hero(5000)
h3 = h + h2
print(h3.power)

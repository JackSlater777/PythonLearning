class Pizza:
    def __init__(self):
        self._status = "Not ready"

    def make_base(self):
        print("Base ready")

    def add_ingr(self):
        pass

    def bake(self):
        print("Bake done")
        self._status = "Ready"

    def get_status(self):
        print(f"{self._status}")
        return self._status


class MeatPizza(Pizza):
    def add_ingr(self):
        print("Add meat")


class VegPizza(Pizza):
    def add_ingr(self):
        print("Add vegetables")


class MushPizza(Pizza):
    def add_ingr(self):
        print("Add mushrooms")


def make_pizza(pizza):
    pizza.make_base()
    pizza.add_ingr()
    pizza.bake()
    pizza.get_status()


menu = (MeatPizza, VegPizza, MushPizza)
i = int(input('Input pizza type: 0 - meat, 1 - veg, 2 - mush: '))
make_pizza(menu[i]())

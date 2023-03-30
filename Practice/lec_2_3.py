# Спроектировать классы (один или несколько) для игры в танки и
# создать экземпляры этих классов.

# Ввести следующие параметры экземпляра - минимальная дальность стрельбы, шанс уклонения
# Написать функции для ai и раунды
class MediumTank:
    def __init__(self, number, name, power, armour, speed):
        self.number = number
        self.name = name
        self.power = power
        self.armour = armour
        self.speed = speed

    def tank_options(self):
        print(f"№{self.number}: {self.name}, {self.power=} {self.armour=} {self.speed=}")

    def move(self, m):
        m -= self.speed
        print(f"До вражеского танка осталось {m} метров")
        return m

    def shoot(self, vs_tank):
        # vs_tank - lst[y]
        print(f"Вы нанесли {self.power} урона танку противника {vs_tank.name}")
        vs_tank.armour -= self.power
        if vs_tank.armour <= 0:
            print(f"Танк противника {vs_tank.name} подбит!")
        elif vs_tank.armour > 0:
            print(f"У танка противника {vs_tank.name} осталось {vs_tank.armour} прочности")


def pick_your_tank(lst):
    tank_choice = int(input(f"Выберите номер своего танка (введите номер от 0 до {len(lst) - 1}): "))
    print(f"Ваш танк - {lst[tank_choice].name}")
    return tank_choice


def pick_enemy_tank(lst):
    enemy_choice = int(input(f"Выберите номер танка противника (введите номер от 0 до {len(lst) - 1}): "))
    print(f"Танк врага - {lst[enemy_choice].name}")
    return enemy_choice


def on_action_choice(lst, x, y, m):
    action_choice = int(input("Хотите передвигаться или стрелять? (введите 1 или 2): "))
    if action_choice == 1:
        lst[x].move(m)
    elif action_choice == 2:
        lst[x].shoot(lst[y])


panther_tank = MediumTank(0, "Panthera", 25, 55, 40)
t34_tank = MediumTank(1, "T-34", 20, 50, 50)

tank_lst = [panther_tank, t34_tank]

for tank in tank_lst:
    tank.tank_options()

#  m
distance = 500

#  x или индекс lst[x]
your_tank = pick_your_tank(tank_lst)
#  y или индекс lst[y]
enemy_tank = pick_enemy_tank(tank_lst)

on_action_choice(tank_lst, your_tank, enemy_tank, distance)

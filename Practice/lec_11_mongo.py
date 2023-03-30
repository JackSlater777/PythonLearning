# ������� NoSQL ���� ������ ��� ������� ������ �����. ������������� ������� � ���������� ������� ����� ���������, 
# ��� ������������ ������� (�����, �������) �, ����������, ������ ����� (�����, �������, ����, ����������). 
# API ��� ������ � �� ������ ��������������� ����� ��������� �� �����������, ���� ����������� �� ����, ������, 
# ������ � ���������� �������. ��� ����������� ������ ������� ������������ ��������������.

import mongoengine as me
# import datetime


# ������������ � ���� MongoDB �� ��������� ������ 
conn = me.connect('taxi') 
print(conn) 


# ��������� ��������� �������� 
class User(me.Document):
    # id = me.StringField(max_length=50)  
    id = me.BinaryField(primary_key=True)
    login = me.StringField(max_length=50) 
    # rating = me.StringField(max_length=50)
    rating = me.FloatField(min_value=0.0, max_value=5.0)
    coordinates = me.DictField()

    def __repr__(self): 
        return f"<User(id={self.id}, login='{self.login}', rating={self.rating}, coordinates={self.coordinates})>"

    # ��������� ��������� ������ � �������
    def find_the_nearest_car(self, lst):
        min_dist = 100000000000
        car_id = 0
        # ��������� ���������� �� ������� �� ������ ������
        for car in lst:
            dist_x = abs(car.coordinates['x'] - self.coordinates['x'])
            dist_y = abs(car.coordinates['y'] - self.coordinates['y'])
            dist = (dist_x ** 2 + dist_y ** 2) ** 0.5  # �� ������� ��������
            if min_dist > dist:
                min_dist = dist
                car_id = car.id
        print(f"��������� ������ � ������� � id: {car_id}")
        print(f"���������� �� ������ �� �������: {min_dist}")
            

# ��������� ��������� �����
class Car(me.Document):
    # id = me.StringField(max_length=50)
    id = me.BinaryField(primary_key=True)
    # number = me.StringField(max_length=50)
    number = me.IntField()
    # rating = me.StringField(max_length=50)
    rating = me.FloatField(min_value=0.0, max_value=5.0)
    # price = me.StringField(max_length=50)
    price = me.IntField()
    # coordinates = me.StringField(max_length=50)
    coordinates = me.DictField()

    def __repr__(self): 
        return f"<Car(id={self.id}, number={self.number}, rating={self.rating}, " \
               f"price={self.price}, coordinates={self.coordinates})>"


def find_the_cheapest_car(lst):
    min_price = 1000000
    car_id = 0
    for car in lst:
        if min_price > car.price:
            min_price = car.price
            car_id = car.id
    print(f"����� ������� ����� �� ������ � id: {car_id}")
    print(f"�����: {min_price}")


# ������� ��������
user1 = User(id=1, login='ivanovi', rating=3.9, coordinates={'x': 33, 'y': 92}) 
user1.save()
user2 = User(id=2, login='petrovp', rating=4.5, coordinates={'x': 60, 'y': 33}) 
user2.save()
user3 = User(id=3, login='orlovi', rating=5.0, coordinates={'x': 99, 'y': 7}) 
user3.save()

# ������� ������
car1 = Car(id=1, number=725, rating=4.5, price=100, coordinates={'x': 25, 'y': 50}) 
car1.save()
car2 = Car(id=2, number=444, rating=4.0, price=150, coordinates={'x': 73, 'y': 88}) 
car2.save()
car3 = Car(id=3, number=804, rating=3.8, price=200, coordinates={'x': 10, 'y': 22}) 
car3.save()
car4 = Car(id=4, number=615, rating=5.0, price=110, coordinates={'x': 55, 'y': 44}) 
car4.save()

# ������� ������ �����
cars = [car1, car2, car3, car4]

# ������� ��������� ������ ��� ������� �1
user1.find_the_nearest_car(cars)

# ������� ����� ������� �������
find_the_cheapest_car(cars)

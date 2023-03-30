class Employee:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.salary = 100000

    def __add__(self, other):
        return self.salary + other.salary

    def say_my_name(self):
        print(f"I'm {self.first_name} {self.last_name}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


e1 = Employee('Petr', 'Petrov')
print(e1)


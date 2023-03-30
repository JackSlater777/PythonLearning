class Employee:
    state = 'RF'

    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def show_employee(self):
        print(f'{self._name} {self._surname} with salary {self._salary}')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, bonus):
        if self._salary + bonus < 0:
            print("Incorrect bonus")
        else:
            self._salary += bonus

    @salary.deleter
    def salary(self):
        print('Salary deleted')


e = Employee('Petr', 'Petrov', 100000)
print(e.salary)
e.salary = -1000000
print(e.salary)
del e.salary


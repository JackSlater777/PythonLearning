# Написать функцию для подсчета количества рабочих дней между двумя датами
# (даты передаются в качестве параметров).

from datetime import date
from datetime import timedelta


def calc_work_days(fst, sec):
    delta = timedelta(days=1)
    workdays = 0
    while sec >= fst:
        if sec.weekday() < 5:
            workdays += 1
        sec -= delta
    return workdays


first_data = date.fromisoformat('2022-01-22')
second_data = date.fromisoformat('2022-02-02')
# first_data = date.fromisoformat(input("Введите стартовую дату в формате 2000-01-20 (год-месяц-день): "))
# second_data = date.fromisoformat(input("Введите конечную дату в формате 2000-01-20 (год-месяц-день): "))
print(calc_work_days(first_data, second_data))

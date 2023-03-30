from iterator_example import MyIter
from generator import my_gen

lst = [1, 2, 3, 4, 10, 5, 2, 7, 10]

cnt = 0
for i in lst:
    if i == 10:
        print(f"{cnt}-й элемент равен 10")
    cnt += 1

for i in my_gen(lst, 10):
    print(f"{i}-й элемент равен 10")

for i in my_gen(lst, 2):
    print(f"{i}-й элемент равен 2")

# for i in MyIter(lst, 10):
#     print(f"{i}-й элемент равен 10")
#
# for i in MyIter(lst, 2):
#     print(f"{i}-й элемент равен 2")
import pickle
from worker import Worker

john = Worker()
john.set_name('John')
john.set_age(25)
john.set_salary(1000)
jack = Worker()
jack.set_name('Jack')
jack.set_age(26)
jack.set_salary(2000)

lst = [jack, john]
with open("dumpfile", "wb") as f:
    pickle.dump(len(lst), f)
    for hum in lst:
        pickle.dump(hum, f)

with open("dumpfile", "rb") as f:
    humans = []
    num = pickle.load(f)
    i = 0
    while i < num:
        humans.append(pickle.load(f))
        i += 1

print(humans)
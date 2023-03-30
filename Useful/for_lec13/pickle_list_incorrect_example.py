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

with open("dumpfile", "wt") as f:
    f.write(str(pickle.dumps(jack)))
    f.write(str(pickle.dumps(john)))

humans = []
with open("dumpfile", "rt") as f:
    for line in f:
        humans.append(pickle.loads(bytes(line)))

print(humans)
# 0 1 1 2 3 5
class Fibonacci:

    def __init__(self, N):
        self.n = 0
        self.a = 0
        self.b = 1
        self.max = N

    def __iter__(self):
        # сами себе итератор: в классе есть метод next()
        return self

    def __next__(self):
        if self.n < self.max:
           #               |self.a self.b|
           #    0      1       1      2     3      5
           #      1       1      1
            a = self.a
            self.n = self.n + 1
            self.a = self.b
            self.b = a + self.b
           #1    2        1      2
            return a
        else:
            raise StopIteration


print(list(Fibonacci(10)))


class MyIter:
    def __init__(self, n):
        self.i = 0
        self.cnt = 0
        self.n = n  # 5

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < self.n:
            res = self.i
            self.i += 2
            self.cnt += 1
            return res
        else:
            raise StopIteration


for i in MyIter(100):
    print(i)

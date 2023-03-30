class MyIter:
    def __init__(self, lst, n):
        self._lst = lst
        self._n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self._i
        while i < len(self._lst):
            if self._lst[i] == self._n:
                self._i = i + 1
                return i
            i += 1
        raise StopIteration
# Реализовать итератор, который бы "читал" заданный текст по параграфам.
# Символ параграфа задается отдельно.

class MyIter:
    def __init__(self, p):
        self._p = p
        self._t = '\n'
        self._f = open(path)

    def __iter__(self):
        return self

    def __next__(self):
        buffer = ''
        self._s = self._f.read(1)
        while self._s:
            if self._s != self._t:
                buffer += self._s
            else:
                return buffer
            self._s = self._f.read(1)
        self._f.close()
        raise StopIteration

    # это деструктор, который автоматически вызывается, когда счетчик ссылок объекта становится равным нулю).
    # Тогда если вдруг не сработала строка 22 (если перед этим исключение случилось, или мы просто недовызывали next
    # до конца текста), файл всё равно закроется вместе с удалением экземпляра MyIter().
    def __del__(self):
        self._f.close()


path = r'.\text.txt'  # относительный путь
for i in MyIter(path):
    print(f"Параграф: {i}")

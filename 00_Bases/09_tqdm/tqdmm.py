class PTqdm:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        for i in self._iterable:
            yield i

    def __str__()



class MyIter():
    def __init__(self, collection, cursor):
        if cursor < -1 and cursor < len(collection):
            raise ValueError()
        self._collection = collection
        self._cursor = cursor

    def first(self):
        self._cursor = -1

    def last(self):
        self._cursor = len(self._collection) - 1
        return self._cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]

    def current(self):
        return self._collection[self._cursor]

    def __iter__(self):
        return self._cursor

    def prev(self):
        if self._cursor + 1 >= len(self._collection) or self._cursor == 0:
            raise StopIteration()
        self._cursor -= 1
        return self._collection[self._cursor]

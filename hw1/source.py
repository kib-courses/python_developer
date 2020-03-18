from array import array


class ArrayList:
    """
    Класс должен реализовывать протокол Sequence
    """
    dictionary = {"i": int, "f": float, "u": str}


    def __init__(self, element_type, elmnts=None):
        """
        Список должен быть типизированым
        Внутреннее хранение должно быть реализовано
        на array.array
        """
        self.container = array(element_type) if elmnts is None \
            else array(element_type, elmnts)
        self.type = self.dictionary[element_type]


    def __getitem__(self, index):
        return self.container[index]

    def __len__(self):
        return len(self.container)

    def __contains__(self, item):
        if type(item) == self.type:
            for x in self:
                if item == x:
                    return True
        return False

    def __iter__(self):
        for idx in range(len(self)):
            yield self.container[idx]

    def __reversed__(self):
        idx = len(self) - 1
        while idx != 0:
            yield self.container[idx]
            idx -= 1

    def index(self, item):
        if type(item) == self.type:
            for idx, x in enumerate(self):
                if x == item:
                    return idx
        return None

    def count(self, item):
        cnt = 0
        if type(item) == self.type:
            for x in self:
                if x == item:
                    cnt += 1
            return cnt
        else:
            return None


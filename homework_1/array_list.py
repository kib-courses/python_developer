import array


def words_to_letters(word_list):
    letter_list = []
    word_lengths = []

    for word in word_list:
        word_lengths.append(len(word))
        for letter in word:
            letter_list.append(letter)

    return letter_list, word_lengths


def letters_to_word(letter_arr):
    word = ""

    for letter in letter_arr:
        word += letter

    return word


class ArrayList:
    def __init__(self, *args):
        if args:
            type_is_int = False
            type_is_float = False
            type_is_str = False

            for item in args:
                if isinstance(item, int):
                    type_is_int = True
                elif isinstance(item, float):
                    type_is_float = True
                elif isinstance(item, str):
                    type_is_str = True
                else:
                    raise TypeError("ArrayList can contain only int, float, str types")

            if type_is_int and not type_is_float and not type_is_str:
                self.array = array.array('q', args)
                self.array_type = int
                self.word_lengths = None
            elif type_is_float and not type_is_str:
                self.array = array.array('d', args)
                self.array_type = float
                self.word_lengths = None
            elif type_is_str and not type_is_int and not type_is_float:
                new_args, sizes = words_to_letters(args)

                self.array = array.array('u', new_args)
                self.array_type = str
                self.word_lengths = array.array('H', sizes)
            else:
                raise TypeError("The ArrayList class is typed")

        else:
            raise TypeError("To create an object, you need at least one value")

    def __getitem__(self, key):
        try:
            if self.array_type == str:
                result = ""
                index = sum(self.word_lengths[:key])

                for _ in range(self.word_lengths[key]):
                    result += self.array[index]
                    index += 1

                return result
            else:
                return self.array[key]
        except IndexError as error:
            raise IndexError("The passed key contains an error") from error

    def __len__(self):
        if self.array_type == str:
            return len(self.word_lengths)
        else:
            return len(self.array)

    def __contains__(self, value):
        if self.array_type == str:
            for word in self:
                if value == word:
                    return True
            else:
                return False
        else:
            return value in self.array

    def __iter__(self):
        self.__index = 0
        if self.array_type == str:
            self.__word_index = 0
        return self

    def __next__(self):
        if self.array_type == str:
            if self.__word_index < len(self.word_lengths):
                tmp = self.__index
                self.__index += self.word_lengths[self.__word_index]
                self.__word_index += 1

                end_of_word = tmp + self.word_lengths[self.__word_index - 1]
                return letters_to_word(self.array[tmp:end_of_word])
            else:
                raise StopIteration
        else:
            if self.__index < len(self):
                self.__index += 1
                return self.array[self.__index - 1]
            else:
                raise StopIteration

    def __reversed__(self):
        new_array = array.array(self.array.typecode)
        if self.array_type == str:
            for item in self:
                new_array = array.array(self.array.typecode, [*item]) + new_array
        else:
            for item in self:
                new_array = array.array(self.array.typecode, [item]) + new_array
        self.array = new_array

        if self.array_type == str:
            new_sizes = array.array('H')
            for size in self.word_lengths:
                new_sizes = array.array('H', [size]) + new_sizes
            self.word_lengths = new_sizes

        return self

    def count(self, value):
        count = 0
        for item in self:
            if value == item:
                count += 1
        return count

    def index(self, value):
        for index, item in enumerate(self):
            if value == item:
                return index
        else:
            raise ValueError("Your value is not in this object")

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError("Key must be of type int")
        elif not isinstance(value, self.array_type):
            raise ValueError("Type of value must match type of ArrayList")
        else:
            try:
                if self.array_type == str:
                    index = sum(self.word_lengths[:key])
                    begin = self.array[:index]
                    end = self.array[index + self.word_lengths[key]:]

                    self.array = begin + array.array('u', [*value]) + end
                    self.word_lengths[key] = len(value)
                else:
                    self.array[key] = value
            except IndexError as error:
                raise IndexError("The passed key contains an error") from error

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise KeyError("Key must be of type int")
        else:
            try:
                if self.array_type == str:
                    index = sum(self.word_lengths[:key])
                    begin = self.array[:index]
                    end = self.array[index + self.word_lengths[key]:]

                    self.array = begin + end
                    del self.word_lengths[key]
                else:
                    del self.array[key]
            except IndexError as error:
                raise IndexError("The passed key contains an error") from error

    def insert(self, key, value):
        if not isinstance(key, int):
            raise KeyError("Key must be of type int")
        elif not isinstance(value, self.array_type):
            raise ValueError("Type of value must match type of ArrayList")
        else:
            try:
                if self.array_type == str:
                    index = sum(self.word_lengths[:key])
                    begin = self.array[:index]
                    end = self.array[index:]

                    self.array = begin + array.array('u', [*value]) + end
                    self.word_lengths = self.word_lengths[:key] +\
                                        array.array('H', [len(value)]) +\
                                        self.word_lengths[key:]
                else:
                    begin = self.array[:key]
                    end = self.array[key:]
                    new_item = array.array(self.array.typecode, [value])

                    self.array = begin + new_item + end
            except IndexError as error:
                raise IndexError("The passed key contains an error") from error

    def __iadd__(self, other):
        try:
            self.array += other.array
            if self.array_type == str:
                self.word_lengths += other.word_lengths
            return self
        except TypeError as error:
            raise TypeError("Different types of ArrayList cannot be added") from error

    def append(self, value):
        if not isinstance(value, self.array_type):
            raise ValueError("Type of value must match type of ArrayList")
        else:
            try:
                if self.array_type == str:
                    self.array = self.array + array.array('u', [*value])
                    self.word_lengths += array.array('H', [len(value)])
                else:
                    self.array = self.array + array.array(self.array.typecode, [value])
            except IndexError as error:
                raise IndexError("The passed key contains an error") from error

    def clear(self):
        self.array = None
        self.word_lengths = None
        self.array_type = None

    def extend(self, iterable):
        iter(iterable)

        try:
            for item in iterable:
                self.append(item)
        except TypeError as error:
            raise TypeError("An invalid type value was passed") from error

    def pop(self, key=None):
        if key is not None:
            try:
                tmp = self[key]
                del self[key]
                return tmp
            except IndexError as error_1:
                raise IndexError("Pop index out of range") from error_1
            except TypeError as error_2:
                raise TypeError("An invalid type value was passed") from error_2
        else:
            try:
                tmp = self[len(self.array) - 1]
                del self[len(self.array) - 1]
                return tmp
            except IndexError as error:
                raise IndexError("Pop from empty ArrayList") from error

    def reverse(self):
        self.__reversed__()

    def remove(self, value):
        for index, item in enumerate(self):
            if value == item:
                del self[index]
                return
        else:
            raise ValueError("ArrayList does not contain a value")

    def __str__(self):
        if self.array_type == str:
            result = "ArrayList("
            cursor = 0

            for index, size in enumerate(self.word_lengths):
                result += str(self.array[cursor:cursor + size])
                if index != len(self.word_lengths) - 1:
                    result += ", "
                cursor += size

            return result + ")"
        else:
            return f"ArrayList({self.array})"


if __name__ == '__main__':
    print("\033[31m\033[1mThis file is just a module.\033[0m")

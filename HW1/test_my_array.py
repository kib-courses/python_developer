import pytest
from my_array import Array


def startup():
     Array()
     return True


def test_startup():
    assert startup()


def int_startup():
    Array(1)
    return True


def test_int_startup():
    assert int_startup()


def str_startup():
    Array('str')


def test_str_startup():
    with pytest.raises(TypeError):
        str_startup()


a = Array(1, 2, 3, 4, 5)


def iter():
    b = [_ for _ in a]
    return b


def test_iter():
    assert iter() == [1, 2, 3, 4, 5]


def test_len():
    assert len(a) == 5


def test_reversed():
    r = 5
    for i in reversed(a):
        assert i == r
        r -= 1


def test_getitem():
    assert a[1] == 2


def test_index():
    assert a.index(5) == 4


def test_count():
    b = Array(1, 1, 2)
    assert b.count(1) == 2



import pytest

from chaining_dictionary import ChainingDictionary


@pytest.fixture
def empty_chaining_dictionary():
    dictionary = ChainingDictionary()
    return dictionary


def test_empty(empty_chaining_dictionary):
    items = []
    for i in empty_chaining_dictionary.items():
        items.append(i)
    assert len(items) == 0


def test_not_existed_key(empty_chaining_dictionary):
    with pytest.raises(KeyError):
        a = empty_chaining_dictionary[1]
    with pytest.raises(KeyError):
        empty_chaining_dictionary[1] = 1


def test_unhashable_key(empty_chaining_dictionary):
    with pytest.raises(TypeError):
        a = empty_chaining_dictionary[[1]]
    with pytest.raises(TypeError):
        empty_chaining_dictionary[[1]] = 1
    with pytest.raises(TypeError):
        empty_chaining_dictionary.add([1], 1)


def test_add(empty_chaining_dictionary):
    empty_chaining_dictionary.add(1, 2)
    empty_chaining_dictionary.add(2, 3)
    assert len(empty_chaining_dictionary) == 2
    assert empty_chaining_dictionary.__str__() == str({1: 2, 2: 3})


def test_extend(empty_chaining_dictionary):
    empty_chaining_dictionary.add(1, 2)
    empty_chaining_dictionary.add(2, 3)
    empty_chaining_dictionary.add(3, 4)
    assert len(empty_chaining_dictionary) == 3
    assert len(empty_chaining_dictionary._buckets) == 3
    empty_chaining_dictionary.add(4, 5)
    assert len(empty_chaining_dictionary) == 4
    assert len(empty_chaining_dictionary._buckets) == 7


def test_order(empty_chaining_dictionary):
    empty_chaining_dictionary.add(2, 1)
    empty_chaining_dictionary.add(1, 2)
    items = []
    for key, value in empty_chaining_dictionary.items():
        items.append((key, value))
    assert items == [(2, 1), (1, 2)]


def test_get_value_by_index(empty_chaining_dictionary):
    empty_chaining_dictionary.add(1, 2)
    empty_chaining_dictionary.add(2, 3)
    assert empty_chaining_dictionary[2] == 3


def test_set_value_by_index(empty_chaining_dictionary):
    empty_chaining_dictionary.add(1, 2)
    empty_chaining_dictionary.add(2, 3)
    assert empty_chaining_dictionary[2] == 3
    empty_chaining_dictionary[2] = 4
    assert empty_chaining_dictionary[2] == 4


def test_add_existed_key(empty_chaining_dictionary):
    empty_chaining_dictionary.add(1, 2)
    with pytest.raises(KeyError):
        empty_chaining_dictionary.add(1, 3)

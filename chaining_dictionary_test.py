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
        empty_chaining_dictionary.__add__([1], 1)


@pytest.fixture
def chaining_dictionary():
    dictionary = ChainingDictionary()
    return dictionary
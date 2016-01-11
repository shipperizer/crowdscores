from list_length import list_length
from single_method_list import SingleMethodList


def test_empty_list():
    s_list = SingleMethodList([])
    assert len(s_list._list) == list_length(s_list)


def test_single_item_list():
    s_list = SingleMethodList([0])
    assert len(s_list._list) == list_length(s_list)


def test_large_list():
    s_list = SingleMethodList([i for i in xrange(0, 100000)])
    assert len(s_list._list) == list_length(s_list)


def test_list_of_different_objects():
    class TestObject:
        def __init__(self):
            pass
    s_list = SingleMethodList([0, 1, "two", TestObject(), [1,2,3]])
    assert len(s_list._list) == list_length(s_list)

import pytest

from test_repo import A, add, forloop, noreturn, union


def test_A():
    a = A("test")
    assert a.test() == "test"


def test_add():
    assert add(1, 2) == 3


def test_union():
    assert union("a", "b") == "ab"


def test_forloop():
    assert forloop([1, 2, 3]) == sum([1, 2, 3])


def test_noreturn():
    with pytest.raises(RuntimeError):
        noreturn()

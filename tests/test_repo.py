from test_repo import A, add, union


def test_A():
    a = A("test")
    assert a.test() == "test"


def test_add():
    assert add(1, 2) == 3


def test_union():
    assert union("a", "b") == "ab"

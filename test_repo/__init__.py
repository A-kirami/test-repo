class A:
    def __init__(self) -> None:
        pass

    def __add__(self, other):
        raise NotImplementedError

    def __test__(self):
        ...

    def test(self):
        ...


def add(a: int, b: int) -> int:
    return a + b


def forloop():
    for i in range(0, 10):
        if i > 5:
            return True

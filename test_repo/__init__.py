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

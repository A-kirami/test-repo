from typing import List, NoReturn


class A:
    def __init__(self, text: str) -> None:
        self.text = text

    def test(self):
        return self.text


def add(a: int, b: int) -> int:
    return a + b


def union(a: str, b: str) -> str:
    return a + b


def noreturn() -> NoReturn:
    raise RuntimeError


def forloop(iter: list[int]) -> int:
    return sum(iter)

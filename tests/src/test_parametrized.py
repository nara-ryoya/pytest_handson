import pytest

from src.parametrized import is_jihai

"""良くない書き方"""


def test_bad_is_jihai() -> None:
    assert not is_jihai("1s")
    assert is_jihai("tan")
    assert is_jihai("nan")


@pytest.mark.parametrize(
    ("pai", "expected"), [("1s", False), ("tan", True), ("nan", True)]
)
def test_is_jihai(pai: str, expected: bool) -> None:
    assert is_jihai(pai) == expected

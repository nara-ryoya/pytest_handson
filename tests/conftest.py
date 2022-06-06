"""前処理・後処理の関数を記述する関数
conftest.pyに記述することで、conftest.pyがあるディレクトリ以下の全ての.pyファイルで
importしなくても使える。
"""

import json
import pathlib
from typing import Generator, List, Tuple, TypedDict

import pytest


class EventDict(TypedDict):
    type: str
    pai: str
    player: int


class Paifu(TypedDict):
    players_name: List[str]
    event: List[EventDict]


@pytest.fixture
def paifu_json() -> Generator[Tuple[pathlib.Path, Paifu], None, None]:
    paifu_dict: Paifu = {
        "players_name": ["amachan", "lyu", "nara", "ogami"],
        "event": [
            {"type": "Discard", "pai": "1s", "player": 0},
            {"type": "Discard", "pai": "nan", "player": 1},
        ],
    }
    paifu_path = pathlib.Path("test_paifu.json")
    with open(paifu_path, "w") as f:
        json.dump(paifu_dict, f)

    yield paifu_path, paifu_dict

    paifu_path.unlink(missing_ok=False)

import json
import pathlib
from typing import List


def get_players_name(json_path: pathlib.Path) -> List[str]:
    """下のようなjsonファイルのpathlib.Pathが与えられた時に、players_nameを返す関数
    {
        "players_name": ["amachan", "lyu", "nara", "ogami"],
        "event": [
            {"type": "Discard", "pai": "1s", "player": 0},
            {"type": "Discard", "pai": "nan", "player": 1}
        ]
    }

    Args:
        json_path (pathlib.Path): 牌譜のjsonの場所を表すpathlib.Path

    Returns:
        List[str]: 4人のプレイヤー名
    """
    with open(json_path, "r") as f:
        paifu = json.load(f)

    return paifu["players_name"]

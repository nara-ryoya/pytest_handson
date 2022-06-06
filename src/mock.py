import pathlib

from .fixture import get_players_name


def last_oya(paifu_path: pathlib.Path) -> str:
    players_name = get_players_name(paifu_path)
    return players_name[-1]

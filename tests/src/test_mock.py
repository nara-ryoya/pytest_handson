from typing import List

import pytest

from src.mock import last_oya


@pytest.mark.parametrize(
    ("players_name", "expected"),
    [(["oi", "sonoken", "hori", "taro"], "taro")],
)
def test_last_oya(players_name: List[str], expected: str, mocker, paifu_json):
    mocker.patch("src.mock.get_players_name", return_value=players_name)
    """src.mock.last_oyaの関数内で使われているget_players_nameの返り値を、players_nameで置き換えてしまう処理。
    関数Aの中で関数Bが使われていて、「関数Bがこういう値を返す時に関数Aがこういう値を返してほしい!」というtestを書きたい時に便利。
    関数Bが組み込みの関数(datetimeとかosとか)でも使用することができる。


    注意: src.mock内で src.fixtureの関数をimportしていて、それをmockに置き換えているので、
        "src.mock.get_players_name"をモック化することに注意
        ("src.fixture.get_players_name"ではない)

    詳細は以下の記事を参照
    https://zenn.dev/re24_1986/articles/0a7895b1429bfa

    """
    paifu, _ = paifu_json
    ret_last_oya = last_oya(paifu)

    assert ret_last_oya == expected

from src.fixture import get_players_name


def test_get_players_name(paifu_json) -> None:
    """paifu_jsonを引数に入れることで、conftest.pyに記述してある前処理・後処理の関数を使えるようになる。
    型ヒントはつけていないものが多いので、つけなくて良い。
    """
    paifu_path, paifu = paifu_json
    players_name = get_players_name(paifu_path)
    assert players_name == paifu["players_name"]

from src.players import Player
from src.index import build_store
from src.users import User

def test_player_returns_id_user_id_x_player():
    store = build_store()
    new_user = User(store, "Allison Hill")
    player_x = Player(store, new_user, player_x = True)
    assert player_x.user_id == 1
    assert player_x.id == 1
    assert player_x.player == 'x'

def test_player_returns_id_user_id_o_player():
    store = build_store()
    new_user = User(store, "Jonah Hill")
    player_o = Player(store, new_user, player_o = True)
    assert player_o.user_id == 1
    assert player_o.id == 1
    assert player_o.player == 'o'

def test_player_returns_updated_store():
    store = build_store()
    new_user = User(store, "Allison Hill")
    player_x = Player(store, new_user, player_x = True)
    assert store['players'][player_x.id] == player_x


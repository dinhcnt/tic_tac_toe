from src.users import User
from src.index import build_store
from src.games import Game

def test_user_returns_id_and_name_object():
    store = build_store()
    new_user = User(store, 'Allison Hill')
    assert new_user.id == 1
    assert new_user.name == 'Allison Hill'

def test_user_returns_updated_store():
    store = build_store()
    new_user = User(store, 'Allison Hill')
    assert store['users'][new_user.id] == new_user

def test_all_user_games_returns_all_games_per_user():
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    user_3 = User(store, "Jack Black")
    game_1 = Game(store, user_1, user_2)
    game_2 = Game(store, user_1, user_3)
    all_user_1_games = user_1.all_games(store)
    assert all_user_1_games == [game_1, game_2]
from src.turn import Turn
from src.index import build_store, blank_state, store
from src.user import User
from src.game import Game
from src.square import Square

def test_turns_returns_turn_id_user_id():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    assert turn_1_user_1.id == 1
    assert turn_2_user_2.id == 2
    assert turn_3_user_1.id == 3

def test_turns_returns_user_id():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    assert turn_3_user_1.user_id == 1
    assert turn_2_user_2.user_id == 2

def test_turns_returns_game_id():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    assert turn_1_user_1.game_id == 1
    assert turn_2_user_2.game_id == 1

def test_turns_returns_updated_store():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    assert store['turns'][turn_1_user_1.id] == turn_1_user_1
    assert store['turns'][turn_2_user_2.id] == turn_2_user_2
    assert store['turns'][turn_3_user_1.id] == turn_3_user_1

def test_turn_adds_row_column():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,1)
    assert turn_1_user_1.row == 0
    assert turn_1_user_1.column == 1

def test_add_square_returns_Square_object_in_store():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    new_square = turn_1_user_1.square
    assert store['squares'][new_square.id] == turn_1_user_1.square

def test_add_square_returns_turn_object_in_store():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game,0,1)
    assert store['turns'][turn_1_user_1.id] == turn_1_user_1
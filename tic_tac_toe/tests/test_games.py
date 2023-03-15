from src.game import Game
from src.index import build_store, blank_state
from src.user import User
from src.board import Board
from src.turn import Turn

def test_games_returns_user_ids():
    state = blank_state
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    assert new_game.user_1_id == 1
    assert new_game.user_2_id == 2

def test_games_returns_board_id_game_id():
    state = blank_state
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    assert new_game.board_id == 1
    assert new_game.id == 1

def test_game_board_returns_board_object():
    state = blank_state
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    board = new_game.board
    assert store['boards'][new_game.board.id] == new_game.board

def test_games_returns_updated_store():
    state = blank_state
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    assert store['games'][new_game.id] == new_game

def test_all_turns_per_game_returns_all_turns_in_one_game():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    turn_4_user_2 = Turn(store, user_2, new_game, 1,1)
    all_turns = new_game.all_turns_per_game()
    assert all_turns == [turn_1_user_1, turn_2_user_2, turn_3_user_1, turn_4_user_2]

def test_all_turns_per_user_returns_all_turns_by_user():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1_user_1 = Turn(store, user_1, new_game, 0,0)
    turn_2_user_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    turn_4_user_2 = Turn(store, user_2, new_game, 1,1)
    turns_per_user_1 = new_game.all_turns_per_user(user_1)
    turns_per_user_2 = new_game.all_turns_per_user(user_2)
    assert turns_per_user_1 == [turn_1_user_1, turn_3_user_1]
    assert turns_per_user_2 == [turn_2_user_2, turn_4_user_2]

def test_games_returns_correct_square_id(): #or returns correct square_id??
    pass
    


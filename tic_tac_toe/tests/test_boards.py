from src.index import build_store, blank_state
from src.board import Board
from src.user import User
from src.game import Game
from src.square import Square
from src.turn import Turn

def test_board_returns_board_id():
    store = build_store()
    state = blank_state
    board = Board(store, state)
    assert board.id == 1

def test_board_returns_game_id():
    state = blank_state
    store = build_store()
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    new_board = Board(store, state, new_game)
    assert new_board.game_id == 1

def test_board_updates_store():
    state = blank_state
    store = build_store()
    new_board = Board(store, state)
    assert store['boards'][new_board.id] == new_board

def test_all_squares_returns_all_squares_objects():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1 = Turn(store, user_1, new_game, 0, 1)
    turn_2 = Turn(store, user_2, new_game, 0, 2)
    new_game.board.turn(turn_1)
    new_game.board.turn(turn_2)
    # breakpoint()
    assert new_game.board.all_squares == {turn_1.square_id: turn_1.square, turn_2.square_id: turn_2.square}

def test_all_squares_per_board_returns_all_squares():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1 = Turn(store, user_1, new_game, 0, 1)
    turn_2 = Turn(store, user_2, new_game, 0, 2)
    new_game.board.turn(turn_1)
    new_game.board.turn(turn_2)
    assert new_game.board.all_squares_per_board() == [turn_1.square, turn_2.square]
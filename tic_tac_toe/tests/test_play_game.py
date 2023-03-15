from src.board import Board
from src.game import Game
from src.index import build_store, store, blank_state
from src.square import Square
from src.turn import Turn
from src.user import User
from src.play_game import PlayGame

def test_PlayGame_initializes_name_1_2():
    bob = 'bob'
    john = 'john'
    new_game = PlayGame(bob, john)
    assert new_game.name_1 == bob
    assert new_game.name_2 == john

def test_create_game_returns_new_game_users_and_state():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        assert new_game.user_1.name == 'bob' 
        assert new_game.user_2.name == 'john'
        assert new_game.board.state == blank_state

def test_create_game_updates_store_with_board_and_game_obj():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        assert store['games'][new_game.id] == new_game
        assert store['boards'][new_game.board.id] == new_game.board

def test_make_turn_updates_state():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        assert new_game.board.state == [['x', None, None], 
                                        [None, None, None], 
                                        [None, None, None]]

def test_make_turn_creates_turn_object():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        assert len(store['turns']) == 1

def test_is_winner_returns_final_winner():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        match.make_turn(store, new_game, new_game.user_1, 2, 1) 
        match.make_turn(store, new_game, new_game.user_1, 3, 1)
        assert match.is_winner(new_game, new_game.user_1) == f"Match completed! {new_game.user_1.name} wins!"

def test_is_winner_returns_no_winner_yet():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        match.make_turn(store, new_game, new_game.user_1, 2, 1) 
        match.make_turn(store, new_game, new_game.user_2, 3, 1)
        assert match.is_winner(new_game, new_game.user_2) == None

def test_change_user_changes_current_user_and_user1_false_user2_true():
        match = PlayGame('bob', 'john')
        store = build_store()
        is_user_1 = True
        is_user_2 = False
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        is_user_1, is_user_2, current_user = match.change_user(is_user_1, new_game.user_1, is_user_2, new_game.user_2)
        assert is_user_1 == False
        assert is_user_2 == True
        assert current_user == new_game.user_2

def test_check_unique_move_returns_False_invalid_move():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        row = 1
        column = 1
        assert match.check_unique_move(new_game.board.state, row, column) == False

def test_check_unique_move_returns_True_valid_move():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        row = 1
        column = 2
        assert match.check_unique_move(new_game.board.state, row, column) == True

def test_check_unique_move_returns_False_invalid_move():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        match.make_turn(store, new_game, new_game.user_1, 1, 1)
        row = 1
        column = 1
        assert match.check_unique_move(new_game.board.state, row, column) == False

def test_check_valid_input_returns_true():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        row_input = 1 
        column_input = 1
        assert match.check_valid_input(row_input, column_input) == True

def test_check_valid_input_returns_false_with_letter_input():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        row_input = 1 
        column_input = 'a'
        assert match.check_valid_input(row_input, column_input) == False

def test_check_valid_input_returns_false_with_non_integer_input():
        match = PlayGame('bob', 'john')
        store = build_store()
        new_game = match.create_game(store, match.name_1, match.name_2)
        row_input = 1 
        column_input = -1
        assert match.check_valid_input(row_input, column_input) == False
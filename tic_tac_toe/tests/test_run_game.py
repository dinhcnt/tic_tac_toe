from src.board import Board
from src.game import Game
from src.index import build_store, store, blank_state
from src.square import Square
from src.turn import Turn
from src.user import User
from src.play_game import *

def test_run_game_creates_play_game_and_game_object():
    name_1 = 'Allison'
    name_2 = 'Jonah'
    user_1 = User(store, name_1)
    user_2 = User(store, name_2)
    match = PlayGame(name_1, name_2)
    game_1 = match.create_game(store, user_1, user_2)
    state = [[None, None, None], 
        [None, None, None], 
        [None, None, None]]
    assert match.name_1 == 'Allison'
    assert Game(store, user_1, user_2, state)

def 

def test_run_game_inner_while_loop_outputs_is_valid_true_to_break_loop():
    



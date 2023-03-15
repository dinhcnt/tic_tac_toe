from src.index import build_store, blank_state, store
from src.board import Board
from src.turn import Turn
from src.user import User

class Game: 
    def __init__(self, store, user_1, user_2, state):
        self.store = store
        self.user_1_id = user_1.id
        self.user_2_id = user_2.id
        self.user_1 = user_1
        self.user_2 = user_2
        self.id = len(store['games']) + 1
        self.board = Board(self.store, state, self)
        self.board_id = self.board.id
        self.store['games'][self.id] = self
    
    def all_turns_per_game(self):
        return [turns for turns in self.store['turns'].values() if turns.game_id == self.id]
    
    def all_turns_per_user(self, user):
        return [turns for turns in self.store['turns'].values() if turns.user_id == user.id]



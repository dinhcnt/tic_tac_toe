
from src.index import build_store, store, blank_state
from src.square import Square

class Turn:
    def __init__(self, store, user, game, row, column):
        self.store = store
        self.user_id = user.id
        self.game_id = game.id
        self.id = len(store['turns']) + 1
        self.square = Square(self.store, row, column, self)
        self.square_id = self.square.id
        self.row = row
        self.column = column
        store['turns'][self.id] = self




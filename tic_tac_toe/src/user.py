from src.index import build_store

class User:
    def __init__(self, store, name):
        self.store = store
        self.name = name
        self.id = len(self.store['users']) + 1
        store['users'][self.id] = self

    def all_games(self, store): #returns all the games that user played
        return [game for game in self.store['games'].values() if (game.user_1_id == self.id) or (game.user_2_id == self.id)]
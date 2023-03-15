from src.index import build_store, store

class Square: 
    def __init__(self, store, row, column, turn):
        self.store = store
        self.row = row
        self.column = column
        self.turn_id = turn.id
        self.id = len(store['squares']) + 1
        store['squares'][self.id] = self
        


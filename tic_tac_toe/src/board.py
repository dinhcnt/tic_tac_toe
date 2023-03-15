from src.index import build_store, blank_state

class Board:
    def __init__(self, store, state, game = False):
        self.store = store
        self.state = state
        if game:
            self.game_id = game.id
        self.id = len(store['boards']) + 1
        self.store['boards'][self.id] = self
        self.all_squares = {}
    
    def turn(self, turn): # square as the instance of the object of Square class
        self.square_id = turn.square_id
        self.all_squares[self.square_id] = turn.square

    def all_squares_per_board(self):
        return [square for square in self.store['squares'].values() if square.id in self.all_squares.keys()]
    
    def check_all_rows(self):
        is_row = sum([1 for row in self.state if len(set(row)) == 1 and set(row) != {None}])
        return 1 <= is_row

    def check_column(self, desired_index):
        column = set([row[desired_index] for row in self.state])
        if column == {None}:
            return False
        return 1 >= len(column)
    
    def check_all_columns(self):
        return 1 <= sum([1 for index in range(len(self.state)) if self.check_column(index)])

    def check_left_diagonal(self):
        is_diag = set([row[index] for index, row in enumerate(self.state)])
        if is_diag == {None}:
            return False
        return 1 == len(is_diag)

    def check_right_diagonal(self):
        is_diag = set([row[index] for index, row in enumerate(reversed(self.state))])
        if is_diag == {None}:
            return False
        return 1 == len(is_diag)

    def check_winner(self):
        if (self.check_all_rows() == True) or (self.check_all_columns() == True) or (self.check_left_diagonal() == True) or (self.check_right_diagonal() == True):
            return True
        return False
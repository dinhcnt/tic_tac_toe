from src.index import build_store
from src.boards import Board

class Player:
    def __init__(self, store, user, player_x = False, player_o = False):
        if player_x: 
            self.player = 'x'
        if player_o:
            self.player = 'o'
        # self.state = state
        self.user_id = user.id
        self.id = len(store['players']) + 1
        store['players'][self.id] = self

    # def make_move(self, state, row, column):
    #     new_state = state.state
    #     new_state[row][column] = self.player
    #     print(new_state)
    #     new_board = Board(new_state)
    #     return new_board


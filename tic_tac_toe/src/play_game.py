from src.board import Board
from src.game import Game
from src.index import build_store, store, blank_state
from src.square import Square
from src.turn import Turn
from src.user import User


class PlayGame:
    valid_inputs = [1,2,3]
    def __init__(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2

    def create_game(self, store, name_1, name_2):
        store = store
        user_1 = User(store, name_1)
        user_2 = User(store, name_2)
        state = [[None, None, None], 
        [None, None, None], 
        [None, None, None]]
        return Game(store, user_1, user_2, state)
    
    def make_turn(self, store, game, user, row, column):
        idx_row = row - 1
        idx_col = column - 1
        turn_1 = Turn(store, user, game, idx_row, idx_col)
        game.board.turn(turn_1)
        current_state = game.board.state
        if user == game.user_1:
            current_state[idx_row][idx_col] = 'x'
        if user == game.user_2:
            current_state[idx_row][idx_col] = 'o'    

    def is_winner(self, game, current_user):
        if game.board.check_winner():
            return self.final_winner(game, current_user)

    def change_user(self, is_user_1, user_1, is_user_2, user_2):
        if is_user_1:
            is_user_1 = False
            is_user_2 = True
            return is_user_1, is_user_2, user_2
        is_user_1 = True
        is_user_2 = False
        return is_user_1, is_user_2, user_1
    
    def check_unique_move(self, new_state, row, col):
        current_square = new_state[row-1][col-1]
        if current_square != None: 
            print('______________________________', '\n')
            print("Invalid move. This box has already been played. Input a different move.")
            print('______________________________', '\n')
            return False
        return True
    
    def check_valid_input(self, row, column):
        try:
            int(row)
            int(column)
        except ValueError:
            print('______________________________', '\n')
            print(f"Invalid input. Input one of the following values: {self.valid_inputs}")
            print('______________________________', '\n')
            return False
        if (int(row) not in self.valid_inputs) or (int(column) not in self.valid_inputs) :
            print('______________________________', '\n')
            print(f"Invalid input. Input one of the following values: {self.valid_inputs}")
            print('______________________________', '\n')
            return False
        return True
        
    def final_winner(self, game, user):
        print(game.board.state[0], '\n', game.board.state[1], '\n', game.board.state[2], '\n')
        user_winner = user.name
        print('______________________________', '\n')
        print(f"Match completed! {user_winner} wins!")
        print('______________________________', '\n')
        return True


# create game
# play game
# make turn
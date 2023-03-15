from src.board import Board
from src.game import Game
from src.index import build_store, store, blank_state
from src.square import Square
from src.turn import Turn
from src.user import User
from src.play_game import *

class RunGame:
    def __init__(self):
        print('______________________________', '\n')
        print("Let's play Tic Tac Toe! ")
        print('______________________________', '\n')
        name_1 = str(input("Who will be X? "))
        name_2 = str(input("Who will be O? "))

        match = PlayGame(name_1, name_2)
        game_1 = match.create_game(store, name_1, name_2)
        print('______________________________', '\n')
        print('\n',f"{name_1} goes first",'\n')
        print('______________________________', '\n')
        winner = False
        is_user_1 = True
        is_user_2 = False
        is_valid = False
        current_user = game_1.user_1

        while winner == False:

            print(game_1.board.state[0],'\n', game_1.board.state[1], '\n', game_1.board.state[2], '\n')

            while is_valid == False:

                row_input = input('Which row number (1-3) is your move? ')
                column_input = input('Which column number (1-3) is your move? ')
                if match.check_valid_input(row_input, column_input):
                    row = int(row_input)
                    column = int(column_input)
                    if game_1.board.state != blank_state:
                        is_valid = match.check_unique_move(game_1.board.state, row, column)
                    else:   
                        break
            print('______________________________', '\n')
            is_valid = False
            new_state = match.make_turn(store, game_1, current_user, row, column)
            if match.is_winner(game_1, current_user):
                break
            is_user_1, is_user_2, current_user = match.change_user(is_user_1, game_1.user_1, is_user_2, game_1.user_2)

            print(f"Now it's {current_user.name}'s turn. ", '\n')
        next_game = input('Would you like to play again? Y or N')
        if next_game == 'Y':
            RunGame()
        else:
            print('Thanks for playing. See you next time!')






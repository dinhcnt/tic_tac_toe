from src.board import Board
from src.game import Game
from src.index import build_store, store, blank_state
from src.square import Square
from src.turn import Turn
from src.user import User
from src.play_game import *

class RunGame:

    print("Let's play Tic Tac Toe! ")
    name_1 = str(input("Who will be X? "))
    name_2 = str(input("Who will be O? "))

    match = PlayGame(name_1, name_2)
    game_1 = match.create_game(store, name_1, name_2)
    print('\n',"X goes first",'\n')
    winner = False
    is_user_1 = True
    is_user_2 = False
    is_valid = False
    current_user = game_1.user_1

    while winner == False:

        print(game_1.board.state[0],'\n', game_1.board.state[1], '\n', game_1.board.state[2], '\n')

        while is_valid == False: 

            row = int(input('Which row number (1-3) is your move? '))
            column = int(input('Which column number (1-3) is your move? '))
            if game_1.board.state != blank_state:
                is_valid = match.check_unique_move(game_1.board.state, row, column)
            else:
                break
        print('______________________________', '\n')
        
        new_state = match.make_turn(store, game_1, current_user, row, column)
        match.is_winner(game_1, current_user)
        is_user_1, is_user_2, current_user = match.change_user(is_user_1, game_1.user_1, is_user_2, game_1.user_2)

        print(f"Now it's {current_user.name}'s turn. ")

#         if is_user_1:
#             new_state = match.make_turn(store, game_1, game_1.user_1, row, column)
#             # winner = game_1.board.check_winner()
#             # if winner:
#             #     break
#             # is_user_1 = False
#             # is_user_2 = True
#             print(f"Now it's {name_2}'s turn.", '\n')

#         elif is_user_2:
#             new_state = match.make_turn(store, game_1, game_1.user_2, row, column)
#             # winner = game_1.board.check_winner()
#             # if winner:
#             #     break
#             # is_user_2 = False
#             # is_user_1 = True
#             print(f"Now it's {name_1}'s turn.",'\n' )

# user = 
# match.final_winner()

    # print(game_1.board.state[0], '\n', game_1.board.state[1], '\n', game_1.board.state[2], '\n')
    # if is_user_1:
    #     user_winner = game_1.user_1.name
    # else:
    #     user_winner = game_1.user_2.name
    # print(f"Match completed! {user_winner} wins!")






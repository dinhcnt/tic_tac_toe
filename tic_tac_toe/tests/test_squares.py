from src.square import Square

def test_square_returns_row_can_column():
    square = Square(1, 2)
    assert square.row == 1
    assert square.column == 2

def test_square_returns_square_in_store():
    store = build_store()
    state = blank_state
    user_1 = User(store, "Allison Hill")
    user_2 = User(store, "Jonah Hill")
    new_game = Game(store, user_1, user_2, state)
    turn_1 = Turn(store, user_1, new_game, 0,0)
    turn_2 = Turn(store, user_2, new_game, 0,1)
    turn_3_user_1 = Turn(store, user_1, new_game, 0,2)
    assert store['squares'][turn_1]
    def __init__(self, store, row, column, turn)
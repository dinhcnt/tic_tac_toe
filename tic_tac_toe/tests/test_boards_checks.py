from src.board import Board
from src.index import build_store

def test_check_all_rows_returns_True_winner():
    store = build_store()
    state = [['x', 'x', 'o'], 
        [None, None, None], 
        ['o', 'o', 'o']]
    new_board = Board(store, state)
    assert new_board.check_all_rows() == True

def test_check_all_rows_returns_False_no_winner_yet():
    store = build_store()
    state =  [['x', 'x', 'o'], 
        [None, None, None], 
        ['o', 'o', None]]
    new_board = Board(store, state)
    assert new_board.check_all_rows() == False

def test_check_column_returns_True_winner_column():
    store = build_store()
    state = [['x', 'x', 'o'], 
        [None, None, 'o'], 
        ['o', None, 'o']]
    new_board = Board(store, state)
    assert new_board.check_column(2) == True

def test_check_column_returns_False_no_winner_yet():
    store = build_store()
    state = [['x', None, 'o'], 
        [None, None, 'o'], 
        ['o', None, 'o']]
    new_board = Board(store, state)
    assert new_board.check_column(1) == False
    
def test_check_all_columns_returns_True_winner_column():
    store = build_store()
    state = [['x', None, 'o'], 
        [None, None, 'o'], 
        ['o', None, 'o']]
    new_board = Board(store, state)
    assert new_board.check_all_columns() == True

def test_check_all_columns_returns_False_no_winner_yet():
    store = build_store()
    state = [['x', None, 'o'], 
        [None, None, 'o'], 
        ['o', None, 'x']]
    new_board = Board(store, state)
    assert new_board.check_all_columns() == False

def test_check_left_diagonal_returns_True_winner_diagonal():
    store = build_store()
    state = [['x', 'x', 'o'], 
    [None, 'x', 'o'], 
    ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_left_diagonal() == True

def test_check_left_diagonal_returns_False_no_winner_yet():
    store = build_store()
    state = [['x', 'x', 'o'], 
        [None, None, 'o'], 
        ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_left_diagonal() == False

def test_check_right_diagonal_returns_True_winner_diagonal():
    store = build_store()
    state = [['x', 'x', 'o'], 
    [None, 'o', 'o'], 
    ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_right_diagonal() == True

def test_check_right_diagonal_returns_False_no_winner_yet():
    store = build_store()
    state = [['x', 'x', 'o'], 
    [None, None, 'o'], 
    ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_right_diagonal() == False

def test_check_winner_returns_True_winner():
    store = build_store()
    state = [['x', 'x', 'o'], 
    [None, 'o', 'o'], 
    ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_winner() == True

def test_check_winner_returns_False_no_winner_yet():
    store = build_store()
    state = [['x', 'x', None], 
    [None, 'o', 'o'], 
    ['o', 'x', 'x']]
    new_board = Board(store, state)
    assert new_board.check_winner() == False


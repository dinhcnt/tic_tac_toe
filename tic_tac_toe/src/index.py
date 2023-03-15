def build_store():
    store = {'users': {},
'games': {}, 'players': {}, 'boards': {}, 'turns': {}, 'squares': {}}
    return store

blank_state = [[None, None, None], 
        [None, None, None], 
        [None, None, None]]

store = build_store()

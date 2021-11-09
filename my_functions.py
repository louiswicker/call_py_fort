def run_function(STATE):
    array = STATE['a'][...]
    print(array.shape)
    STATE['a'][0,:] = STATE['a'][0,:] + 1.0
    print(STATE['a'])

def change_a(STATE):
    return

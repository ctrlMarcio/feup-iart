def bfs(initial_state, functions, objective):
    state = {
        'state': initial_state,
        'parent': False
    }

    return __bfs([state], functions, objective)

def __bfs(states, functions, objective):
    if len(states) == 0:
        return False

    current_state = states.pop(0)
    
    if objective(*(current_state['state'])):
        return __path(current_state)
    
    for f in functions:
        result = f(*(current_state['state']))
        if result != False:
            states.append({'state': result, 'parent': current_state})

    return __bfs(states, functions, objective)

def __path(state):
    res = [state['state']]
    parent = state['parent']

    while parent != False:
        res.insert(0, parent['state'])

        state = parent
        parent = state['parent']

    return res
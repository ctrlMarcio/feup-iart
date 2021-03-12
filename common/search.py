# DISCLAIMER
# DISCLAIMER IN UPPER CASE BECAUSE IM IN CRISIS
# WELL THE SITUATION IS, I COULD DOCUMENT THIS ESPARGUETE BUT FIRST OF ALL I DONT WANT TO
# AND SECOND OF ALL I DONT FEEL LIKE IT, THIS IS A CARBONARA ALREADY AND I DONT WANT TO LOOK
# AT THIS CODE ANYMORE DONT CONTACT ME ABOUT THIS, THANK YOU 🖤

class Node:
    def __init__(self, state, parent=False, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def path(self):
        # bubble up bubble up
        res = [self.state]
        parent = self.parent

        while parent != False:
            res.insert(0, parent.state)

            state = parent
            parent = state.parent

        return res

    def is_root(self):
        return self.parent == False

    def is_repeated(self, depth=6):
        if self.is_root() or depth == 0:
            return False

        return self.parent.__is_repeated(self.state, depth-1)

    def __is_repeated(self, state, depth):
        if self.is_root() or depth == 0:
            return False

        if self.state == state:
            return True

        return self.parent.__is_repeated(state, depth-1)


def bfs(initial_state, functions, objective):
    state = Node(initial_state)

    last_node = __bfs([state], functions, objective)

    if last_node == False:
        return last_node

    return last_node.path()


def __bfs(states, functions, objective):
    if len(states) == 0:
        return False

    current_state = states.pop(0)

    if objective(current_state.state):
        return current_state

    for f in functions:
        result = f(current_state.state)
        if result != False and not current_state.is_repeated():
            states.append(Node(result, current_state, current_state.depth + 1))

    return __bfs(states, functions, objective)


def dfs(initial_state, functions, objective, depth):
    state = Node(initial_state)

    best_node = __dfs([state], functions, objective, False, depth)

    if best_node == False:
        return best_node

    return best_node.path()


def __dfs(states, functions, objective, best_state, depth, stop_on_find=False):
    if len(states) == 0:
        return best_state

    current_state = states.pop(len(states) - 1)  # gets the last state

    if (current_state.depth > depth):
        return __dfs(states, functions, objective, best_state, depth, stop_on_find)

    if objective(current_state.state):
        if stop_on_find:
            return current_state

        depth = current_state.depth
        if best_state == False or depth < best_state.depth:
            best_state = current_state
            depth = current_state.depth

        return __dfs(states, functions, objective, best_state, depth, stop_on_find)

    for f in functions:
        result = f(current_state.state)
        if result != False and not current_state.is_repeated():
            states.append(Node(result, current_state,
                               current_state.depth + 1))

    return __dfs(states, functions, objective, best_state, depth, stop_on_find)


def iterative_dfs(initial_state, functions, objective):
    state = Node(initial_state)

    best_node = False
    depth = 0
    while best_node == False:
        # if problem impossible then not working idc tbh
        best_node = dfs(initial_state, functions, objective, depth)
        depth += 1

    return best_node

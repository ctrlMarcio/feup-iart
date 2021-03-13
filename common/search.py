# DISCLAIMER
# DISCLAIMER IN UPPER CASE BECAUSE IM IN CRISIS
# WELL THE SITUATION IS, I COULD DOCUMENT THIS ESPARGUETE BUT FIRST OF ALL I DONT WANT TO
# AND SECOND OF ALL I DONT FEEL LIKE IT, THIS IS A CARBONARA ALREADY AND I DONT WANT TO LOOK
# AT THIS CODE ANYMORE DONT CONTACT ME ABOUT THIS, THANK YOU 🖤

class Node:
    def __init__(self, state, parent=False, function="start", depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.function = function

    def path(self):
        # bubble up bubble up
        res = [self]
        parent = self.parent

        while parent != False:
            res.insert(0, parent)

            state = parent
            parent = state.parent

        return res

    def path_string(self):
        path = self.path()

        res = ""
        for node in path:
            # calls to_string if the state has it, else just gets the state in raw
            to_string = getattr(node.state, "to_string", None)
            if callable(to_string):
                # TODO update, __str__ instead of to_string
                res += " |\n | " + node.function + "\n v\n" + node.state.to_string()
            else:
                res += " |\n | " + node.function + \
                    "\n v\n" + str(list(node.state)) + "\n"

        res += "\nweight: " + str(len(path) - 1)

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


### SEARCH METHODS ###


def bfs(initial_state, functions, objective):
    state = Node(initial_state)

    last_node = __bfs([state], functions, objective)

    if last_node == False:
        return last_node

    return last_node.path_string()


def dfs(initial_state, functions, objective, depth):
    state = Node(initial_state)

    best_node = __dfs([state], functions, objective, False, depth)

    if best_node == False:
        return best_node

    return best_node.path_string()


def iterative_dfs(initial_state, functions, objective):
    state = Node(initial_state)

    best_node = False
    depth = 0
    while best_node == False:
        # if problem impossible then not working idc tbh
        best_node = dfs(initial_state, functions, objective, depth)
        depth += 1

    return best_node


def a_star(initial_state, functions, objective, heuristic):
    state = Node(initial_state)

    last_node = __a_star([state], functions, objective, heuristic)

    if last_node == False:
        return last_node

    return last_node.path_string()

 ### HELPER FUNCTIONS ###


def __bfs(states, functions, objective):
    if len(states) == 0:
        return False

    current_state = states.pop(0)

    if objective(current_state.state):
        return current_state

    for f in functions:
        result = f(current_state.state)
        if result != False and not current_state.is_repeated():
            states.append(Node(result, current_state,
                               f.__name__, current_state.depth + 1))

    return __bfs(states, functions, objective)


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
                               f.__name__, current_state.depth + 1))

    return __dfs(states, functions, objective, best_state, depth, stop_on_find)


def __a_star(states, functions, objective, heuristic):
    if len(states) == 0:
        return False

    states = sorted(states, key=lambda node: heuristic(node.state))
    current_state = states.pop(0)

    if objective(current_state.state):
        return current_state

    for f in functions:
        result = f(current_state.state)
        if result != False and not current_state.is_repeated():
            node = Node(result, current_state,
                               f.__name__, current_state.depth + 1)
            states.append(node)
            

    return __a_star(states, functions, objective, heuristic)

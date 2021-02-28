# %%
# Starting

c1, c2 = (4, 3)
n = 2
initial_state = (0, 0)

def fill1(w1, w2):
    if w1 >= c1:
        return False

    w1 = c1
    return (w1, w2)


def fill2(w1, w2):
    if w2 >= c2:
        return False

    w2 = c2
    return (w1, w2)


def empty1(w1, w2):
    if w1 == 0:
        return False

    w1 = 0
    return (w1, w2)


def empty2(w1, w2):
    if w2 == 0:
        return False

    w2 = 0
    return (w1, w2)


def fill2from1(w1, w2):
    if w1 == 0 or c2 - w2 > w1:
        return False

    w1 = w1 - (c2 - w2)
    w2 = c2
    return (w1, w2)


def fill1from2(w1, w2):
    if w2 == 0 or c1 - w1 > w1:
        return False

    w2 = w2 - (c1 - w1)
    w1 = c1
    return (w1, w2)


def empty1to2(w1, w2):
    if w1 == 0 or c2 - w2 < w1:
        return False

    w2 = w2 + w1
    w1 = 0
    return (w1, w2)


def empty2to1(w1, w2):
    if w2 == 0 or c1 - w1 < w2:
        return False

    w1 = w1 + w2
    w2 = 0
    return (w1, w2)


def objective(w1, w2):
    return w1 == n


# %%
# Breadth first search
from common import bfs

functions = [fill1, fill2, empty1, empty2, fill2from1, fill1from2, empty1to2, empty2to1]
res = bfs(initial_state, functions, objective)
print(res)


# %%

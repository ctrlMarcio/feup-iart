from common import dfs
from common import bfs
import sys

# initial state
sm = 3
sc = 3
initial_state = (sm, sc, 1)

# operators definition


def mm2(nm, nc, nb):
    if nm < 2 or (nc > nm - 2 and nm - 2 > 0) or nb != 1:
        return False

    nm -= 2
    nb = 0
    return (nm, nc, nb)


def m2(nm, nc, nb):
    if nm < 1 or (nc > nm - 1 and nm - 1 > 0) or nb != 1:
        return False

    nm -= 1
    nb = 0
    return (nm, nc, nb)


def mc2(nm, nc, nb):
    if nm < 1 or nc < 1 or nb != 1:
        return False

    nm -= 1
    nc -= 1
    nb = 0
    return (nm, nc, nb)


def cc2(nm, nc, nb):
    if nc < 2 or (sm - nm < sc - nc + 2 and sm - nm > 0) or nb != 1:
        return False

    nc -= 2
    nb = 0
    return (nm, nc, nb)


def c2(nm, nc, nb):
    if nc < 1 or (sm - nm < sc - nc + 1 and sm - nm > 0) or nb != 1:
        return False

    nc -= 1
    nb = 0
    return (nm, nc, nb)


def mm1(nm, nc, nb):
    if sm - nm < 2 or (sc - nc > sm - nm - 2 and sm - nm - 2 > 0) or nb != 0:
        return False

    nm += 2
    nb = 1
    return (nm, nc, nb)


def m1(nm, nc, nb):
    if sm - nm < 1 or (sc - nc > sm - nm - 1 and sm - nm - 1 > 0) or nb != 0:
        return False

    nm += 1
    nb = 1
    return (nm, nc, nb)


def mc1(nm, nc, nb):
    if sm - nm < 1 or sc - nc < 1 or nb != 0:
        return False

    nm += 1
    nc += 1
    nb = 1
    return (nm, nc, nb)


def cc1(nm, nc, nb):
    if sc - nc < 2 or (nm < nc + 2 and nm > 0) or nb != 0:
        return False

    nc += 2
    nb = 1
    return (nm, nc, nb)


def c1(nm, nc, nb):
    if sc - nc < 1 or (nm < nc + 1 and nm > 0) or nb != 0:
        return False

    nc += 1
    nb = 1
    return (nm, nc, nb)

# Objective


def objective(nm, nc, nb):
    return nm == 0 and nc == 0


functions = [mm2, m2, mc2, cc2, c2, mm1, m1, mc1, cc1, c1]


sys.setrecursionlimit(10**6)

res = dfs(initial_state, functions, objective, 10)
print(res)

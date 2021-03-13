# operators
import time
import copy
import sys
from copy import copy, deepcopy
from search import bfs, a_star


class NPuzzleState:
    def __init__(self, board):
        self.board = [row[:] for row in board]
        (self.empty_x, self.empty_y) = NPuzzleState.empty_square(self.board)
        self.board_side = len(self.board)

    # gets the (x, y) of the empty square
    @staticmethod
    def empty_square(board):
        for y, line in enumerate(board):
            for x, element in enumerate(line):
                if element == 0:
                    return (x, y)

        return False

    def to_string(self):
        res = ""

        for list in self.board:
            for element in list:
                res += str(element) + " "
            res += "\n"

        return res

    def __eq__(self, other):
        if not isinstance(other, NPuzzleState):
            return False
        return self.board == other.board


def up(state):
    if state.empty_y <= 0:
        return False

    new_state = NPuzzleState(state.board)
    new_state.board[new_state.empty_y][new_state.empty_x] = new_state.board[new_state.empty_y - 1][new_state.empty_x]
    new_state.board[new_state.empty_y - 1][new_state.empty_x] = 0
    new_state.empty_y -= 1
    return new_state


def down(state):
    if state.empty_y >= state.board_side - 1:
        return False

    new_state = NPuzzleState(state.board)
    new_state.board[new_state.empty_y][new_state.empty_x] = new_state.board[new_state.empty_y + 1][new_state.empty_x]
    new_state.board[new_state.empty_y + 1][new_state.empty_x] = 0
    new_state.empty_y += 1
    return new_state


def left(state):
    if state.empty_x <= 0:
        return False

    new_state = NPuzzleState(state.board)

    new_state.board[new_state.empty_y][new_state.empty_x] = new_state.board[new_state.empty_y][new_state.empty_x - 1]
    new_state.board[new_state.empty_y][new_state.empty_x - 1] = 0
    new_state.empty_x -= 1
    return new_state


def right(state):
    if state.empty_x >= state.board_side - 1:
        return False

    new_state = NPuzzleState(state.board)

    new_state.board[new_state.empty_y][new_state.empty_x] = new_state.board[new_state.empty_y][new_state.empty_x + 1]
    new_state.board[new_state.empty_y][new_state.empty_x + 1] = 0
    new_state.empty_x += 1
    return new_state


functions = [up, down, left, right]


def h1(state):
    res = 0
    for i in range(state.board_side):
        for j in range(state.board_side):
            if state.board[i][j] != 0 or state.board[i][j] != i*state.board_side + j + 1:
                res += 1

    return res


def h2(state):
    res = 0
    for i in range(state.board_side):
        for j in range(state.board_side):
            if state.board[i][j] != 0 and state.board[i][j] != i*state.board_side + j + 1:
                res += abs(i - (state.board[i][j] - 1) // state.board_side) + \
                    abs(j - (state.board[i][j] - 1) % state.board_side)

    return res


def objective(state):
    flat_list = []
    for sublist in state.board:
        for item in sublist:
            flat_list.append(item)

    return (all(i < j for i, j in zip(flat_list[:len(flat_list) - 2], flat_list[1:len(flat_list) - 1]))) and flat_list[0] == 1


start = time.process_time()
initial_state = NPuzzleState([[5, 1, 3, 4],
                              [2, 0, 7, 8],
                              [10, 6, 11, 12],
                              [9, 13, 14, 15]])
res = a_star(initial_state, functions, objective, h2)
time4 = time.process_time() - start
print(res)
print(time4)

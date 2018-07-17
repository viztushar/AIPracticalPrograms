import numpy as np
from collections import deque

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def up(state):
    """move blank space up on the board and return new state."""
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 1, 2]:
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def down(state):
    """move blank space down on the board and return new state."""
    new_state = state[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def left(state):
    """move blank space left on the board and return new state"""
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def right(state):
    """move blank space right on the board and return new state."""
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def bfs(prob_state, goal_state):
    iterations = 0
    visited = set()
    queue = deque(prob_state)



afterup = up(goal_state)

afterleft = left(afterup)
print(np.array(afterleft).reshape(3, 3))

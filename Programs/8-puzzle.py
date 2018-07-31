import numpy as np
from collections import deque

goal_state = [1, 2, 3, 4, 5, 7, 6, 8, 0]


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
    visited = []
    q = [(prob_state, [])]
    while q:
        current = tuple(q.pop(0))
        current[1].append(current[0])
        if current[0] == goal_state:
            print(np.array(current[1]))
            print(len(current[1]))
            break
        if (left(list(current[0])) is not None) and (current[0] not in visited):
            t = tuple((left(list(current[0])), list(current[1])))
            q.append(t)
        if (right(list(current[0])) is not None) and (current[0] not in visited):
            t = tuple((right(list(current[0])), list(current[1])))
            q.append(t)
        if (up(list(current[0])) is not None) and (current[0] not in visited):
            t = tuple((up(list(current[0])), list(current[1])))
            q.append(t)
        if (down(list(current[0])) is not None) and (current[0] not in visited):
            t = tuple((down(list(current[0])), list(current[1])))
            q.append(t)
        if current[0] not in visited:
            visited.append(current[0])


afterup = [1, 2, 3, 0, 4, 5, 6, 7, 8]
print(np.array(goal_state).reshape(3,3))
bfs(afterup, goal_state)

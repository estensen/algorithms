from queue import Queue
from a_star import Node

__author__ = 'estensen'


def bfs(board, start, goal):
    """Return open nodes, closed nodes and path"""
    _node_cost = {
        'w': 100,
        'm': 50,
        'f': 10,
        'g': 5,
        'r': 1,
        '.': 1,
        'A': 1,
        'B': 1
    }
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    explored_coordinates = set()

    # Board x size
    board_x = len(board[0])
    # Board y size
    board_y = len(board)

    start = Node(start[1], start[0])
    goal = Node(goal[1], goal[0])

    visited = set()
    queue = Queue()
    queue.put(start)

    no_children = 0

    while queue:
        current = queue.get()
        visited.add(current)

        if current.x == goal.x and current.y == goal.y:
            return list(queue.queue), visited, current.retrace_path()

        for n in neighbors:
            child_x = current.x + n[0]
            child_y = current.y + n[1]
            # Outside board
            if child_x >= board_x or child_y >= board_y or child_x < 0 or child_y < 0:
                continue
            # Not a wall
            if board[child_y][child_x] != '#':
                no_children += 1
                current.add_child(Node(child_x, child_y))

        for child in current.children:
            if (child.x, child.y) not in explored_coordinates:
                explored_coordinates.add((child.x, child.y))

                child.parent = current
                queue.put(child)
    return None

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Cost of getting to this node
        self.g = 0
        # Estimated cost to goal
        self.h = 0
        self.parent = None
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def generate_children(self):
        pass

    def retrace_path(self):
        current, path = self, []
        while current.parent:
            path.append(current)
            current = current.parent
        # When no parent add self
        path.append(current)
        path.reverse()
        return path

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y


def manhattan(node1, goal):
    return abs(node1.x - goal.x) + abs(node1.y - goal.y)


def a_star(board, start, goal):
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
    # Board x size
    board_x = len(board[0])
    # Board y size
    board_y = len(board)
    # Explored coordinates
    explored_coordinate = set()
    explored_coordinate.add((start[1], start[0]))
    # The set of nodes already evaluated
    closed_set = set()
    # The set of currently discovered nodes still to be evaluated
    open_set = set()
    # Make A and B nodes
    start = Node(start[1], start[0])
    goal = Node(goal[1], goal[0])
    # Add start node
    open_set.add(start)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while open_set:
        current = min(open_set, key=lambda o: o.g + o.h)
        if current.x == goal.x and current.y == goal.y:
            return open_set, closed_set, current.retrace_path()
        # Generate children
        for n in neighbors:
            # Give the neighbors coordinates
            child_x = current.x + n[0]
            child_y = current.y + n[1]
            # Outside board
            if child_x >= board_x or child_y >= board_y or child_x < 0 or child_y < 0:
                continue
            # Not a wall
            if board[child_y][child_x] != '#':
                current.add_child(Node(child_x, child_y))

        open_set.remove(current)
        closed_set.add(current)

        for child in current.children:
            # Calculate new node distances
            if (child.x, child.y) not in explored_coordinate:
                explored_coordinate.add((child.x, child.y))
                child.parent = current
                child.g = current.g + _node_cost[board[child.y][child.x]]
                child.h = manhattan(child, goal)
                open_set.add(child)
            elif current.g + _node_cost[board[child.y][child.x]] < child.g:
                child.parent = current
                child.g = current.g + _node_cost[board[child.y][child.x]]
                child.h = manhattan(child, goal)
                open_set.add(child)
    return None

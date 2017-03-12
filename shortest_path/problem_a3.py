from a_star import a_star
from bfs import bfs
from dijkstra import dijkstra

__author__ = 'estensen'

'''
Find paths with
- A*
- BFS
- Dijkstra's algorithm

Visualize boards with open and closed_set nodes

Give brief analysis of differences in paths and number of open and closed_set nodes
'''


def solve(file, algo):
    # Read board
    with open(file) as f:
        board = [list(line.rstrip()) for line in f]

    # Find start and goal for board
    def find_char_on_board(char, board):
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == char:
                    return y, x


    # Make start and goal nodes
    start = find_char_on_board('A', board)
    goal = find_char_on_board('B', board)

    # Solve board
    open_set = None
    closed_set = None
    if algo == "astar":
        open_set, closed_set, path = a_star(board, start, goal)
    elif algo == "bfs":
        open_set, closed_set, path = bfs(board, start, goal)
    elif algo == "dijkstra":
        open_set, closed_set, path = dijkstra(board, start, goal)

    # Print board after solving
    if path:
        if closed_set:
            for o in closed_set:
                if board[o.y][o.x] != 'B' and board[o.y][o.x] != 'A':
                    board[o.y][o.x] = 'x'
        if open_set:
            for p in open_set:
                if board[p.y][p.x] != 'B':
                    board[p.y][p.x] = '*'
        for n in path[1:-1]:
            board[n.y][n.x] = 'o'

    for line in board:
        print("".join(line))
    print()

# A*
solve("boards/board-1-1.txt", "astar")
solve("boards/board-1-2.txt", "astar")
solve("boards/board-1-3.txt", "astar")
solve("boards/board-1-4.txt", "astar")
solve("boards/board-2-1.txt", "astar")
solve("boards/board-2-2.txt", "astar")
solve("boards/board-2-3.txt", "astar")
solve("boards/board-2-4.txt", "astar")


# BFS

solve("boards/board-1-1.txt", "bfs")
solve("boards/board-1-2.txt", "bfs")
solve("boards/board-1-3.txt", "bfs")
solve("boards/board-1-4.txt", "bfs")
solve("boards/board-2-1.txt", "bfs")
solve("boards/board-2-2.txt", "bfs")
solve("boards/board-2-3.txt", "bfs")
solve("boards/board-2-4.txt", "bfs")

# Dijkstra
solve("boards/board-1-1.txt", "dijkstra")
solve("boards/board-1-2.txt", "dijkstra")
solve("boards/board-1-3.txt", "dijkstra")
solve("boards/board-1-4.txt", "dijkstra")
solve("boards/board-2-1.txt", "dijkstra")
solve("boards/board-2-2.txt", "dijkstra")
solve("boards/board-2-3.txt", "dijkstra")
solve("boards/board-2-4.txt", "dijkstra")

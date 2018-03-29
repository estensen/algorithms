from a_star import a_star


def solve(file):
    # Read board
    with open(file) as f:
        board = [list(line.rstrip()) for line in f]

    # Print board before solving
    #for line in board:
    #    print(line)


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
    a, b, shortest_path = a_star(board, start, goal)

    # Print board after solving
    if shortest_path:
        print("Path found for " + file)
        for n in shortest_path[1:-1]:
            board[n.y][n.x] = 'o'

    for line in board:
        print("".join(line))
    print()

solve('boards/board-1-1.txt')
solve('boards/board-1-2.txt')
solve('boards/board-1-3.txt')
solve('boards/board-1-4.txt')
solve('boards/board-2-1.txt')
solve('boards/board-2-2.txt')
solve('boards/board-2-3.txt')
solve('boards/board-2-4.txt')
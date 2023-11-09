import numpy as np
import copy

def is_safe(board, x, y):
    N = len(board)

    for i in range(x):
        if board[i][y] == 1:
            return False

    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(x, -1, -1), range(y, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nQueen():
    n, x, y = map(int, input().split())

    board = [[0] * n for _ in range(n)]
    board[x][y] = 1

    result = [[] for _ in range(n)]
    result[x].append(copy.deepcopy(board))

    target_x = copy.deepcopy(x)

    for i in range(n - 1):
        target_x = (target_x + 1) % n
        new_boards = []

        for prev_board in result[target_x - 1]:
            for y_point in range(n):
                if prev_board[target_x][y_point] == 1:
                    continue
                if is_safe(prev_board, target_x, y_point):
                    new_board = copy.deepcopy(prev_board)
                    new_board[target_x][y_point] = 1
                    new_boards.append(new_board)


        result[target_x] = new_boards
        
    if len(result[-1]) > 0:
        print('YES({})'.format(len(result[-1])))
    else:
        print('NO')

while True:
    try:
        solve_nQueen()
    except:
        break

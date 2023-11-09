import copy

def is_safe(board, point_row, point_col):
    
    N = len(board)
    
    for i in range(N):
        if board[i][point_col] == 1 or board[point_row][i] == 1:
            return False

    # 所有的可行步
    for i in range(1, N):
        if (point_row - i >= 0 and point_col - i >= 0 and board[point_row - i][point_col - i] == 1) or \
           (point_row - i >= 0 and point_col + i < N and board[point_row - i][point_col + i] == 1) or \
           (point_row + i < N and point_col - i >= 0 and board[point_row + i][point_col - i] == 1) or \
           (point_row + i < N and point_col + i < N and board[point_row + i][point_col + i] == 1):
            return False

    return True

def solve_nQueen():
    n, row, col = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[row][col] = 1

    result = [[] for _ in range(n)]
    result[row].append(copy.deepcopy(board))

    target_row = row

    for i in range(n - 1):
        target_row = (target_row + 1) % n
        for new_board in result[target_row - 1]:
            for col_point in range(n):
                if new_board[target_row][col_point] == 0 and is_safe(new_board, target_row, col_point):
                    new_board[target_row][col_point] = 1
                    result[target_row].append(copy.deepcopy(new_board))
                    new_board[target_row][col_point] = 0

    if len(result[-1]) != 0:
        print('YES({})'.format(len(result[-1])))
    else:
        print('NO')

while True:
    try:
        solve_nQueen()
    except:
        break

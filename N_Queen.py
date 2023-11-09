import copy

def is_safe(board, x, y):
    N = len(board)
    # 檢查垂直方向
    for r in range(x):
        if board[r][y] == 1:
            return False

    # 檢查左上到右下的對角線
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    # 檢查右上到左下的對角線
    for i, j in zip(range(x, -1, -1), range(y, N)):
        if board[i][j] == 1:
            return False

    return True

def place_queen(board, x, n, solutions):
    if x == n:
        # 找到一個解決方案
        solutions.append(copy.deepcopy(board))
        return

    for y in range(n):
        if is_safe(board, x, y):
            board[x][y] = 1
            place_queen(board, x + 1, n, solutions)
            board[x][y] = 0

def solve_nQueen(n, x, y):
    # 初始化棋盤
    board = [[0] * n for _ in range(n)]
    board[x][y] = 1

    solutions = []
    place_queen(board, 0, n, solutions)

    if len(solutions) > 0:
        print('YES({})'.format(len(solutions)))
    else:
        print('NO')

while True:
    try:
        # 請確保在這裡設定適當的 n、x 和 y 值，或者根據需要接收使用者輸入
        n, x, y = map(int, input().split())
        solve_nQueen(n, x, y)
    except Exception as e:
        break

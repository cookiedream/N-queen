def is_safe(board, row, col):
    # 檢查列上是否有皇后
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 檢查左上對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 檢查右上對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            # 找到一個解，將其加入結果中
            solutions.append([''.join(['Q' if c == 1 else '.' for c in row]) for row in board])
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

N, row, col = map(int, input().split())
solutions = solve_n_queens(N)
result = 0

for solution in solutions:
    if solution[row].count('Q') == 1 and solution[row][col] == 'Q':
        result += 1

if result == 0:
    print('NO')
else:
    print('YES({})'.format(result))

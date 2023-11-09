def solveNQueens(n):
    def is_safe(board, row, col):
        # 檢查列中是否有皇后
        for i in range(col):
            if board[row][i] == 1:
                return False

        # 檢查左上至右下對角線上是否有皇后
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # 檢查左下至右上對角線上是否有皇后
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(row):
        if row == n:
            # 找到一個解，將其加入結果
            solutions.append(["".join(["Q" if x == 1 else "." for x in row]) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve(0)
    return solutions

# 測試
n = 4  # 4-Queens問題的解
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()


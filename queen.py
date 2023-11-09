# import numpy as np
import copy

#在board[row][col]中插入皇后[2]，並使其攻擊範圍為[1]
# def Add_Queen(board1, row, col):
#         n=len(board1)
#         board1[row][col]=2

#         # 檢查row中是否有皇后
#         for i in range(1,n):
#             board1[row][col-i] = 1

#         #檢查col中是否有皇后
#         for i in range(1,n):
#             board1[row-i][col]=1

#         # 檢查左上對角線上是否有皇后
#         for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
#             board1[i][j] = 1

#         #檢查右下對角線上是否有皇后
#         for i, j in zip(range(row+1, n, 1), range(col+1, n, 11)):
#             board1[i][j] = 1

#         # 檢查左對角線上是否有皇后
#         for i, j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
#             board1[i][j] = 1

#         #檢查右上對角線上是否有皇后
#         for i, j in zip(range(row-1, -1, -1), range(col+1, n, 1)):
#             board1[i][j] = 1        
        
#         return board1

# 定義一個函數，用來檢查在特定位置放置皇后是否安全
def is_safe(board, x, y):
    N = len(board)

    # # 檢查垂直方向是否有皇后
    # for i in range(x):
    #     if board[i][y] == 1:
    #         return False
    # # 檢查水平方向是否有皇后
    # for i in range(y):
    #     if board[x][i] == 1:
    #         return False

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == y or j == x:
                    return False
                if abs(x - j) == abs(y - i):
                    return False
    return True
    # # 檢查左上到右下的對角線是否有皇后
    # for i, j in zip(range(x+N, -1, -1), range(y+N, -1, -1)):
    #     if i < 0 or j < 0:
    #         continue
    #     if board[i][j] == 1:
    #         return False

    # # # 檢查右上到左下的對角線是否有皇后
    # for i, j in zip(range(x+N, -1, -1), range(y+N, N)):
    #     if board[i][j] == 1:
    #         return False

    # return True

# def place_queen(board, x, N, solutions):
#     if x == n:
#         # 找到一個解決方案
#         solutions.append(copy.deepcopy(board))
#         return

#     for y in range(n):
#         if is_safe(board, x, y):
#             board[x][y] = 1
#             place_queen(board, x + 1, n, solutions)
#             board[x][y] = 0

# 主函數，用來解決N皇后問題
def solve_nQueen():
    
    # 讀取輸入，包括棋盤大小（n）、初始皇后位置（x、y）
    N, x, y = map(int, input().split())

    # 創建一個N×N的棋盤，並將初始皇后放在指定位置
    board = [[0] * N for i in range(N)]
    board[x][y] = 1

    # # 創建一個用來保存解的列表
    # result = [[] for i in range(N)]
    # result[x].append(copy.deepcopy(board))

    # # 初始目標行
    # target_x = copy.deepcopy(x)
        
    # # 開始迭代，一行一行地擺放皇后
    # for i in range(N - 1):
    #     target_x = (target_x + 1) % N
    #     new_boards = []
    #     # print(y_point)
    #     # 對上一行的每個解，嘗試在當前行擺放皇后
    #     for prev_board in result[target_x - 1]:
    #         for y_point in range(N):
    #             if prev_board[target_x][y_point] == 1:
    #                 continue
    #             if is_safe(prev_board, target_x, y_point):
    #                 new_board = copy.deepcopy(prev_board)
    #                 new_board[target_x][y_point] = 1
    #                 new_boards.append(new_board)
    #             else:
    #                 continue  # 如果不符合is_safe規則，則跳過當前的y_point

    #     # 保存當前行的新解
    #     result[target_x] = new_boards

    # print(result[-1])

# def DFS(a):
#     if check(a):
#         return  # 该return仅结束其中一次循环，变相有很多循环在执行
#     for i in range(1, n + 1):
#         x[a] = i  # 即第a个皇后放置在第i列
#         if judge(a):  # 判断是否可以放置在该处
#             DFS(a + 1)
#         else:
#             continue  # 即使第i列不可以，continue之后，x[a]的值也会改变，不影响后续


    # 如果最後一行有解，顯示"YES"以及解的數量，否則顯示"NO"
    if len(result[-1]) > 0:
        print('YES({})'.format(len(result[-1])))
    else:
        print('NO')

# 不斷執行主函數，直到發生異常（通常是輸入結束）
while True:
    try:
        solve_nQueen()
    except:
        break

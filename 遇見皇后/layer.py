import numpy as np
import copy

def slanting(board, x, y, dir):
    # 计算皇后走斜的路径
    if dir == 'RU':
        # 右上
        while True:
            try:
                x -= 1
                y += 1
                if x < 0:
                    break
                board[x][y] = 1
            except IndexError:
                break
    # ... 其他方向的代码 ...

def Queen(board, x, y):
    # 不能放皇后的点为1
    # 皇后所在位置为2
    board[x][y] = 2

    # 水平方向
    for i in range(1, size):
        point = x + i
        if point >= size:
            point = point - size
        board[point][y] = 1
    # ... 其他方向的代码 ...

def point(size, board):
    # 找可以放皇后的位置
    points = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                points.append([i, j])
    return points

def count(size, board):
    # 计算有几个皇后
    counts = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 2:
                counts += 1
    return counts

def main(size, board, result, level=0):
    # 打印当前层级
    print(f"Level {level}: {board}")

    # 把所有可放的点找出来
    points = point(size, board)

    # 若满皇后将board加入result
    if count(size, board) == size:
        result.append(board)
        return
    else:
        for i in points:
            x = i[0]
            y = i[1]
            # 额外再要一个记忆体将board存起来
            new_board = Queen(copy.deepcopy(board), x, y)
            main(size, new_board, result, level + 1)

size = 4
x = 0
y = 1
board = [[0] * size for _ in range(size)]
board = Queen(board, x, y)
result = []
main(size, board, result)

result = set(tuple(tuple(row) for row in matrix) for matrix in result)

total = len(result)
if total != 0:
    print('YES({})'.format(total))
else:
    print('NO')

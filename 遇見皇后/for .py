import numpy as np
import copy

#在board[row][col]中插入皇后[2]，並使其攻擊範圍為[1]
def Add_Queen(board1, row, col):
        n=len(board1)
        board1[row][col]=2

        # 檢查row中是否有皇后
        for i in range(1,n):
            board1[row][col-i] = 1

        #檢查col中是否有皇后
        for i in range(1,n):
            board1[row-i][col]=1

        # 檢查左上對角線上是否有皇后
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            board1[i][j] = 1

        #檢查右下對角線上是否有皇后
        for i, j in zip(range(row+1, n, 1), range(col+1, n, 11)):
            board1[i][j] = 1

        # 檢查左對角線上是否有皇后
        for i, j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
            board1[i][j] = 1

        #檢查右上對角線上是否有皇后
        for i, j in zip(range(row-1, -1, -1), range(col+1, n, 1)):
            board1[i][j] = 1        
        
        return board1

#找出在board中所有仍可放置皇后的點
def find_points(board2):
    N=len(board2)
    points=[]
    for row in range(N):
        for col in range(N):
            if board2[row][col]==0:
                points.append([row,col])
    return points

#計算在board中皇后的數量，若其數量為len(board)則返回True 反之則返回False
def count_Queen(board3):
    N=len(board3)
    count=0
    for row in range(N):
        for col in range(N):
            if board3[row][col]==2:
                count+=1

    if count==N:
        return True
    else:
        return False

def main(board,result):
    if count_Queen(board):
        if board not in result:
            result.append(board)
            return

    points=find_points(board)

    for point in points:
        row=point[0]
        col=point[1]
        new_board=Add_Queen(copy.deepcopy(board),row,col)
        main(new_board,result)

while True:
    try:
        n,row,col=map(int,input().split())
        board=[[0]*n for _ in range(n)]
        result=[]
        board=Add_Queen(board,row,col)
        main(board,result)
        long=len(result)

        if long==0:
            print('NO')
        else:
            print('YES({})'.format(long))
    except:
        break

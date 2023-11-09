import numpy as np
import copy

def is_safe(board,point_row,point_col):
    N=len(board)
    #垂直
    for row in range(1,N):
        if board[point_row-row][point_col]==1:
            return False
        
    #水平
    for col in range(1,N):
        if board[point_row][point_col-col]==1:
            return False
        
    #RU
    for i in range(1,min(1+point_row,N-point_col)):
        if board[point_row-i][point_col+i]==1:
            return False
        
    #RD
    for i in range(1,min(N-point_row,N-point_col)):
        if board[point_row+i][point_col+i]==1:
            return False
        
    #LU
    for i in range(1,min(1+point_row,1+point_col)):
        if board[point_row-i][point_col-i]==1:
            return False
        
    #LD
    for i in range(1,min(N-point_row,1+point_col)):
        if board[point_row+i][point_col-i]==1:
            return False

    return True

def row_subset(target_row,board1,n,result1,row):

    for col_point in range(n): 
        if board1[target_row][col_point]==1:
            continue
        if is_safe(board1,target_row,col_point):
            board1[target_row][col_point]=1
            result1[target_row].append(copy.deepcopy(board1))
            board1[target_row][col_point]=0

def solve_nQueen():
    #初始盤面    
    n,row,col=map(int,input().split())
    board=[[0]*n for _ in range(n)]
    board[row][col]=1

    result=[[] for _ in range(n)]
    result[row].append(board)

    target_row=copy.deepcopy(row)


    for i in range(n-1):
        target_row=target_row+1
        if target_row>=n:
            target_row=target_row-n
        for new_board in result[target_row-1]:
            row_subset(target_row,new_board,n,result,row)
            # if row_subset(target_row,new_board,n,result,init_board,row):
            #     print('NO')
            #     break

    # for i in range(len(result)):
    #     print(result[i])

    if len(result[row-1])!=0:
        print('YES({})'.format(len(result[-1])))
    elif result[row-1] ==[]:
        print('NO')

while True:
    try:
        solve_nQueen()
    except:
        break
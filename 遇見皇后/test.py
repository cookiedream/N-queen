import numpy as np
import copy

def slanting(board,x,y,dir):
            #計算皇后走斜的的路徑
            if dir=='RU':
                #右上
                while True:
                    try:
                        x-=1
                        y+=1
                        if x<0:
                            break
                        board[x][y]=1
                    except IndexError:
                        break
            elif dir=='RD':
                #右下
                while True:
                    try:
                        x+=1
                        y+=1
                        board[x][y]=1
                    except IndexError:
                        break
            elif dir=='LU':
                #左上
                while True:
                    try:
                        x-=1
                        y-=1
                        if x<0 or y<0:
                            break
                        board[x][y]=1
                    except IndexError:
                        break
            elif dir=='LD':
                #左下
                while True:
                    try:
                        x+=1
                        y-=1
                        if y<0:
                            break
                        board[x][y]=1
                    except IndexError:
                        break

def AddQueen(board,x,y):
            #不能放皇后的點為1
            #皇后所在位置為2
            board[x][y]=2
            size=len(board)

            #水平方向
            for i in range(1,size):
                point=x+i
                if point>=size:
                    point=point-size
                board[point][y]=1
            #垂直方向
            for i in range(1,size):
                point=y+i
                if point>=size:
                    point=point-size
                board[x][point]=1
            #斜的
            dir=['RU','RD','LU','LD']
            for i in dir:
                slanting(board,x,y,i)
            return board

def All_points(board):
     N=len(board)
     points=[]
     for i in range(N):
          for j in range(N):
               if board[i][j]==0:
                    points.append([i,j])
     return points

def count(board):
     N=len(board)
     time=0
     for i in range(N):
          for j in range(N):
               if board[i][j]==2:
                    time+=1
     if time==4:
          return True
     else:
          return False

def NQueen(board,result):
    
    if count(board):
         result.append(board)

    points=All_points(board)

    for i in points:
        x=i[0]
        y=i[1]
        new_board=AddQueen(copy.deepcopy(board),x,y)
        NQueen(new_board,result)

    return result
          
# y=0
# x=1
# n,x,y=map(int(),input().split())
# board=[[[0]*n for _ in range(n) ]]
# AddQueen(board,x,y)
# result=[]
# path=[]
# NQueen(board,result)

# for i in result:
#      print(np.array(i))
#      print('')

while True:
     try:
        N=[int(i) for i in input().split()]
        size,x,y=N[0],N[1],N[2]
        board=[[0]*size for _ in range(size)]
        board=AddQueen(board,x,y)
        result=[]
        NQueen(board,result)

        total=set(tuple(tuple(row) for row in matrix) for matrix in result)

        total=len(total)
        if total!=0:
            print('YES({})'.format(total))
        else:
            print('NO')
     except:
        break
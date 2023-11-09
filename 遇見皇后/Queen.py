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

def Queen(board,x,y):
            #不能放皇后的點為1
            #皇后所在位置為2
            board[x][y]=2

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

def point(size,board):
            #找可以放皇后的位置
            points=[]
            for i in range(size):
                for j in range(size):
                    if board[i][j]==0:
                        points.append([i,j])
            return points

def count(size,board):
            #計算有幾個皇后
            counts=0
            for i in range(size):
                for j in range(size):
                    if board[i][j]==2:
                        counts+=1
            return counts   

def main(size,board,result):
            #把所有可放的點找出來
            points=point(size,board)
            # print(points)
            
            #若滿皇后將board加入result
            if count(size,board)==size:
                result.append(board)
                return
            else:
                for i in points:
                    x=i[0]
                    y=i[1]
                    #額外再要一個記憶體將board存起來
                    new_board=copy.deepcopy(board)
                    new_board=Queen(new_board,x,y)

                    # print(x,y)
                    # print(np.array(new_board))

                    main(size,new_board,result)

                    new_board=copy.deepcopy(board)

# size,x,y=4,0,1
# board=[[0]*size for _ in range(size)]
# board=Queen(board,x,y)
# result=[]
# main(size,board,result)

# total=set(tuple(tuple(row) for row in matrix) for matrix in result)

# total=len(total)
# if total!=0:
#     print('YES({})'.format(total))
# else:
#     print('NO')

while True:
     try:
        N=[int(i) for i in input().split()]
        size,x,y=N[0],N[1],N[2]
        board=[[0]*size for _ in range(size)]
        board=Queen(board,x,y)
        result=[]
        main(size,board,result)

        total=set(tuple(tuple(row) for row in matrix) for matrix in result)

        total=len(total)
        if total!=0:
            print('YES({})'.format(total))
        else:
            print('NO')
     except:
        break
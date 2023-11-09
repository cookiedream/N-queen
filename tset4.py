import copy

def place(t):
    for i in range(1,t):
        if t-i==abs(x[t]-x[i]):
            return False
    return True

def dfs(t):
    global ans
    if t>N:
        ans.append(copy.deepcopy(x))

    else:
        for i in range(t,N+1):
            x[t],x[i]=x[i],x[t]
            if place(t):dfs(t+1)
            x[t],x[i]=x[i],x[t]

N,row,col=map(int,input().split())
x=[i for i in range(N+1)]
ans=[]
result=0
dfs(1)

for i in ans:
    if i[row+1]==col+1:
        result+=1

if result==0:
    print('NO')
else:
    print('YES({})'.format(result))
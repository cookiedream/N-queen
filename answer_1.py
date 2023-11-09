def can_place_q(k):
    for i in range(k):
        # 檢查是否有其他皇后在同一列或對角線上
        if queen[i] == queen[k] or abs(k - i) == abs(queen[i] - queen[k]):
            return False
    return True

def dfs(k):
    for j in range(n):
        if k == x:
            queen[k] = y
            j = n
        else:
            queen[k] = j
        if k == n - 1 and can_place_q(k):
            ans[0] += 1
            return
        elif can_place_q(k):
            dfs(k + 1)

while True:
    n, x, y = map(int, input().split())
    queen = [0] * 10
    ans = [0]
    dfs(0)
    if ans[0] > 0:
        print(f"YES ({ans[0]})")
    else:
        print("NO")

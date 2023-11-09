#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int queen[10]; // 皇后的放置位置，最多10個皇后
int n, x, y, ans; // n是棋盤大小，x和y是額外放置的皇后的位置，ans是答案的計數

// 檢查是否可以放置皇后在第k行
bool canPlaceQ(int k) {
    for(int i = 0; i < k; ++i) {
        // 檢查是否有其他皇后在同一列或對角線上
        if(queen[i] == queen[k] || abs(k - i) == abs(queen[i] - queen[k]))
            return false;
    }
    return true;
}

// 遞歸函數來嘗試放置皇后
void dfs(int k) {
    for(int j = 0; j < n; ++j) {
        if(k == x) {
            queen[k] = y;
            j = n;
        }
        else
            queen[k] = j;
        if(k == n - 1 && canPlaceQ(k)) {
            ans++;
            return;
        }
        else if(canPlaceQ(k))
            dfs(k + 1);
    }
}

int main() {
    while(cin >> n >> x >> y) {
        memset(queen, 0, sizeof queen);
        ans = 0;
        dfs(0);
        if(ans)
            cout << "YES" << '(' << ans << ")\n"; // 輸出答案
        else
            cout << "NO\n"; // 若無解，輸出NO
    }
    return 0;
}

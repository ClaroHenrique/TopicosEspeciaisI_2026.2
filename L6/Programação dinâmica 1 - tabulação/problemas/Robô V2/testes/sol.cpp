#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    if (grid[0][0] == 1 || grid[n - 1][m - 1] == 1) {
        cout << 0 << '\n';
        return 0;
    }

    vector<vector<long long>> dp(n, vector<long long>(m, 0));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            dp[i][j] = grid[i][j];
            if(i > 0) dp[i][j] = max(dp[i][j], grid[i][j]+dp[i-1][j]);
            if(j > 0) dp[i][j] = max(dp[i][j], grid[i][j]+dp[i][j-1]);
        }
    }

    cout << dp[n - 1][m - 1] << '\n';
    return 0;
}

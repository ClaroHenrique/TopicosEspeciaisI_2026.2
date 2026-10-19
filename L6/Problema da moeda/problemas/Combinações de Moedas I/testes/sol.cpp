#include <bits/stdc++.h>
using namespace std;
const int MAXV = 100010;
const int MAXN = 101;
const int INF = 1e9; // 10 ^ 9

int V;
int n, C[MAXN];

int dp[MAXV];

int solve(int v){
    // caso base
    if(v == 0) return 0;
    if(v < 0) return INF;

    // verifica se já foi calculado
    if(dp[v] != -1) return dp[v];

    // armazena o valor calculado 
    int ans = INF;
    for(int i = 0; i < n; i++){
        ans = min(ans, 1 + solve(v - C[i]));
    }
    dp[v] = ans;
    return dp[v];
}

int main(){
    for(int i = 0; i < MAXV; i++) dp[i] = -1;

    cin >> n >> V;
    for(int i = 0; i < n; i++){
        cin >> C[i];
    }
    int ans = solve(V);
    if(ans >= INF){
        cout << -1 << endl;
    }
    else{
        cout << ans << endl;
    }
}

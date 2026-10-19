#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 200100;
const int MOD = 1000000000+7;

int arr[MAXN];
int dp[MAXN];
int n;

int solve(){
    dp[n-1] = 1;
    for(int i = n-2; i >= 0; i--){
        dp[i] = 0;
        for(int j = 1; j <= arr[i] && (i+j) < n; j++){
            dp[i] = (dp[i] + dp[i+j]) % MOD;
        }
    }
    return dp[0];
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    cout << solve() << endl;
}

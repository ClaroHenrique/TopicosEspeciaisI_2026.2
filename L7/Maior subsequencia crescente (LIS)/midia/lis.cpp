#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2000;

int A[MAXN], n;
int dp[MAXN];

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> A[i];
    }

    for(int i = n-1; i >= 0; i--){
        dp[i] = 1;
        for(int j = i+1; j < n; j++){
            if(A[j] > A[i]){
                dp[i] = max(dp[i], 1 + dp[j]);
            }
        }
    }

    int ans = 0;
    for(int i = 0; i < n; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans << endl;
}

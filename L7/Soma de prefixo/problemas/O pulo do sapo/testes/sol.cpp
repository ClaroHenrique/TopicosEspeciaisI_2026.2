#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 200100;
const int MOD = 1000000000+7;

int arr[MAXN];
int dp[MAXN];
int ssum[MAXN];
int n;

int solve(){
    dp[n-1] = 1;
    ssum[n-1] = 1;

    for(int i = n-2; i >= 0; i--){
        if(arr[i] == 0){
            dp[i] = 0;
        } else {
            int r = min(n-1, i+arr[i]);
            if(r == n-1){
                dp[i] = ssum[i+1];
            } else {
                dp[i] = ((ll) MOD + ssum[i+1] - ssum[r+1]) % MOD;
            }
        }
        ssum[i] = (ssum[i+1] + dp[i]) % MOD;
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

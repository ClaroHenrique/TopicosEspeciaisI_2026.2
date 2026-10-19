#include <iostream>
#include <vector>

using namespace std;

int conv(char c){
    if(c == 'A') return 0;
    if(c == 'C') return 1;
    if(c == 'G') return 2;
    if(c == 'T') return 3;
    return -1;
}

const int MAXN = 200010;
const int MAXA = 4;
int dp[MAXN][MAXA];
string s;

int sol(int i, int e){
    if(i == s.size()) return 0;
    if(e == 4) return 0;
    if(dp[i][e] != -1) return dp[i][e];
    
    int vi = conv(s[i]);
    if(vi == e) return dp[i][e] = 1 + sol(i+1, e);
    return dp[i][e] = max(sol(i, e+1), sol(i+1, e));
}

int solve(){
    int n = s.size();
    for(int i = n - 1; i >= 0; i--){
        for(int e = MAXA-1; e >= 0; e--){
            int vi = conv(s[i]);
            if(vi == e) dp[i][e] = 1 + dp[i+1][e];
            else if(e == MAXA-1) dp[i][e] = dp[i+1][e];
            else dp[i][e] = max(dp[i][e+1], dp[i+1][e]);
        }
    }
    int lis = dp[0][0];
    return n - lis;
}

int main() {
    cin >> s;

    // for(int i = 0; i < MAXN; i++){
    //     dp[i][0] = dp[i][1] = dp[i][2] = dp[i][3] = -1; 
    // }
    // cout << s.size()-sol(0, 0) << endl;

    cout << solve() << endl;
    return 0;
}
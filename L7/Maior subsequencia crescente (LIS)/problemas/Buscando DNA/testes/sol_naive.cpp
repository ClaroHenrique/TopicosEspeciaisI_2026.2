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
int dp[MAXN];
string s;

int solve(){
    int n = s.size();
    for(int i = n - 1; i >= 0; i--){
        dp[i] = 1;
        for(int j = i+1; j < n; j++){
            if(s[j] >= s[i]){
                dp[i] = max(dp[i], 1 + dp[j]); 
            }
        }
    }
    int lis = 0;
    for(int i = 0; i < n; i++){
        lis = max(lis, dp[i]);
    }
    return n - lis;
}

int main() {
    cin >> s;

    cout << solve() << endl;
    return 0;
}
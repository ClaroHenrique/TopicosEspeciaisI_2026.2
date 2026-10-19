#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

long long fat(int n){
    if(n == 0) return 1;
    return n * fat(n - 1) % MOD;
}

// (a * b) % M == (a%M) * (b%M) % M

int main(){
    int n;
    cin >> n;

    cout << fat(n) << endl;
}

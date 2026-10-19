#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    vector<int> queries(Q);
    int maxN = 0;

    for (int i = 0; i < Q; i++) {
        cin >> queries[i];
        maxN = max(maxN, queries[i]);
    }

    vector<int> fib(maxN + 1);
    fib[0] = 0;
    if (maxN >= 1) fib[1] = 1;

    for (int i = 2; i <= maxN; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }

    for (int x : queries) {
        cout << fib[x] << '\n';
    }

    return 0;
}
